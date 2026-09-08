#simple chains
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model=ChatOllama(model='llama3.2:1b')
parser=StrOutputParser()
template=PromptTemplate(
 template='define 5 facts , keypoints about this {topic}',
 input_variables=['topic']
 )
# this (|) called pipe operation called lcel this is pipe operation
#This is LCEL (LangChain Expression Language) using the pipe | operator.
#One small correction: the parser doesn't "form" the answer. The model generates the answer; the StrOutputParser simply converts/extracts the model's response into a string.
#And yes, this is the main idea of chains with LCEL:
chain=template|model|parser
result=chain.invoke({'topic':'Black Hole'})
# phly topic invoke huga template me to pora prompt banjaega then it go to model then it go to parser wo form kare ga string for
print(result)

chain.get_graph().print_ascii()
#visulization happedn