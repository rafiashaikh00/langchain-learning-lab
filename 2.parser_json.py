from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
model = ChatOllama(
    model="llama3.2:1b"

 )
#JsonOutputParser mainly cares that the output is valid JSON, not necessarily that the JSON has exactly the fields you wanted.
# you are the parser which is gen json output
parser=JsonOutputParser()
#format_instruction ys basiccaly name is return object in json frmate
template=PromptTemplate(
 template="Generate a completely made-up, imaginary fictional character (not a real person). "
          "Give me their name, age and phone_number. "
          "This is for a fictional story, not a real individual.\n {format_instruction}",
 input_variables=[],
 #Whatever formatting instructions the parser gives me, automatically put them into {format_instruction}.
 partial_variables={'format_instruction':parser.get_format_instructions()}
 #you are the json parser gen such instrction whih=cih i gie to llm and it gen outputy which you are able to parse so as json parser gen instrction like  resul in json formate

)
#"Template, fill the {format_instruction} placeholder with the value I already gave you."

#So now prompt becomes a complete prompt.,Give me the name, age and phone_number of any fictional person.

#[JSON formatting instructions]
"""prompt=template.format()#neche wali instruiom ko uper templatye me dalo 
result=model.invoke(prompt)
#yha par parse huga output ai mess be huta hn result. mei so we do result.content tak k ai mess chla jae and hum sai mess ko json me kare
#Here is the LLM's response. Parse it as JSON.
final_result=parser.parse(result.content)
print(final_result)"""
#chains  after template ye huga es me kudh hei prompt bane ga everthing
chain=template|model|parser
#es ke nadr blank dict ko dale ge
result=chain.invoke({})
print(result)

