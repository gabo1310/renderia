from .pinecone import build_retriever
from functools import partial
retriever_map = {
    "pinecone_1":partial(build_retriever, k=4),
    "pinecone_2":partial(build_retriever, k=6),
    "pinecone_3":partial(build_retriever, k=8),
    "pinecone_4":partial(build_retriever, k=10),

}