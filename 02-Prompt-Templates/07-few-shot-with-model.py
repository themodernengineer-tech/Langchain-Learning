from pathlib import Path  # Imports Path to locate the .env file containing the API key.
from dotenv import load_dotenv  # Loads environment variables from the .env file.
from langchain_google_genai import ChatGoogleGenerativeAI  # Imports the Gemini chat model.
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate  # Imports the prompt classes needed for few-shot prompting.


env_path = Path(__file__).parent.parent / ".env"  # Locates the .env file in the main project folder.
load_dotenv(env_path)  # Loads the Gemini API key into the environment.


examples = [  # Provides examples that demonstrate the type and style of answer expected.
    {
        "term": "API",
        "explanation": "A way for two software programs to communicate."
    },
    {
        "term": "Database",
        "explanation": "A structured place for storing and organizing information."
    }
]


example_prompt = PromptTemplate.from_template(  # Defines how each example will appear inside the final prompt.
    "Term: {term}\nExplanation: {explanation}"
)


prompt = FewShotPromptTemplate(  # Combines instructions, examples, and the new input into one reusable prompt.
    examples=examples,
    example_prompt=example_prompt,
    prefix="Explain technical terms in simple language.",
    suffix="Term: {term}\nExplanation:",
    input_variables=["term"]
)


formatted_prompt = prompt.invoke({  # Builds the final prompt and inserts the new term.
    "term": "Embeddings"
})


model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)


response = model.invoke(formatted_prompt.text)  # Sends the completed few-shot prompt to Gemini.

print(response.text)  # Displays Gemini's generated explanation.