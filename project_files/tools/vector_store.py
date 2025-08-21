from langchain_google_genai import GoogleGenerativeAIEmbeddings
import chromadb
from project_files.configs import GEMINI_API_KEY, VECTOR_DB_DIR,MODEL_NAME

def get_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(model=MODEL_NAME, google_api_key=GEMINI_API_KEY)
    client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
    return client, embeddings