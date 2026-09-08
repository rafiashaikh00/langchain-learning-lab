from langchain_core.tools import tool
from langchain_ollama import ChatOllama
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent,AgentExecutor
from langchain.agents import create_agent
from langchain import hub
#this is atool 
search_tool=DuckDuckGoSearchRun()
result=search_tool.invoke("today pakistan news ")
print(result)
#llm jo ai agnet ko reasoning capibility provide krta hn
model=ChatOllama(model='llama3.2:1b')
#step2 we calling prompt taht is predefined present in hub
prompt=hub.pull("hwchase17/react")# pull teh standard react prompt cause we wnat to use react agent
#step2 agent create hume es agemt ko model+tool +prompt dena huta hn
#here u decide konsa agent use karo ge
agent=create_react_agent(
    llm=model,
    tools=[search_tool],
    prompt=prompt
)
#step3 wrap it with agent excutor,basically agent_executior is teh guy jo agent ki bat man ke kam krta hn agent basiaclly who palin every thing stat to stop
agent_executor=AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
    #es se ye huga agent soochy ag wo be hume dekhai dega
)
#step 4 Invoke
response=agent_executor.invoke({'input':'3 ways to reach goa from pakistan'})
print(response)

