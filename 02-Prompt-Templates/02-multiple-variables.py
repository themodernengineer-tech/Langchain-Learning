# I imported PromptTemplate from LangChain so I can create
# reusable prompts instead of writing a new prompt every time.
from langchain_core.prompts import PromptTemplate


# I created a prompt template with three input variables:
# {topic} = the topic I want to explain
# {level} = the learner's knowledge level
# {style} = the style I want the explanation in
prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} student using {style}."
)


# I used invoke() to provide values for the variables
# inside my prompt template.
#
# The dictionary keys match the variables in the template:
# "topic" matches {topic}
# "level" matches {level}
# "style" matches {style}
result = prompt.invoke({
    "topic": "Embeddings",
    "level": "beginner",
    "style": "a real-world analogy"
})


# I printed the final formatted prompt.
# At this stage, I am NOT sending the prompt to Gemini.
# I am only using LangChain to construct the prompt.
print(result)