# AI Workshop Day 1

## Project Overview

This project demonstrates the difference between a basic LLM chatbot, a rule-based workflow, and an AI agent that uses tools.

The project uses a sample college course fee dataset to demonstrate how different AI systems handle questions and calculations.

## Technologies Used

- Python
- OpenAI-compatible API
- Groq
- Python-dotenv
- Git & GitHub

## Course Fee Data

| Course | Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

## Project Components

### 1. LLM Chatbot

**File:** `chatbot.py`

A basic LLM chatbot that answers user questions without access to the private course fee data.

### 2. Rule-Based Workflow

**File:** `workflow.py`

Uses predefined Python rules to process course fee questions without using an LLM.

### 3. Tools

**File:** `tools.py`

Provides two tools:

- `get_course_fee()` - retrieves the fee for a course.
- `calculator()` - performs safe arithmetic calculations.

### 4. AI Agent

**File:** `agent.py`

Combines an LLM with tools. The agent decides when to use the available tools to obtain reliable course information and perform calculations.

### 5. Challenge

**File:** `challenge.py`

Checks which combinations of two courses can be selected within a given budget.

For a budget of Rs. 30,000:

- CS101 + AI202 = Rs. 30,000
- CS101 + DS303 = Rs. 27,000

## Screenshots

Program output screenshots are available in the `output/` folder.

## Learning Outcomes

Through this workshop, I learned:

- How to connect Python applications to an LLM.
- How rule-based workflows work.
- How tools can provide reliable external data.
- How an AI agent can use tools to solve problems.
- How to organize and upload a Python project using Git and GitHub.