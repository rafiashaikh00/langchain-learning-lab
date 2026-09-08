from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

model=ChatOllama(model='gemma3:1b')


prompt1=PromptTemplate(
template='write a joke about this topic \n {topic} ',
input_variables=['topic']
)
parser=StrOutputParser()
prompt2=PromptTemplate(
template='explain the above mention topic what it want to saying ,its message {text}',
input_variables=['text']
)
#joke bana
joke_gen_chain=RunnableSequence(prompt1|model|parser)
#parralel me joke print hu and explanation too use pass through so  as it is joke print hu
parallel_chain=RunnableParallel({
'joke':RunnablePassthrough(), #es se joke as it is print huga,
'Explanation':RunnableSequence(prompt2|model|parser)
})
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'Ai'})
print(result)

