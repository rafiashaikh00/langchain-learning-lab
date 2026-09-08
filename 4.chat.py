from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
model=ChatOllama( 
    model='llama3.2:1b',
    temperature=0
)
#infinite loop chlae ge jo chlta jae ga untill user stop nhi krta
""" this code is work fine but it not last the memory 
while True:
    #we take input from user
    user_input=input("You:")
    if user_input=='exit':
        break
    result= model.invoke(user_input)
    print("AI",result.content)"""
chat_history=[
    SystemMessage(content='You are helpfull AI Assistant')
]
while True:
    user_input=input("You:")
    #jo be userinput put kare ga hum us koa append krty jae ge caht history me
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    #jo nya result aya hn us ko be append kare 
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)
#print entitre chat
#print(chat_history)
#isinstance ye bta ta hn obj es class ka hn ya nhi mess is obj humanmess is class
#thsi print teh entire chat a good format clena clear 
for mess in chat_history:
  if isinstance(mess,HumanMessage):
    print("human",mess.content)
  elif isinstance(mess,AIMessage):
    print("AI",mess.content)
  else:
    print("System",mess.content)





