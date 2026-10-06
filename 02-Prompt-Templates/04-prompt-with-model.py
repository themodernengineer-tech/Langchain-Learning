from pathlib import Path  # Imports Path to locate the .env file containing the API key.
from dotenv import load_dotenv  # Imports load_dotenv to load environment variables from the .env file.
from langchain_google_genai import ChatGoogleGenerativeAI  # Imports the Gemini chat model integration.
from langchain_core.prompts import ChatPromptTemplate  # Imports ChatPromptTemplate to create structured chat prompts.


env_path = Path(__file__).parent.parent / ".env"  # Finds the .env file located in the main langchain-learning folder.
load_dotenv(env_path)  # Loads the API key from .env into the environment.


prompt = ChatPromptTemplate.from_messages([  # Creates a reusable chat prompt containing system and human messages.
    ("system", "You are a helpful AI tutor. Explain concepts clearly and simply."),  # Sets the model's role and behaviour.
    ("human", "Explain {topic} to a {level} student.")  # Defines the user's request with two reusable variables.
])


model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"  # Creates the Gemini chat model used in the previous topic.
)


formatted_prompt = prompt.invoke({  # Fills the variables and creates the final structured chat messages.
    "topic": "RAG",  # Replaces {topic} with RAG.
    "level": "beginner"  # Replaces {level} with beginner.
})


response = model.invoke(formatted_prompt)  # Sends the formatted chat messages to Gemini and receives an AIMessage response.

print(response.text)  # Prints only the readable text from Gemini's response.