"""import langchain
print(langchain.__version__)"""
from langchian_openai import OpenAI
#this is way to import this librarary so our key taht present in env that laod here
from dotenv import load_dotenv
#loadopenapikey
dotenv()
#we make openai obj and write which model we will work
llm=OpenAI(model="gpt-3.5-turbo-instruct")
#we talk this model by invoke,invoke send this ( bracket ques to model model give response that store in variable we call ed here result)
result=llm.invoke("what is capital of india")
print(result)
#This uses the LLM interface. It sends a single text prompt and gets back plain text.