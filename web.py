from langchain_community.document_loaders import WebBaseLoader

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
model=ChatOllama(model='gemma3:1b')
prompt=PromptTemplate(template='Answer the following query {query} the text i pasted {text}', input_variables=['query','text'])
parser=StrOutputParser()
#this work good where pages are mostly with html based 
url='https://letmeinspireyou.nl/?gad_source=1&gad_campaignid=24099880294&gbraid=0AAAABCyOT6LdHIz8eyfKqy7xB7xH1We1u&gclid=Cj0KCQjwnbrUBhDOARIsAKKhPpddIhx_92fmdvA7SSv6VxRn4CFYEFDXt-w9lTIMpNI6ab05zkQOmY0aArZSEALw_wcB'
loader=WebBaseLoader(url)
docs=loader.load()
"""print(len(docs))
print(docs[0].page_content)"""
#WebBaseLoader basically webpage ka HTML source fetch → BeautifulSoup se parse → text extract karta hai.
#k URL ke liye normally docs mein ek Document object aata hai.
chain=prompt|model|parser
result=chain.invoke({'query':'nutshell summary of this blog what is author want to show','text':docs[0].page_content})
print(result)

#there is a loader for csv files which make object for every row you can get one row by docs[0] just import csv loader same code way can ask ques like max slaary etc ealted to file
