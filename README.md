# LinkedIn-Content-Creation-Assistant

Automate LinkedIn post creation with Generative AI (Google Gemini) and Streamlit, leveraging past posts to maintain personal style and tone.

### Project Overview

LinkedIn Content Creation Assistant is a Generative AI application designed to help professionals automatically generate high quality LinkedIn posts from given topics. 
It leverages past posts to maintain your unique writing style and applies structured content frameworks (Hook, Body, CTA, Hashtags) to maximize engagement.

### Key features

- Personalized post generation using Google Gemini.

- RAG-inspired modular workflow with evidence retrieval and style fine-tuning.

- Compliance and moderation checks to maintain professional tone.

- Streamlit interface for easy topic input and post preview.

### Project Struture

```
LinkedIn-Content-Creation-Assistant/
│
├── app/
│   ├── config.py              # Environment variables & model config
│   ├── graph.py               # Orchestrates the pipeline (Planner → Researcher → Writer → Editor → Compliance)
│   ├── tools/                 # Helper modules
│   │   ├── search_tool.py     # Web search for evidence
│   │   ├── scrape_tool.py     # Extract content from URLs
│   │   ├── vectorstore.py     # Embeddings & vector DB
│   │   ├── moderation.py      # Toxicity & compliance check
│   │   └── voice_profile.py   # Load past posts for style
│   ├── agents/                # Modular AI agents
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── writer.py
│   │   ├── editor.py
│   │   └── compliance.py
│   └── utils.py
│
├── data/
│   ├── voice/past_posts.csv  # Sample past LinkedIn posts
│   └── cache/
│
├── streamlit_app.py          # Streamlit UI entrypoint
├── requirements.txt
├── .env                      # API keys (e.g., GEMINI_API_KEY)
└── README.md
```


### Setup Instructions

1. Clone the repository:
```
git clone https://github.com/RushikeshDhaigude/LinkedIn-Content-Creation-Assistant.git
cd LinkedIn-Content-Creation-Assistant
```

2. Install dependencies:
```
pip install -r requirements.txt
```

4. Add your Gemini API key in .env:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

6. Run the Streamlit app:
```
streamlit run streamlit_app.py
```

### How It Works

1. Planner: Generates a content brief and angles for the given topic.

2. Researcher: Gathers evidence via web search and scraping.

3. Writer: Drafts multiple post variants, structured into Hook, Body, CTA, Hashtags.

4. Editor: Refines posts for clarity, conciseness, and engagement.

5. Compliance: Checks for toxicity, length, and professional tone.

6. Voice Profile: Ensures posts match the user’s previous style and tone.
