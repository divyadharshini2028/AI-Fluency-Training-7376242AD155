# Day 2 – Reasoning, ReAct and Self-Consistency

## Overview

Day 2 focuses on different AI reasoning techniques using the Groq API with the `openai/gpt-oss-120b` model.

The lab covers:

- ReAct tool-based reasoning
- Chain-of-Thought (CoT) comparison
- Self-Consistency
- Comparing direct answers with step-by-step reasoning
- Evaluating repeated model outputs

## Model and Provider

- Provider: Groq
- Model: `openai/gpt-oss-120b`
- Language: Python
- Environment: Python virtual environment (`.venv`)

## Part A – ReAct Paper Trace

The problem compares two fee options:

1. CS101 + AI202 with a 10% scholarship
2. CS101 + AI202 + DS303 with a 25% scholarship

Course fees:

| Course | Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

Calculations:

- First option: `(12000 + 18000) × 0.90 = Rs. 27,000`
- Second option: `(12000 + 18000 + 15000) × 0.75 = Rs. 33,750`
- Difference: `33750 - 27000 = Rs. 6,750`

Therefore, the first option is cheaper by **Rs. 6,750**.

## Part B – ReAct Agent Trace

`react_trace.py` demonstrates an agent using tools to retrieve course fees and perform calculations.

Tools used:

- `get_course_fee`
- `calculator`

The agent uses the tool results to determine the final cost difference.

## Part C – Chain-of-Thought Comparison

`cot_compare.py` compares:

- Direct answers without step-by-step reasoning
- Step-by-step Chain-of-Thought answers

Three problems are tested:

1. Course fee instalment calculation
2. Computer lab student sittings
3. Height comparison

Expected answers:

- Instalment: **Rs. 9,562.50**
- Student sittings: **90**
- Tallest: **Ravi**
- Shortest: **Priya**

The experiment shows how step-by-step reasoning can provide more detailed explanations, while direct answers are shorter.

## Part D – Self-Consistency

`self_consistency.py` runs the same reasoning problem five times with temperature `0.8`.

The five runs produced the same numerical answer:

**Rs. 9,562.50 per instalment**

The program normalizes different formats such as `9562.5`, `9,562.50`, and `Rs. 9,562.50` and identifies them as the same numerical answer.

Final result:

**Majority answer: 5 of 5 runs – Rs. 9,562.50 per instalment**

## Files

```text
Day2/
├── output/
│   ├── 01_react_trace.png
│   ├── 02_cot_compare.png
│   └── 03_self_consistency.png
├── react_trace.py
├── cot_compare.py
├── self_consistency.py
├── README.md
└── explanation.txt