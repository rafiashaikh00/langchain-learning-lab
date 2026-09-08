from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatOllama(
    model="llama3.2:1b"

 )
#1st prompt
template1=PromptTemplate(
 template="write a detail report on {topic}",
 input_variables=['topic']


)

#Prompt template is basically a blue print of template taht we jsut cahneg placeholder 
#2nd prompt
template2=PromptTemplate(

 template="write a 5 line summary on following text.\n {text}",
 input_variables=['text']

)
parser=StrOutputParser()
chain=template1|model|parser|template2|model|parser
result=chain.invoke({'topic':'blach hole'})
print(result)

#
