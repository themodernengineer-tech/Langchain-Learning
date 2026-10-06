from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Find the .env file
env_path = Path(__file__).parent.parent / ".env"

# Load API keys from .env
load_dotenv(env_path)


# Create our LangChain model
model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash"
)


# Send a question to the model
response = model.invoke("What is LangChain? Explain in simple terms.")


# Print the answer
print(response.text)


