from dotenv import load_dotenv

load_dotenv()

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def intial_embedding():
    """
    Intialize an embedding function.
    Args:
        model_name: name of the model used
    Return:
        embedding: Embedding model
    """
    print("Intialize Embedding Model")
    embedding = OpenAIEmbeddings()
    return embedding


def initial_db(docs, collection_name: str, embedding, db_path: str):
    """
    Intialize an vector database.
    Args:
        collection_name: name of the model used
        embedding
        db_path
    Return:
        db: vector_database
    """
    print(f"Initialize vector database for {collection_name}")
    db = Chroma.from_documents(
        documents= docs,
        collection_name=collection_name,
        embedding=embedding,
        persist_directory=db_path,
    )


def get_retriever(collection_name: str, embedding, db_path: str):
    retriever = Chroma(
        collection_name = collection_name,
        persist_directory= db_path,
        embedding_function= embedding
    ).as_retriever()
    return retriever