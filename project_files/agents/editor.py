from langchain_google_genai import ChatGoogleGenerativeAI
from project_files.configs import GEMINI_API_KEY, MODEL_NAME

def refine_post(post_text):
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=GEMINI_API_KEY)
    prompt = f"Edit the following LinkedIn post for clarity, conciseness, and impact:\n{post_text}"
    return llm.invoke(prompt).content