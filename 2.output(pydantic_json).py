"""from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class student(BaseModel):
    #name:str
    #this set by default 
    name:str='rafia'
    age:Optional[int]=None
    #if hum koiage ki value nhi dege to wo none aae ga aghr set krni hn to dict m andr value dege
    age:Optional[int]=None
    email:EmailStr
    #this field func basically tell that range
    cgp:float=Field(gt=0,lt=10,default=8,description="this your cgp")
#int wala hn na aghr to aghr me string be dugi to be wo accept kare ga, es ko string converstion bolty hn 
new_student={'age':'45','name':'shaikh','email':'rafia@gmail.com'}#email ko aghr sai nhi dale ge to error  aaaega
#dict 
#new_student={'name':1rafia}
#obj pydantic
student2=student(**new_student)
print(student2)
#convert into dict
student_dict=student2.model_dump()
print(student_dict)
#json convert
student_json=student2.model_dump_json()
print(student_json)"""

#pydantic 
from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import Field,BaseModel
#literal se hum option choose kr sakhty hn like pos ,neg
#annotated se ai ko pta chly ga zeyda sai se person kyacahrha hn
model=ChatOllama(model="llama3.2:1b")
class review(BaseModel):
    #list of strings strings ki list bane gei
    #ey_themes ke case mein AI review ko read karega, important/key themes identify karega, aur un themes ko separate strings ki form mein ek list ke andar return karega.
    key_themes:list[str]=Field(description="List all important themes discussed in the review ")
   
    summary:str=Field(description="this is summary pof whole review")
    sentiment:Literal['pos','neg','neutral']=Field(description="return sentiment of review either positive,negative,neutral")
   # sentiment:Annotated[str,"return sentiment of review either positive,negative,or neutral"]
    pros:Optional[list[str]]=Field(default=None,description="write down all the pros in the list formate ")
    cons:Optional[list[str]]=Field(default=None,description="write down all the cons in the list formate ")
    name:Optional[str]=Field(default=None,description="Extract ONLY the human reviewer's name. Do NOT return any product, brand, company, model, or phone name. If no person's name is explicitly mentioned, return None."
)
    
#model ka jo ans hn wo struture output mein wrap hugya revuew bta rha hn bhai sah ans ese huna cahahye abi tak ans aya nhi hn ye ek varaibl m store hn hn wo variable neeche .invoke hugya us k andr prompt hn ab prompt invoke huwa stctutre me us k andr real model ollama ka hn
structure_model=model.with_structured_output(review)
result=structure_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse. The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away was the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:

Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera (incredible zoom capabilities)
Long battery life with fast charging
S-Pen support is unique and useful

Cons:

Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors  review by rafia""")
print(result)
print(result.name)
#TypedDict = structure batata hai.
#BaseModel = structure + Pydantic validation/parsing

#json schema jo worldwide huta hn can be use in any language
"""{
  "title": "student",
  "description": "schema about student",

  "type": "object",

  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    }
  },

  "required": ["name"]
}"""
#json schema is blueprint ke output esa huna chhaye bhly hum python me kare ya kesi language me and values badh m kudh replace hugei prompt se
from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import Field,BaseModel
#literal se hum option choose kr sakhty hn like pos ,neg
#annotated se ai ko pta chly ga zeyda sai se person kyacahrha hn
model=ChatOllama(model="llama3.2:1b")
#json schema
output_json ={
  "title": "review",
  "description": "Schema about a product review",

  "type": "object",

  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List all important themes discussed in the review"
    },

    "summary": {
      "type": "string",
      "description": "This is summary of whole review"
    },

    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg", "neutral"],
      "description": "Return sentiment of review either positive, negative, neutral"
    },

    "pros": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros in list format"
    },

    "cons": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons in list format"
    },

    "name": {
      "type": "string",
      "description": "Extract ONLY the human reviewer's name. Do NOT return any product, brand, company, model, or phone name. If no person's name is explicitly mentioned, return None."
    }
  },

  "required": [
    "key_themes",
    "summary",
    "sentiment"
  ]
}

#model ka jo ans hn wo struture output mein wrap hugya revuew bta rha hn bhai sah ans ese huna cahahye abi tak ans aya nhi hn ye ek varaibl m store hn hn wo variable neeche .invoke hugya us k andr prompt hn ab prompt invoke huwa stctutre me us k andr real model ollama ka hn
structure_model=model.with_structured_output(output_json)
result=structure_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse. The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away was the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:

Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera (incredible zoom capabilities)
Long battery life with fast charging
S-Pen support is unique and useful

Cons:

Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors  review by rafia""")
print(result)#result come in dict
#output me tittle and uper ek cheez nhi ae gei from properties se aae ga cause this is impo field uper wlai is meta data


