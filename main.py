import argparse
import os
import sys
import json

from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt
from call_function import available_functions
from call_function import call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
    raise RuntimeError("Unable to find API key")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]


def go_ai():
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    if response.usage != None and args.verbose == True:
        print("""
        User prompt: {args.user_prompt}
        Response tokens: {response.usage.completion_tokens}\n---\n
        Prompt tokens: {response.usage.prompt_tokens}
        """)

    message = response.choices[0].message
    messages.append(message)

    return message


def main():

    for _ in range(20):
        request = go_ai()

        if request.tool_calls:
            for tool_call in request.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)

                if not result_message["content"]:
                    print("Something went wrong...")
                    raise Exception("Something went wrong...")

                if args.verbose:
                    print(f"-> {result_message['content']}")
                else:
                    print(result_message["content"])
        else:
            print(request.content)
            sys.exit(0)
    print("Max requests reached")
    sys.exit(1)


if __name__ == "__main__":
    main()
