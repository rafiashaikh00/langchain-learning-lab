#import streamlit as st
#from langchain_ollama import ChatOllama

# Create the model
#model = ChatOllama(
#    model="llama3.2:1b"
#)

# Streamlit UI
#st.header("Research Tool")

# User input
#user_input = st.text_input("Enter Your Prompt")

# Button
#if st.button("Summarize"):
#    result = model.invoke(user_input)
#  st.write(result.content)


#code 2


from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatOllama(
    model="llama3.2:1b"
)

st.header('Research Tool')
#select box se drop down create huta hn
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
#template
template=PromptTemplate(template=
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
""",
#"Mere template me ye 3 placeholders hain. Baad me inki values aa kar fill hongi
input_variables=['paper_input','style_input','length_input']
)
#fill the place holder jo uper present hn
prompt=template.invoke(
    {
       'paper_input' : paper_input,
       'style_input'  : style_input,
       'length_input' : length_input

    }
)


if st.button("Summarize"):
    st.write(prompt.to_string())
    #cause prompt behave as obj so convert in string

    result = model.invoke(prompt.to_string())

    st.write(result.content)

