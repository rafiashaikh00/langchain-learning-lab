"""from typing import TypedDict
#make one class jha ye sabh present huga
class person(TypedDict):
    name:str
    age:int
#new dict
new_person:person={'name':'rafia','int':23}
print(new_person)"""
#in typedict llm can mak mistake so data validation you have to perform pydnatic
from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Optional,Literal
#literal se hum option choose kr sakhty hn like pos ,neg
#annotated se ai ko pta chly ga zeyda sai se person kyacahrha hn
model=ChatOllama(model='llama3.2:1b')
class review(TypedDict):
    #list of strings strings ki list bane gei
    #ey_themes ke case mein AI review ko read karega, important/key themes identify karega, aur un themes ko separate strings ki form mein ek list ke andar return karega.
    key_themes:Annotated[list[str],"List all important themes discussed in the review "]
    summary:Annotated[str,"this is summary pof whole review"]
   # sentiment:Annotated[str,"return sentiment of review either positive,negative,or neutral"]
    sentiment:Annotated[Literal['pos','neg','neutral'],"return sentiment of review either positive,negative,neutral"]
    pros:Annotated[Optional[list[str]],"write down all the pros in the list formate "]
    cons:Annotated[Optional[list[str]],"write down all the cons in the list formate "]
    name:Annotated[Optional[str],"Extract ONLY the human reviewer's name. Do NOT return any product, brand, company, model, or phone name. If no person's name is explicitly mentioned, return None."
]
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
print(result['sentiment'])
print(result['name'])


