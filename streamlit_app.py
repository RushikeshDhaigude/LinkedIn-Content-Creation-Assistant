import streamlit as st
from project_files.graph import generate_linkedin_posts

st.set_page_config(page_title="LinkedIn Content Co-Pilot", layout="wide")

st.title("LinkedIn Content Co-Pilot")
topic = st.text_input("Enter a topic for your LinkedIn post")

if st.button("Generate"):
    with st.spinner("Researching and drafting..."):
        output = generate_linkedin_posts(topic)
    
    st.subheader("Content Brief")
    st.write(output["brief"])
    
    # st.subheader("Evidence Sources")
    # st.write(output["evidence"])
    
    st.subheader("Draft Variants")
    for i, v in enumerate(output["variants"], 1):
        st.markdown(f"**Variant {i}:**\n\n{v}")
