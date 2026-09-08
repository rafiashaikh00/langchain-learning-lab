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

result=llm_with_tools.invoke( "What is 5 multiplied by 7?")
#tool calling just suggets ypu his query ans krne time ab ye tool use kro thsi is output
#[{'name': 'multiply', 'args': {'a': '5', 'b': '7'}, 'id': 'a1c903fa-0403-4094-b467-d23d75c2e3d1', 'type': 'tool_call'}]
#here i have to pass message not a nad b values wo tool k parameters hn
#llm says bhai ap a ka value 5 rkho b ka value 7 rkho and mul waly tool ko bolao wo apka kam sai kare ga himself llm ans tool s nhi nekale ga
#Instead, the LLM looks at the available tools and the user's query, and generates a tool call for the tool it thinks is appropriate:
#print(result.tool_calls[0]['args'])#with zero se humaar first tool and us k arugemnt hunge wo jo aurgy hunge us ko hum pass kare ge kudh func ko call kr ke

#Tools excution  args se kya huga mere func ko pas argumnet mily ge sara nam kuch nhi aje ga
a=multiply.invoke(result.tool_calls[0]['args'])
#llm ne ek revelant list dei hn tools ki ok jo query se fit hu rhy hn us list me se first tool hum kudh select kre ge fir multiply func ko call kya us me  srai detials pass kr rhy hn
print(a)
#es ka matalb hn pora resilt m jo srae tool aae query k hesa se unh list m se first tool jo mul wala hn us  wo
#a=multiply.invoke(result.tool_calls[0])




#---------------version 2 ------- es me hum pori converstauin llm ko dege tak us ko humara ans pta chly
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
query=HumanMessage("What is 5 multiplied by 7?")
#we are making a list hwhere store our messages
messages=[query]
result2=llm_with_tools.invoke(messages)
#ai suggest walal be mess me jae ga
messages.invoke(result2)

tols_call=multiply.invoke(result.tool_calls[0])
#yha tools ka jo mess hn wo eb meessage k pas gya
messages.invoke(tols_call)
#ab pori histiory hum llm ko dege

llm_result=llm_with_tools.invoke(messages)
print(llm_result)