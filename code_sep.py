#we split python code use separate spilttors ,
#"\n class" for class keyword,"\ndef" for func,"\n\tdef" these are especial and after that we use same previous spilttors 
#"Pehle largest meaningful boundary try karo; agar chunk abhi bhi bada hai, next smaller boundary par jao; phir next; aur end mein character level tak jao."
#"\n classclass, inside \ndef" func,insdemethods \n\tdef"indetication ,/nline ,' 'word ,''char
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
code = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

    def study(self, subject):
        print(f"{self.name} is studying {subject}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}")


def calculate_sum(a, b):
    result = a + b
    return result


def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
"""
#spillter obj,call method language
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=0


)
#split_text() chunks ki list return karta hai, aur tum us list ko result variable mein store kar rahi ho.
result=splitter.split_text(code)
print(result[0])
#jese document loader k trha object store in list same  spilt text store chunks in list 