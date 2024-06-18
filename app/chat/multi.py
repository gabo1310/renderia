# import os
# import re
# import pinecone
# from langchain.vectorstores import Pinecone as LangchainPinecone
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI
# import warnings
# from dotenv import load_dotenv
# from flask import session

# # Cargar variables de entorno desde el archivo .env
# load_dotenv()

# # Ignorar todas las advertencias de LangChain deprecado
# warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

# # Inicializar Pinecone
# pc = pinecone.Pinecone(
#     api_key=os.getenv("PINECONE_API_KEY"),
#     environment=os.getenv("PINECONE_ENV_NAME")
# )


# # Usar el índice existente
# embeddings = OpenAIEmbeddings()
# vector_store = LangchainPinecone.from_existing_index(
#     os.getenv("PINECONE_INDEX_NAME"), embeddings
# )

# DEFAULT_COMBINE_DOCS_PROMPT = PromptTemplate(
#     input_variables=["docs", "question"],
#     template="""
# You are a knowledgeable assistant. You have been provided with the 
# following documents:
# {docs}
# Using the provided documents, answer the following question:
# {question}
# Answer:
# """
# )

# def parse_questions(text):
#     questions = text.strip().split('\n\n')  # Divide por saltos de línea dobles
#     parsed_questions = []
#     for i, question in enumerate(questions):
#         parsed_questions.append({
#             'number': i + 1,
#             'question': question.strip()
#         })
#     return parsed_questions

# def send_to_llm(question, prompt1, llm):
#     combined_prompt = f"{prompt1}\n\n{question}"
#     prompt = DEFAULT_COMBINE_DOCS_PROMPT.format(docs="No documents available", question=combined_prompt)
    
#     try:
#         response = llm.predict(prompt)
#         print(f"Respuesta del LLM: {response}")
#         return response
#     except Exception as e:
#         print(f"Error al obtener la respuesta del LLM: {e}")
#         return None

# def handle_prompts(data):
#     prompt1 = data.get('prompt1')
#     prompt2 = data.get('prompt2')

#     # Imprimir los valores de los prompts
#     print(f"Prompt 1: {prompt1}")
#     print("-----------------------")
#     print(f"Prompt 2: {prompt2}")
#     print("-----------------------")
#     print("entro")
#     print("-----------------------")
    
#     questions = parse_questions(prompt2)
#     print(f"Preguntas parsed: {questions}")  # Registro de depuración

#     llm = ChatOpenAI(model_name="gpt-4", temperature=0.3)  # Asegúrate de tener la API key configurada en tu entorno

#     results = []
#     for question in questions:
#         response = send_to_llm(question['question'], prompt1, llm)
#         if response:
#             results.append({
#                 "question": question['question'],
#                 "response": response
#             })
#             # Imprimir la respuesta del LLM
#             print(f"Respuesta del LLM para '{question['question']}': {response}")
#         else:
#             print(f"No se obtuvo respuesta para la pregunta: {question['question']}")

#     # Escribir los resultados en un archivo de texto
#     try:
#         with open('resultados.txt', 'w', encoding='utf-8') as file:
#             for result in results:
#                 file.write(f"Pregunta: {result['question']}\n")
#                 file.write(f"Respuesta: {result['response']}\n")
#                 file.write("----------\n")
#         print("Archivo 'resultados.txt' creado exitosamente.")
#         return {"message": "Archivo creado"}
#     except Exception as e:
#         print(f"Error al escribir en el archivo: {e}")
#         return {"message": "Error al crear el archivo"}


# import os
# import re
# import pinecone
# from functools import partial
# from langchain.vectorstores import Pinecone as LangchainPinecone
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI
# import warnings
# from dotenv import load_dotenv

# # Cargar variables de entorno desde el archivo .env
# load_dotenv()

# # Ignorar todas las advertencias de LangChain deprecado
# warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

# # Inicializar Pinecone
# pc = pinecone.Pinecone(
#     api_key=os.getenv("PINECONE_API_KEY"),
#     environment=os.getenv("PINECONE_ENV_NAME")
# )

# # Usar el índice existente
# embeddings = OpenAIEmbeddings()
# vector_store = LangchainPinecone.from_existing_index(
#     os.getenv("PINECONE_INDEX_NAME"), embeddings
# )







