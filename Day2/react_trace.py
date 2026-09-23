"""Day 2: print the agent's real ReAct trace."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Day1"))

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS

SYSTEM_PROMPT = """
You are a helpful college assistant.

The available courses are:
CS101 = 12000
AI202 = 18000
DS303 = 15000

If the question says "all three courses", it means CS101, AI202, and DS303.

Use the available tools whenever the question requires course fees or calculations.

After using the tools, give a short and clear final answer.
"""


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)


def agent(question):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append(message)

        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            function = TOOL_FUNCTIONS[function_name]
            result = function(**arguments)

            print(f"  Tool used: {function_name}({arguments}) -> {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
            )


print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")

answer = agent(QUESTION)

print("\nFINAL ANSWER:", answer)
