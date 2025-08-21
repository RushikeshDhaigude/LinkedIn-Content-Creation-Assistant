from langchain_google_genai import ChatGoogleGenerativeAI
from project_files.configs import GEMINI_API_KEY, MODEL_NAME

def draft_posts(topic, evidence, voice_profile):
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=GEMINI_API_KEY)
    prompt = f"""
    Write 2 LinkedIn post drafts on "{topic}" for tech audience.
    Use evidence below and match voice style:
    Voice profile: {voice_profile}
    Evidence: {evidence}

    Output format:
    - Variant A: Hook, Body, CTA, Hashtags
    - Variant B: Hook, Body, CTA, Hashtags
    """
    return llm.invoke(prompt).content