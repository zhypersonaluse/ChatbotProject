from dotenv import load_dotenv

load_dotenv()

from document_preparation import read_single_pdf, split_documents
from db_tools import intial_embedding, initial_db

MODEL_NAME = "gpt-4o"
FILE_PATH_C1 = "./data/bcbsc125.pdf"
C1_DB_PATH = "./C1_DB"
FILE_PATH_C2 = "./data/FairLendingACt.pdf"
C2_DB_PATH = "./C2_DB"


file_content_C1 = read_single_pdf(FILE_PATH_C1)
file_content_C2 = read_single_pdf(FILE_PATH_C2)
split_docs_C1 = split_documents(file_content_C1, chunk_size=1000, chunk_overlap=200)
split_docs_C2 = split_documents(file_content_C2, chunk_size=1000, chunk_overlap=200)
embedding = intial_embedding(MODEL_NAME)
db_C1 = initial_db("Company-One", embedding=embedding, db_path=C1_DB_PATH)
db_C2 = initial_db("Company-Two", embedding=embedding, db_path=C2_DB_PATH)


if __name__ == "__main__":
    print("Chatbot")
