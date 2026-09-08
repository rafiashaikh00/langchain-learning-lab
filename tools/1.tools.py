#DDG is duckduckosdearach enginer is just liek google serach engienr we use this so it python serach the text in duckducgp
"""from langchain_community.tools import DuckDuckGoSearchRun
#es class ka ek obj bane ge
search_tool=DuckDuckGoSearchRun()
#these tools are also runnables so ue invike func
result=search_tool.invoke("i heard google office is going to open in pkaistan?")
print(result)"""
"""DuckDuckGoSearchRun ek LangChain Tool hai jo DuckDuckGo ke through web par search karta hai aur search results return karta hai."""
#shell tool commnad line me commnad run huga
"""from langchain_community.tools import ShellTool
serach_tool=ShellTool()
result=serach_tool.invoke('whoami')
print(result)"""
#explantion of tools
"""A tool acts like a function that we give to an LLM or an agent, giving it the ability to perform actions or retrieve information from external sources.

For example:

Calculator tool → perform calculations
Search tool → get information from the web
Shell tool → execute commands/code
Database tool → retrieve data from a database

One small point: the LLM doesn't execute the function by itself. With tool calling, the LLM decides which tool to call and what arguments to give it, and the tool actually performs the operation."""

#coustom tools
from langchain_core.tools import tool
#step1 func create krna
#create a function

def mul(a,b):
    #It's a docstring, not a comment. ✅,And in your LangChain Tool example, the docstring is especially useful because LangChain can use it as the tool's description for the LLM.
    """Multiply the two numbers"""
    return a*b

#STEP 2 yah type hinting krna
def mul(a:int ,b:int)-> int:
    """multiply two numbers return result also in number """
    return a*b

#STEP 3 ADD TOOL DECORATOR 
@tool
def mul(a:int ,b:int)-> int:
    """multiply two numbers return result also in number """
    return a*b
# first you write function logic -> then type hinting ,-> then mention @tool 
result=mul.invoke({'a':2,'b':8})
print(result)
print(mul.name)#print mul func name
print(mul.args)#argumnet ka datat type be
print(mul.description)#descption be
