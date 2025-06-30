import os

MAX_SIZE: int = 10_000

def get_file_content(working_directory: str, file_path: str) -> str:
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(full_path, "r") as f:
            content: str = f.read(MAX_SIZE)
    except Exception as e:
        return f"Error unable to read file {file_path} content: {e}"
    if len(content) == MAX_SIZE:
        content += f'[...File "{file_path}" truncated at 10000 characters]'
    return content
