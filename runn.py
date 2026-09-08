"""from abc import ABC,abstractmethod
#making abstract class cause it inherit from ABC
class runnable(ABC):
    #we make an method of invoke
    @abstractmethod
    def invoke(input_data):
        pass #thsi method no work so we use pass abd do label
#this works as demi llm
import random
#this class inherit runnable class , so this nikli llm also now is runnable,we must implemnt abstract method too

class niklillm(runnable):

    def __init__(self):
        print("LLM Created")
    #making same methiod
    def invoke(self,prompt):
     response_list=[
        'pakistan is good country',
        'im learning ai',
        'im bored too much in my life'

        ]
     return{'response':random.choice(response_list)}
  
#obj
llm=niklillm()


#this works as demi prompt
#yha be implemnt kare ge runnable so ye be runnable hujae also implemnt invoke
class demipromptTemplate(runnable):
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
    def invoke(self,input_dict):
        #dict ko unpack kr rhy hn
        #template object ke andar jo format() method hai, usko call karo.
        return self.template.format(**input_dict)
   
template=demipromptTemplate(
    template='write a poem about this topic \n {topic}',
    input_variables=['topic']
)
class nikliparser(runnable):
    def __init__(self):
        pass
    def invoke(self,input_data):
        return input_data['response']
parser=nikliparser()
#chain form
#we convert above class in runnable they must have common methods runnable is used to make cahins
class runnableconnector(runnable):
    def __init__(self,runnable_list):
        self.runnable_list=runnable_list
    def invoke(self,input_data):
        #loop chlae ge
    for runnable in self.runnable_list:
     input_data=   runnable.invoke(input_data)
    return input_data
chain=runnableconnector([template,llm,parser])
a=chain.invoke({'topic':'what is india?'})
print(a)"""
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

model=ChatOllama(model='gemma3:1b')
prompt=PromptTemplate(
template='write a poetry about this topic \n {topic} in 5 lines',
input_variables=['topic']
)
parser=StrOutputParser()
prompt1=PromptTemplate(
template='explain the above mention topic what it want to saying ,its message {text}',
input_variables=['text']
)
#make chains prompt send input to model model sent his output as input to parser
#lcel is chain=(prompt|model|parser so on we use pipe no word wri)
chain=RunnableSequence(prompt,model,parser,prompt1,model,parser)
result=chain.invoke({'topic':'AI'})
print(result)

