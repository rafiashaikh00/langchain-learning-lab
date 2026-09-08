"""from langchain_openai import ChatOpenAI
#we take this labriry 
from dotenv import load_dotenv
#call cahtopenaoi
load_dotenv()
#make object and write model name store in varaible,temp tell how creative ans should be
model=ChatOpenAI(model="gpt-4",temperature=1.5,max_completion_tokens=10)
#we call this model and ask ques and store value in varble
result=model.invoke("what is acpital of pak")
print(result.content)#give exact result"""








f"""rom langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
#call the function
load_dotenv()
#create llm end pouint and neech we will use
llm=HuggingFaceEndpoint(
 repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
 task="text-generation"



)
#llm nam kaa parameter huta hn wo value pass karo
model=ChatHuggingFace(llm=llm)

result=model.invoke("who is the capital of india")
print(result.content)"""
"""from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))"""

#ollamaki class import kr rhy hn

from langchain_ollama import ChatOllama
#class ka obj banae ge
model=ChatOllama( 
    model='llama3.2:1b',
    temperature=0
)
#temp 0 harr bar same ans temp 0.5 thora creative temp 1 always change in all run
result=model.invoke("generate 5 bullets points each linme have three dots")
print(result.content)

