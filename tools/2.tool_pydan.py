from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
class MultiplyInput(BaseModel):
    # First number jo tool ko diya jayega
    a: int = Field(
        required=True,
        description="The first number to multiply"
    )

    # Second number jo tool ko diya jayega
    b: int = Field(
        required=True,
        description="The second number to multiply"
    )

def multiply_func(a: int, b: int) -> int:
    # Ye actual operation perform karega
    return a * b
# STEP 3: Convert the function into a LangChain Tool
multiply_tool = StructuredTool.from_function(
    # Jo Python function tool ke through execute hogi
    func=multiply_func,
    # Tool ka naam jo ek label behave kare ag llm sumj sgahy it can be multiply_func or multipl or domultiple naything
    name="multiply",
    # LLM ko batayega ke ye tool kya karta hai
    description="Multiply two numbers",
    # Tool ko kis type ka input chahiye
    args_schema=MultiplyInput
)
# Tool ko dictionary ke form mein inputs de rahe hain
result = multiply_tool.invoke({
    "a": 3,
    "b": 3
})
# Tool ka result
print(result)
# Tool ka naam
print(multiply_tool.name)
# Tool ki description
print(multiply_tool.description)










from pydantic import BaseModel, Field
from typing import Type
from langchain.tools import BaseTool

# arg schema using pydantic

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")


class MultiplyTool(BaseTool):#ye class basetool ko inhrit krta hn sare tools es sebanty hn
    name: str = "multiply"#tool ka nmae
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput#uper defien kiye hn wo yah ae ge

    def _run(self, a: int, b: int) -> int:#func uinside thsi class
        return a * b


multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a': 3, 'b': 3})

print(result)
print(multiply_tool.name)
#tookit multiply tools ko ek kit k store karo
from langchain_core.tools import tool


# --------------------------------------------------
# STEP 1: Tools bana rahe hain @tool decorator se
# --------------------------------------------------

@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# --------------------------------------------------
# STEP 2: Toolkit — dono tools ko ek list mein group kiya
# --------------------------------------------------

class MathToolkit:
    def get_tools(self):
        return [add, multiply]


# --------------------------------------------------
# STEP 3: Test karna
# --------------------------------------------------

toolkit = MathToolkit()
tools = toolkit.get_tools()


for t in tools:
    print(t.name, "->", t.description)

# Individual tool call karna
add_result = add.invoke({"a": 5, "b": 3})
multiply_result = multiply.invoke({"a": 5, "b": 3})

print("Add result:", add_result)
print("Multiply result:", multiply_result)