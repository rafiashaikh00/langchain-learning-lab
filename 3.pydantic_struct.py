#this is pydantic parser of structure output this provide json formate also validation and es em scehma be aagei
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import Field,BaseModel

model=ChatOllama(model="llama3.2:1b")
class person(BaseModel):
    name:str=Field(description='Name of the person')
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description="where the person belongs to")
    salary:float=Field(description='persons salary')
parser=PydanticOutputParser(pydantic_object=person)
template=PromptTemplate(
 template='write the name,age,city,saalry of one fictional {place} of  a real person \n {format_instruction}',
 input_variables=['place'],
 partial_variables={'format_instruction':parser.get_format_instructions()}

)
prompt=template.invoke({'place':'Pakistan'})
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)