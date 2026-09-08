from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
#tool banate hn
@tool
def multiply(a:int,b:int)->int:
    """Given two numbers a and b this tool returns their product"""
    return a*b
#tool binding 
model=ChatOllama(model='llama3.2:1b')
#func name bind tools jis se hum tools ko llm k sath join krty hn
llm_with_tools=model.bind_tools([multiply])
#future mein jab llm ko multiply func perform krna huga so it call this tool to do so more perfectly ye kam kre ga
#tool calling
query=HumanMessage(content="What is 5 multiplied by 7?")
#we are making a list hwhere store our messages
messages=[query]
result2=llm_with_tools.invoke(messages)
#ai suggest walal be mess me jae ga
messages.append(result2)

tols_call=multiply.invoke(result2.tool_calls[0])
#yha tools ka jo mess hn wo eb meessage k pas gya
messages.append(tols_call)
#ab pori histiory hum llm ko dege
#rem messages is a list to he use append
#giving back reuskt to ai so he or she convert in to ai message format
llm_result=llm_with_tools.invoke(messages)
print(llm_result)