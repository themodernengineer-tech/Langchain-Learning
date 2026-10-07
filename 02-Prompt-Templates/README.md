# Topic 02 — Prompt Templates

## Overview

This topic covers how LangChain Prompt Templates can be used to create reusable and dynamic prompts instead of hard-coding instructions.

## What I Learned

### PromptTemplate

`PromptTemplate` creates reusable text prompts using variables.

```python
prompt = PromptTemplate.from_template(
    "Explain {topic} to a {level} student."
)
```

Variables such as `{topic}` and `{level}` can be changed without rewriting the prompt.

### ChatPromptTemplate

`ChatPromptTemplate` structures prompts using chat messages.

- **System message** — defines the AI's role and behaviour.
- **Human message** — contains the user's request.

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI tutor."),
    ("human", "Explain {topic} to me.")
])
```

### Dynamic User Input

Python `input()` can be used to collect values from the user and pass them into prompt variables.

### Prompt vs Model Invocation

```python
prompt.invoke()
```

Formats the prompt.

```python
model.invoke()
```

Sends the formatted prompt to the language model.

### Few-Shot Prompting

Few-shot prompting provides examples to guide the model toward the expected response style.

I also learned about **example selection**, where relevant examples can be selected dynamically. Semantic example selection will be explored later with embeddings and vector databases.

## Application Flow

```text
User Input
    ↓
Prompt Variables
    ↓
PromptTemplate / ChatPromptTemplate
    ↓
prompt.invoke()
    ↓
model.invoke()
    ↓
Gemini
    ↓
AI Response
```

## Files

```text
01-basic-prompt.py
02-multiple-variables.py
03-chat-prompt-template.py
04-prompt-with-model.py
05-dynamic-chat-prompt.py
06-few-shot-prompt.py
07-few-shot-with-model.py

Meeting-Preparation-Assistant/
├── README.md
└── meeting-preparation-assistant.py
```

## Troubleshooting

While testing Gemini, I encountered a `503 UNAVAILABLE` error caused by temporary high model demand. Retrying the request was sufficient.

I also encountered an Automatic Function Calling (AFC) warning from the Gemini integration. It did not prevent the application from generating responses.

## Mini Project

### AI Meeting Preparation Assistant

I applied the concepts from this topic to build an interactive Meeting Preparation Assistant using:

- `ChatPromptTemplate`
- Multiple prompt variables
- Dynamic user input
- System and human messages
- Google Gemini

The project has its own README with the implementation and test scenario.

## Key Takeaways

- Prompt Templates make prompts reusable.
- Variables make prompts dynamic.
- `ChatPromptTemplate` structures chat messages.
- `prompt.invoke()` formats the prompt.
- `model.invoke()` calls the language model.
- Few-shot prompting uses examples to guide model behaviour.

## Next Topic

**Topic 03 — Chains and LCEL**

Next, these separate components will be combined into pipelines such as:

```python
chain = prompt | model
```
