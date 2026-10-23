import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Ai Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise Exception("API key not found. Please set the GEMINI_API_KEY environment variable.")

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    resp = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages) 
    prompt_tokens = resp.usage_metadata.prompt_token_count
    response_tokens = resp.usage_metadata.candidates_token_count

    if prompt_tokens == None or response_tokens == None:
        raise RuntimeError("API request failed")
    if args.verbose:
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
        print(f"User prompt: {resp.text}")
    print(resp.text)


if __name__ == "__main__":
    main()
