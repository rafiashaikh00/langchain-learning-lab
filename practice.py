from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load the model
model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

# Create the prompt template
chat_template = ChatPromptTemplate([
    ("system",
    "You are a helpful AI assistant. Always use the previous chat history to answer the user's questions. If the user asks about something mentioned earlier in the conversation, answer using the chat history."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Load old chat history
chat_history = []

try:
    with open("chat_history.txt", "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("Human:"):
                chat_history.append(
                    HumanMessage(
                        content=line.replace("Human:", "").strip()
                    )
                )

            elif line.startswith("AI:"):
                chat_history.append(
                    AIMessage(
                        content=line.replace("AI:", "").strip()
                    )
                )

except FileNotFoundError:
    # First time running the chatbot
    pass

# Get user input
query = input("You: ")

# Create the prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": query
})

# Generate response
result = model.invoke(prompt)

print("AI:", result.content)

# Store today's conversation
chat_history.append(HumanMessage(content=query))
chat_history.append(AIMessage(content=result.content))

# Save updated history
with open("chat_history.txt", "w") as f:

    for message in chat_history:

        if isinstance(message, HumanMessage):
            f.write(f"Human: {message.content}\n")

        elif isinstance(message, AIMessage):
            f.write(f"AI: {message.content}\n")