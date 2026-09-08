from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


# MODEL
model = ChatOllama(model='gemma3:1b')


# NORMAL STRING PARSER
parser = StrOutputParser()


# PYDANTIC MODEL
class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description='Give the sentiment of the feedback'
    )


# PYDANTIC OUTPUT PARSER
parser2 = PydanticOutputParser(
    pydantic_object=feedback
)


# CLASSIFIER PROMPT
prompt1 = PromptTemplate(
    template='''
classify the sentiment of the following feedback text into positive or negative

{feedback}

{formate_instruction}
''',

    input_variables=['feedback'],

    partial_variables={
        'formate_instruction': parser2.get_format_instructions()
    }
)


# CLASSIFIER CHAIN
classifier_chain = prompt1 | model | parser2
# output Feedback(sentiment='negative')


# POSITIVE PROMPT
prompt2 = PromptTemplate(
    template='''
Write an appropriate response to the positive feedback:

{feedback}
''',

    input_variables=['feedback']
)


# NEGATIVE PROMPT
prompt3 = PromptTemplate(
    template='''
Write an appropriate response to the negative feedback:

{feedback}
''',

    input_variables=['feedback']
)


# ------------------------------------------------
# PRESERVE ORIGINAL FEEDBACK + CLASSIFIER OUTPUT
# ------------------------------------------------
#ecause your classifier doesn't return the original feedback.it return positive negative 
def prepare_branch_input(x):
 # x is basically parameter invoke se real prompt jo hn teriabkle wala chain m jae ga 
    classification = classifier_chain.invoke(x)
    # ye es ka output hnFeedback(sentiment="negative")
 #This creates a new dictionary. x is result feedback ke andr jo hn teribakle wali cheez
    return {
        'feedback': x['feedback'],
        #Because it's a Pydantic object, we can access its field:
        'sentiment': classification.sentiment
    }


prepare_input = RunnableLambda(prepare_branch_input)


# ------------------------------------------------
# BRANCH
# ------------------------------------------------

branch_chain = RunnableBranch(

    (
        lambda x: x['sentiment'] == 'positive',
        prompt2 | model | parser
    ),

    (
        lambda x: x['sentiment'] == 'negative',
        prompt3 | model | parser
    ),

    RunnableLambda(
        lambda x: 'could not find sentiment'
    )
)


# FINAL CHAIN
chain = prepare_input | branch_chain


# INVOKE
# x is = resukt x={'feedback':'this is teriable pohone}
result = chain.invoke({
    'feedback': 'This is a terrible phone'
})


print(result)