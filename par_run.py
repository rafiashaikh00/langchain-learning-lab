from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

model=ChatOllama(model='gemma3:1b')
prompt1=PromptTemplate(
template='Generate a twetter post about this topic {topic}',
input_variables=['topic']
)
parser=StrOutputParser()
prompt2=PromptTemplate(
template='Generate a linkedln post about this topic {topic}',
input_variables=['topic']
)
#runnable parallel se kya huga two kam sath m huge linkeldn and tweeter
parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1|model|parser),
    'linkedln':RunnableSequence(prompt2|model|parser)
})
result=parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
