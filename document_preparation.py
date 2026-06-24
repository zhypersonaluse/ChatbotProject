from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def read_single_pdf(file_path: str):
    """
    This function loads a file from the given path.

    :param file_path: the path to the file to be loaded
    :return: the content of the file
    """
    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()
    return documents


def read_folders(folder_path: str):
    pass


def split_documents(documents, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    split_docs = splitter.split_documents(documents)
    return split_docs
