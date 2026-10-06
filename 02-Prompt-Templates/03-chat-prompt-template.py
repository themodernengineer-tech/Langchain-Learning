from langchain_core.prompts import ChatPromptTemplate  # Imports ChatPromptTemplate, which is used to build reusable prompts for chat-based models.

prompt = ChatPromptTemplate.from_messages([  # Creates a chat prompt made up of multiple messages instead of one plain text prompt.
    ("system", "You are a helpful AI tutor. Explain concepts clearly and simply."),  # System message sets the role, behaviour, and instructions for the AI.
    ("human", "Explain {topic} to me.")  # Human message represents the user's request. {topic} acts as a placeholder for different topics.
])

result = prompt.invoke({  # Formats the chat prompt by providing values for its variables.
    "topic": "Vector Databases"  # Replaces the {topic} placeholder with "Vector Databases".
})

print(result)  # Displays the completed system and human messages. No request is being sent to Gemini yet.