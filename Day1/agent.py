"""System 3: An AI agent that can use tools."""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS

SYSTEM_PROMPT = """
You are a helpful college assistant.

You have access to tools that contain reliable college course fee data.

Use the tools whenever the question requires course fees or calculations.

After using the tools, give a short and clear final answer.
"""


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
                {"role": "tool", "tool_call_id": tool_call.id, "content": result}
            )


if __name__ == "__main__":
    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)
