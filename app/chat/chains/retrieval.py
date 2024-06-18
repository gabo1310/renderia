# from langchain.chains import ConversationalRetrievalChain
# from app.chat.chains.streamable import StreamableChain
# from app.chat.chains.traceable import TraceableChain
# # warnings_filter.py
# import warnings

# # Ignorar todas las advertencias de LangChain deprecado
# warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')



# class StreamingConversationalRetrievalChain(
#     TraceableChain, StreamableChain, ConversationalRetrievalChain
# ):
#     pass

# from langchain.chains import ConversationalRetrievalChain, LLMChain
# from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
# from app.chat.chains.streamable import StreamableChain
# from app.chat.chains.traceable import TraceableChain
# from langchain.prompts import PromptTemplate
# import warnings
# import asyncio

# # Ignorar todas las advertencias de LangChain deprecado
# warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

# class CustomCombineDocumentsChain(BaseCombineDocumentsChain):
#     def combine_docs(self, docs, **kwargs):
#         combined_text = " ".join([doc.page_content for doc in docs])  # Usar el atributo correcto
#         return combined_text, {}

#     async def acombine_docs(self, docs, **kwargs):
#         combined_text = " ".join([doc.page_content for doc in docs])  # Usar el atributo correcto
#         return combined_text, {}

# class StreamingConversationalRetrievalChain(
#     TraceableChain, StreamableChain, ConversationalRetrievalChain
# ):
#     @classmethod
#     def from_llm(cls, llm, condense_question_llm, memory, retriever, metadata, condense_question_prompt, combine_docs_prompt):
#         condense_question_chain = LLMChain(
#             llm=condense_question_llm, prompt=condense_question_prompt
#         )
#         combine_docs_chain = CustomCombineDocumentsChain(
#             llm_chain=LLMChain(llm=llm, prompt=combine_docs_prompt)
#         )
#         return cls(
#             question_generator=condense_question_chain,
#             combine_docs_chain=combine_docs_chain,
#             memory=memory,
#             retriever=retriever,
#             metadata=metadata
#         )

from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from app.chat.chains.streamable import StreamableChain
from app.chat.chains.traceable import TraceableChain
from langchain.prompts import PromptTemplate
import warnings
import asyncio

# Ignorar todas las advertencias de LangChain deprecado
warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

class StreamingConversationalRetrievalChain(
    TraceableChain, StreamableChain, ConversationalRetrievalChain
):
    @classmethod
    def from_llm(cls, llm, condense_question_llm, memory, retriever, metadata, condense_question_prompt, combine_docs_prompt):
        condense_question_chain = LLMChain(
            llm=condense_question_llm, prompt=condense_question_prompt
        )
        combine_docs_chain = StuffDocumentsChain(
            llm_chain=LLMChain(llm=llm, prompt=combine_docs_prompt),
            document_variable_name="docs"  # Añadir el nombre de variable de documento
        )
        return cls(
            question_generator=condense_question_chain,
            combine_docs_chain=combine_docs_chain,
            memory=memory,
            retriever=retriever,
            metadata=metadata
        )
