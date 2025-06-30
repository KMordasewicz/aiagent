import os
import sys
from dotenv import load_dotenv
from google.genai import Client, types


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
        contents=messages
    )
    if is_verb:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

if __name__ == "__main__":
    main()
