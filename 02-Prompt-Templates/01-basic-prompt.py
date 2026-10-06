from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} to a beginner in simple terms."
)

result = prompt.invoke({
    "topic": "Docker"
})

print(result)