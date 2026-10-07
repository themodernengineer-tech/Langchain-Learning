# AI Meeting Preparation Assistant

## Project Overview

The AI Meeting Preparation Assistant is a command-line application built using LangChain `ChatPromptTemplate` and Google Gemini.

The purpose of this project is to help a user prepare for an upcoming meeting by collecting important information about the meeting and generating a structured preparation brief.

This project applies the Prompt Template concepts learned in Topic 02 to a practical use case.

---

## Problem

Preparing for an important meeting requires understanding:

- What needs to be achieved
- What topics should be discussed
- What questions should be asked
- What potential problems should be considered
- How the conversation should be approached

Instead of manually creating a preparation plan for every meeting, this application collects information from the user and uses an LLM to generate a customized meeting preparation brief.

---

## How It Works

The application asks the user for five pieces of information:

1. Meeting type
2. Person or audience attending the meeting
3. Main objective
4. Important context
5. Main concerns

These values are inserted into a reusable LangChain `ChatPromptTemplate`.

The completed prompt is then sent to the Gemini model, which generates a meeting preparation brief.

---

## Application Flow

User Input  
↓  
Prompt Variables  
↓  
ChatPromptTemplate  
↓  
System + Human Messages  
↓  
Gemini Model  
↓  
Meeting Preparation Brief

---

## Prompt Variables

The project uses five dynamic prompt variables:

- `{meeting_type}`
- `{audience}`
- `{objective}`
- `{context}`
- `{concerns}`

Because these values are dynamic, the same prompt can be reused for many different meeting situations.

---

## Example Test

I tested the application using a software development project scenario.

### Input

**Meeting Type:**  
Office Project

**Meeting With:**  
Senior Developer

**Main Objective:**  
Discuss errors encountered while running a program.

**Important Context:**  
There is uncertainty about whether the application will be ready for deployment.

**Main Concern:**  
The team may be unable to meet the client's deadline.

### Terminal Example

```text
Meeting type: Office Project
Who are you meeting with? Senior Developer
What is your main objective? Discussing some errors while running a program
Provide the important context: Doubt if we would be able to deploy the app
What are your main concerns? Unable to reach client deadline

--- MEETING PREPARATION BRIEF ---