# DEFAULT_COMBINE_DOCS_PROMPT = PromptTemplate(
#     input_variables=["docs", "question"],
#     template="""
# You are a knowledgeable assistant. You have been provided with the 
# following documents:
# {docs}
# Using the provided documents, answer the following question:
# {question}
# Answer:
# """
# )

# def parse_questions(text):
#     questions = text.strip().split('\n\n')  # Divide por saltos de línea dobles
#     parsed_questions = []
#     for i, question in enumerate(questions):
#         parsed_questions.append({
#             'number': i + 1,
#             'question': question.strip()
#         })
#     return parsed_questions

# def send_to_llm(question, prompt1, llm):
#     combined_prompt = f"{prompt1}\n\n{question}"
#     prompt = DEFAULT_COMBINE_DOCS_PROMPT.format(docs="No documents available", question=combined_prompt)
    
#     try:
#         response = llm.predict(prompt)
#         print(f"Respuesta del LLM: {response}")
#         return response
#     except Exception as e:
#         print(f"Error al obtener la respuesta del LLM: {e}")
#         return None

# def handle_prompts(data):
#     prompt1 = data.get('prompt1')
#     prompt2 = data.get('prompt2')

#     # Imprimir los valores de los prompts
#     print(f"Prompt 1: {prompt1}")
#     print("-----------------------")
#     print(f"Prompt 2: {prompt2}")
    
#     questions = parse_questions(prompt2)
#     print(f"Preguntas parsed: {questions}")  # Registro de depuración

#     llm = ChatOpenAI(model_name="gpt-4o", temperature=0.3)  # Asegúrate de tener la API key configurada en tu entorno

#     results = []
#     for question in questions:
#         response = send_to_llm(question['question'], prompt1, llm)
#         if response:
#             results.append({
#                 "question": question['question'],
#                 "response": response
#             })
#             # Imprimir la respuesta del LLM
#             print(f"Respuesta del LLM para '{question['question']}': {response}")
#         else:
#             print(f"No se obtuvo respuesta para la pregunta: {question['question']}")

#     # Escribir los resultados en un archivo de texto
#     try:
#         with open('resultados.txt', 'w', encoding='utf-8') as file:
#             print("paso por aca1")
#             for result in results:
#                 file.write(f"Pregunta: {result['question']}\n")
#                 file.write(f"Respuesta: {result['response']}\n")
#                 print("paso por aca2")
#                 file.write("----------\n")
#         print("Archivo 'resultados.txt' creado exitosamente.")
#     except Exception as e:
#         print(f"Error al escribir en el archivo: {e}")
#         return {"message": "Error al crear el archivo"}

#     return {"message": "Archivo creado"}

#..........................................................
#..........................................................
#..........................................................
#..........................................................
#..........................................................


# multi.py

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

def parse_questions(text):
    questions = text.strip().split('\n\n')  # Divide por saltos de línea dobles
    parsed_questions = []
    for i, question in enumerate(questions):
        parsed_questions.append({
            'number': i + 1,
            'question': question.strip()
        })
    return parsed_questions

def send_to_llm(question, prompt1, llm):
    combined_prompt = f"{prompt1}\n\n{question}"
    prompt = DEFAULT_COMBINE_DOCS_PROMPT.format(docs="No documents available", question=combined_prompt)
    
    try:
        response = llm.predict(prompt)
        print(f"Respuesta del LLM: {response}")
        return response
    except Exception as e:
        print(f"Error al obtener la respuesta del LLM: {e}")
        return None

def handle_prompts(data):
    prompt1 = data.get('prompt1')
    prompt2 = data.get('prompt2')

    # Imprimir los valores de los prompts
    print(f"Prompt 1: {prompt1}")
    print("-----------------------")
    print(f"Prompt 2: {prompt2}")
    
    questions = parse_questions(prompt2)
    print(f"Preguntas parsed: {questions}")  # Registro de depuración

    llm = ChatOpenAI(model_name="gpt-4", temperature=0.3)  # Asegúrate de tener la API key configurada en tu entorno

    results = []
    for question in questions:
        response = send_to_llm(question['question'], prompt1, llm)
        if response:
            results.append({
                "question": question['question'],
                "response": response
            })
            # Imprimir la respuesta del LLM
            print(f"Respuesta del LLM para '{question['question']}': {response}")
        else:
            print(f"No se obtuvo respuesta para la pregunta: {question['question']}")

    return results
