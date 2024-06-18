# from langchain.chat_models import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
# from app.chat.models import ChatArgs
# from app.chat.vector_store import retriever_map
# from app.chat.llms.chatopenai import build_llm
# from app.chat.memories.sql_memory import build_memory
# from langchain.chains import ConversationalRetrievalChain
# from app.chat.vector_store.pinecone import build_retriever
# import warnings

# # Ignorar todas las advertencias de LangChain deprecado
# warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

# def conversationalRetrievalChain2(chat_args: ChatArgs):
#     retriever = build_retriever(chat_args)
#     llm = build_llm(chat_args)
#     memory = build_memory(chat_args)

#     return ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         memory=memory,
#         retriever=retriever
#     )
