from dotenv import load_dotenv

load_dotenv()

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def intial_embedding(model_name: str):
    """
    Intialize an embedding function.
    Args:
        model_name: name of the model used
    Return:
        embedding: Embedding model
    """
    print("Intialize Embedding Model")
    embedding = OpenAIEmbeddings(model=model_name)
    return embedding


def initial_db(collection_name: str, embedding, db_path: str):
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
    db = Chroma(
        collection_name=collection_name,
        embedding_function=embedding,
        persist_directory=db_path,
    )
    return db
