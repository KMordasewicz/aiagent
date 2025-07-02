import os
import sys
from dotenv import load_dotenv
from google.genai import Client, types

import config
from functions.schemas import (
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
)


def main():
    try:
        prompt = sys.argv[1]
    except IndexError:
        print("ERROR: Expecting prompt argument recived None.")
        sys.exit(1)
    is_verb = False
    if "".join(sys.argv[2:]) == "--verbose":
        is_verb = True
    _ = load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = Client(api_key=api_key)
    system_prompt = config.SYSTEM_PROMPT
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )
    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=prompt)
            ]
        )
    ]
    response: types.GenerateContentResponse = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
    )
    if is_verb:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
