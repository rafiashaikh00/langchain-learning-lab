"""from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_ollama import ChatOllama
model=ChatOllama(model="llama3.2:1b")
messages=[
       SystemMessage(content='You are a helpful assistant'),
       HumanMessage(content="Explain langchain")


]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)"""

#this tempalte for list of dynamixc messages 
"""from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
#Use tuples (or message prompt templates), not SystemMessage objects:
#when we craete system not system message cause it is dynamic prompt we have to replace in altter the palceholder so tahts why
chat_template=ChatPromptTemplate.from_messages(
    [
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple words what is {topic}")

    ]
)
#fill the palce holder
prompt=chat_template.invoke({'domain':'cricket','topic':'bat ball'})
print(prompt)"""
#prompttemplate he use static prompt jis m only soem palecholder for string ,but chtaprompottemplate use two things statcu is sytem human ,dynamic poart is emssage placeholderw hcuh use to load teh cahts not only strng
#message place holder ek if coustemr tak to chatbox a second day he asked soemthing so we laod past info  so based on taht info chabox rep 
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#chat template
chat_template=ChatPromptTemplate([
  ("system","You are helpful coustmer support agent"),
  #suppose human ask where is my refund jo ai ko sumj nhi aaega to hum bech m message placeholder banae ge
  #this load old data ,wese we store in cloude but yha we store in text so human jab new mess kare ga old history load
  MessagesPlaceholder(variable_name='chat_history'),
  #this is human new message
  ("human","{query}")


])
#we make list of chat_histor and we append aghy ki be histiry
#khalii list anao
chat_history=[]
#load chat history
with open('chat_history.txt')as f:
    #us ko open kr ke ek ek line ko string convert kr ke list me dalo by entend ,us ko old caht ko list m dalta hn 
    chat_history.extend(f.readlines())
#print(chat_history)
#craete prompt
#es se ye huga wo list uper ja ke load hugei 
prompt=chat_template.invoke({'chat_history':chat_history,'query':'what is my refund'})
print(prompt)