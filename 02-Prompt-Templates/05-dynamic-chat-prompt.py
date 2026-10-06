from pathlib import Path  # Imports Path to locate the .env file containing the API key.
from dotenv import load_dotenv  # Loads environment variables such as the Gemini API key.
from langchain_google_genai import ChatGoogleGenerativeAI  # Imports the Gemini chat model.
from langchain_core.prompts import ChatPromptTemplate  # Imports ChatPromptTemplate for reusable chat prompts.


env_path = Path(__file__).parent.parent / ".env"  # Locates the .env file in the main langchain-learning folder.
load_dotenv(env_path)  # Loads the API key from the .env file.


prompt = ChatPromptTemplate.from_messages([  # Creates a reusable prompt containing system and human messages.
    ("system", "You are a helpful AI tutor. Explain concepts clearly and simply."),  # Sets the AI's role and behaviour.
    ("human", "Explain {topic} to a {level} student.")  # Uses variables so the request can change dynamically.
])


model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)


topic = input("Enter a topic: ")  # Takes the topic from the user instead of hard-coding it.
level = input("Enter your learning level: ")  # Takes the learning level from the user.


formatted_prompt = prompt.invoke({  # Inserts the user's values into the prompt template.
    "topic": topic,
    "level": level
})


response = model.invoke(formatted_prompt)  # Sends the completed chat prompt to Gemini.

print(response.text)  # Displays the readable AI response.