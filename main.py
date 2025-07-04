import os
import sys
from tabnanny import verbose
from dotenv import load_dotenv
from google.genai import Client, types

import config
from functions.call_funtion import call_function
from functions.schemas import (
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
)

def generate_content(client: Client, prompt: str, is_verb: bool) -> None:
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    for _ in range(20):
        response: types.GenerateContentResponse = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=config.SYSTEM_PROMPT,
                tools=[available_functions],
            ),
        )
        if is_verb:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if response.candidates:
            messages.extend([candidate.content for candidate in response.candidates])
        if response.function_calls:
            # function_call_responses = []
            for function_call in response.function_calls:
                function_call_content = call_function(function_call, is_verb)
                if not function_call_content.parts or not function_call_content.parts[0].function_response.response:
                    raise Exception("Fatal error: function call was made, but no response.")
                if is_verb:
                    print(f"-> {function_call_content.parts[0].function_response.response}")
                messages.append(function_call_content)
        else:
            print(response.text)
            break
            # function_call_responses.append(function_call_content.parts[0])
        # if not function_call_responses:
        #     raise Exception("No function responses generated, exiting.")
        # return function_call_responses


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
    content = generate_content(client, prompt, is_verb)
    if content:
        print(content)


if __name__ == "__main__":
    main()
