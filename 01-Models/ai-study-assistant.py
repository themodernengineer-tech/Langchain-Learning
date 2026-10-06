# 1. Import Path so we can locate our .env file
from pathlib import Path


# 2. Import load_dotenv so Python can load our API key
from dotenv import load_dotenv


# 3. Import LangChain's Google Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI


# 4. Find the .env file
env_path = Path(__file__).parent.parent / ".env"


# 5. Load the environment variables from .env
load_dotenv(env_path)


# 6. Create our LangChain chat model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)


# 7. Ask the user to enter a question
while True:

    # Ask the user for a question
    question = input("\nYou: ")

    # Stop the program if the user types exit
    if question.lower() == "exit":
        print("AI: Goodbye!")
        break

    # Send the question to the model
    response = model.invoke(question)

# Print the answer
    print("\nAI:")
    print(response.text)




