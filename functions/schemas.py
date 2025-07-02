from google.genai import types
import config


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Read file in the specified path up to {config.MAX_CHARACTER} characters long, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="get_write_file",
    description="Write specified content to file in the specified path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file."
            ),
        },
        required=["file_path"],
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run specified python file in the specified path with given optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional agruments to pass to python program."
                ),
                description="Optional agruments to pass to python program."
            ),
        },
        required=["file_path"],
    ),
)
