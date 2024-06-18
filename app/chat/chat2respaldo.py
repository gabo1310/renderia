

# from langchain.chat_models import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
# from app.chat.models import ChatArgs
# from app.chat.vector_store import retriever_map
# from app.chat.llms.chatopenai import build_llm
# from app.chat.memories.sql_memory import build_memory
# from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
# from app.web.api import (
#     set_conversation_components,
#     get_conversation_components
# )
# import random
# from app.chat.llms import llm_map
# from app.chat.memories import memory_map
# from app.chat.score import random_component_by_score
# from langchain.prompts import PromptTemplate
# import os
# import warnings

# # Ignorar todas las advertencias de LangChain deprecado
# warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

# CONDENSE_QUESTION_PROMPT = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template="""
# Using the provided documents and incorporating relevant context from the conversation history, rewrite the following query.
# {chat_history}
# The rewritten query should:
# - Preserve the core intent and meaning of the original query
# - Expand and clarify the query to make it more specific and informative for retrieving relevant context
# - Avoid introducing new topics or queries that deviate from the original query
# - DONT EVER question the Original query, but instead focus on rephrasing and expanding it into a new query
# -the question must be in spanish
# Return ONLY the rewritten query text, without any additional formatting or explanations.
# Original question:
# {question}

# """
# )

# COMBINE_DOCS_PROMPT = PromptTemplate(
#     input_variables=["docs", "question"],
#     template="""
# You are a knowledgeable assistant. You have been provided with the following documents:
# {docs}
# Using the provided documents, answer the following question:
# {question}
# Answer:
# """
# )


# def select_component(
#     component_type, component_map, chat_args
# ):
#     components = get_conversation_components(chat_args.conversation_id)
#     previous_component = components[component_type]

#     if previous_component:
#         builder = component_map[previous_component]
#         return previous_component, builder(chat_args)
#     else:
#         random_name = random_component_by_score(component_type, component_map)
#         builder = component_map[random_name]
#         return random_name, builder(chat_args)

# def build_chat(chat_args: ChatArgs):
#     retriever_name, retriever = select_component("retriever", retriever_map, chat_args)
#     llm_name, llm = select_component("llm", llm_map, chat_args)
#     memory_name, memory = select_component("memory", memory_map, chat_args)

#     print("###############################")
#     print(f"memoria: {memory_name}, llm: {llm_name}, retriever: {retriever_name}")
#     print(f"metadata: {chat_args.metadata}")  # Verificar metadata incluyendo el prompt
#     print("###############################")
    
#     set_conversation_components(chat_args.conversation_id, llm=llm_name, retriever=retriever_name, memory=memory_name)

#     if llm_name == "claude-3":
#         condense_question_llm = ChatAnthropic(temperature=0, model_name="claude-3-opus-20240229")
#     else:
#         condense_question_llm = ChatOpenAI(streaming=False, temperature=0.7)

#     return StreamingConversationalRetrievalChain.from_llm(
#         llm=llm,
#         condense_question_llm=condense_question_llm,
#         memory=memory,
#         retriever=retriever,
#         metadata=chat_args.metadata,
#         condense_question_prompt=CONDENSE_QUESTION_PROMPT,
#         combine_docs_prompt=COMBINE_DOCS_PROMPT
#     )
#-------------------------------------------
#-------------------------------------------

from flask import session
from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from app.chat.models import ChatArgs
from app.chat.vector_store import retriever_map
from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from app.web.api import (
    set_conversation_components,
    get_conversation_components
)
import random
from app.chat.llms import llm_map
from app.chat.memories import memory_map
from app.chat.score import random_component_by_score
from langchain.prompts import PromptTemplate
import os
import warnings

# Ignorar todas las advertencias de LangChain deprecado
warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')



DEFAULT_CONDENSE_QUESTION_PROMPT = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""
Using the provided documents and incorporating relevant context from the conversation history, rewrite the following query.
{chat_history}
The rewritten query should:
- Preserve the core intent and meaning of the original query
- Expand and clarify the query to make it more specific and informative for retrieving relevant context
- Avoid introducing new topics or queries that deviate from the original query
- DONT EVER question the Original query, but instead focus on rephrasing and expanding it into a new query
-the question must be in spanish
Return ONLY the rewritten query text, without any additional formatting or explanations.
Original question:
{question}

"""
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

def select_component(
    component_type, component_map, chat_args
):
    components = get_conversation_components(chat_args.conversation_id)
    previous_component = components[component_type]

    if previous_component:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)
    else:
        random_name = random_component_by_score(component_type, component_map)
        builder = component_map[random_name]
        return random_name, builder(chat_args)

def build_chat(chat_args: ChatArgs):
    retriever_name, retriever = select_component("retriever", retriever_map, chat_args)
    llm_name, llm = select_component("llm", llm_map, chat_args)
    memory_name, memory = select_component("memory", memory_map, chat_args)

    print("###############################")
    print(f"memoria: {memory_name}, llm: {llm_name}, retriever: {retriever_name}")
    print(f"metadata: {chat_args.metadata}")  # Verificar metadata incluyendo el prompt
    print("###############################")
    
    set_conversation_components(chat_args.conversation_id, llm=llm_name, retriever=retriever_name, memory=memory_name)

    if llm_name == "claude-3":
        condense_question_llm = ChatAnthropic(temperature=0, model_name="claude-3-opus-20240229")
    else:
        condense_question_llm = ChatOpenAI(streaming=False, temperature=0.7)

    # Obtener el prompt personalizado de la sesión, si está disponible
    custom_prompt_text = session.get("custom_prompt", "")

    # Crear el PromptTemplate combinado
    combine_docs_prompt = PromptTemplate(
        input_variables=["docs", "question"],
        template=f"""
        You are a knowledgeable assistant. You have been provided with the following documents:
        {{docs}}
        -{custom_prompt_text}
        -Using the provided documents, answer the following question:
        {{question}}
        Answer:
        """
    )

    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever,
        metadata=chat_args.metadata,
        condense_question_prompt=DEFAULT_CONDENSE_QUESTION_PROMPT,
        combine_docs_prompt=combine_docs_prompt
    )







# Definición de los prompts personalizados usando PromptTemplate
# DEFAULT_CONDENSE_QUESTION_PROMPT = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template="""
# Your task is to refine a question for more accurate retrieval of information.
# Here is the conversation so far:
# {chat_history}
# Here is the question to be refined:
# {question}
# Refined question:
# """
# )