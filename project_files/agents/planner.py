from langchain_google_genai import ChatGoogleGenerativeAI
from project_files.configs import GEMINI_API_KEY, MODEL_NAME

def create_brief(topic, audience="Data professionals"):
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=GEMINI_API_KEY)
    prompt = f"""
    Create a LinkedIn content brief for the topic: {topic}.
    Audience: {audience}
    Include: angle, 3 key points, suggested title, desired outcome.
    """
    return llm.invoke(prompt).content