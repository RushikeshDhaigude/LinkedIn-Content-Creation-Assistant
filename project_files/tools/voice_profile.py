import pandas as pd
from project_files.configs import VOICE_PROFILE_PATH

def load_voice_profile():
    df = pd.read_csv(VOICE_PROFILE_PATH)
    all_text = " ".join(df["post_text"].dropna().tolist())
    return all_text[:3000]  # Keep a manageable token count