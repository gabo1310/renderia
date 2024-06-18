import os
import re
import pinecone
from functools import partial
from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import warnings
from dotenv import load_dotenv

import warnings
from flask import session

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Ignorar todas las advertencias de LangChain deprecado
warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

# Inicializar Pinecone
pc = pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

# Usar el índice existente
embeddings = OpenAIEmbeddings()
vector_store = LangchainPinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)

# def build_retriever(chat_args, k):
#     pdf_ids_to_search = [chat_args.get('pdf_id')]  # Obtener las IDs de la sesión
#     if isinstance(pdf_ids_to_search, str):
#         pdf_ids_to_search = [pdf_ids_to_search]  # Convertir a lista si es una cadena
    
#     search_kwargs = {"filter": {"pdf_id": {"$in": pdf_ids_to_search}}, "k": k}
#     return vector_store.as_retriever(
#         search_kwargs=search_kwargs
#     )

# retriever_map = {
#     "pinecone_1": partial(build_retriever, k=10),
# }
from langchain.embeddings import OpenAIEmbeddings
import warnings



def build_retriever(chat_args, k):
    embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
    # Eliminar el filtro de búsqueda específico de pdf_id para buscar en todos los documentos
    search_kwargs = {"k": k}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )

retriever_map = {
    "pinecone_1": partial(build_retriever, k=10),
}

# Define los prompts personalizados usando PromptTemplate
DEFAULT_COMBINE_DOCS_PROMPT = PromptTemplate(
    input_variables=["docs", "question"],
    template="""
You are a knowledgeable assistant. You have been provided with the 
following documents:
{docs}
Using the provided documents, answer the following question:
{question}
Answer:
"""
)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_questions(text):
    pattern = re.compile(r'(\d+)\. (.+)')
    matches = pattern.findall(text)
    
    questions = []
    for match in matches:
        question_number = int(match[0])
        question_text = match[1].strip()
        
        questions.append({
            'number': question_number,
            'question': question_text
        })
    
    return questions

def send_to_llm(question, llm):
    prompt = DEFAULT_COMBINE_DOCS_PROMPT.format(docs="No documents available", question=question)
    response = llm.predict(prompt)
    return response

def main():
    file_path = 'promptDatos.txt'
    text = read_file(file_path)
    questions = parse_questions(text)

    for question in questions:
        print(f"Pregunta {question['number']}: {question['question']}")

    # Configurar el LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0.3)  # Asegúrate de tener la API key configurada en tu entorno

    with open('resultados.txt', 'w', encoding='utf-8') as file:
        for question in questions:
            response = send_to_llm(question['question'], llm)
            file.write(f"Pregunta {question['number']}: {question['question']}\n")
            file.write(f"Respuesta: {response}\n")
            file.write("----------\n")
            print(f"Pregunta {question['number']} procesada.")

if __name__ == '__main__':
    main()
