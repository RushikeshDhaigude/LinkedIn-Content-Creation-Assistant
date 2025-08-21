def check_toxicity(text):
    """Basic keyword filter (extend with LLM for production)."""
    bad_words = ["hate", "violence", "racist"]
    return any(bad in text.lower() for bad in bad_words)