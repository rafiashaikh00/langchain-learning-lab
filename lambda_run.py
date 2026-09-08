"""#convert python function to runnable
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnableSequence,RunnablePassthrough
#through this yiu can excute parallel chains
model1=ChatOllama(model='gemma3:1b')
#func ctreate for lambda
def word_count(text):
    return len(text.split())
prompt1=PromptTemplate(
    template='tell me joke about this topic \n {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
#joke bana
joke_gen_chain=RunnableSequence(prompt1,model1,parser)
#joke bana wo print plaus me len of words print too
parallel_chain=RunnableParallel(
    {
     'joke':RunnablePassthrough(),
     'word_counter':RunnableLambda(word_count)



    }
)
#dono chains ko milae ge tak ke ek chain ka output dhusre k pas jae ga as input
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'Ai'})
print(result)"""


#RunnableBranch
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnableSequence,RunnablePassthrough,RunnableBranch
#through this yiu can excute parallel chains
model1=ChatOllama(model='gemma3:1b')
prompt1=PromptTemplate(
    template='Write a detail report  and excellent observation about this topic {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
template='kindly summarize this about text i will be thankfull summerziation should be meaningfull {text}',
input_variables=['text']
)
parser=StrOutputParser()
report_chain=RunnableSequence(prompt1,model1,parser)
branch_chain=RunnableBranch(
    #tuple bhjty hn tuple is like if condition if elif here one condition if more than 500 words other is less then 500 word so i will send one ()
 #tuple and default condition    
 #tuple ke inside  hum bhjy ge ek condition and runnable jo tab excute huga jab condition becime trye
 # condition wo output huga jo uper waly parser ka output hn sio we here send func on lambda
 (lambda x : len(x.split())>500,RunnableSequence(prompt2,model1,parser)),
 #x is the output of that parser above and len is func  
 #this is default condition,lambda use for condition if above condition fail come here
  #DEFAULT → condition FALSE ho to ye chalega so no lambda use here
  RunnablePassthrough()
)
final_chain=RunnableSequence(report_chain,branch_chain)
result=final_chain.invoke({'topic':'Gen AI'})
print(result)