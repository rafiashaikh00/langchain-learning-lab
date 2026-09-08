from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
#we add header
st.header('Research Tool')
#input box ,user put their input and we store in varaible
user_input=st.text_input('Enter Your Prompt')
#we make button
if st.button('Summarize'):
    #jo input huga wo model us ka response dega that store in result
    result=model.invoke(user_input)
    #prnt teh response on webpage
    st.write(result.content)
"""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}

Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

3. If certain information is not available in the paper, respond with:
   "Insufficient information available"
   instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length. 
"""
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)


style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)
if st.button('Summarize'):
    
    st.write("hello")