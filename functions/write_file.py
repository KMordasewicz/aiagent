import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_file_path  = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_path = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_work_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        dir_to_make = os.path.dirname(abs_file_path)
        try:
            os.makedirs(dir_to_make, exist_ok=True)
        except Exception as e:
            return f'Error unable to create "{file_path}" file: {e}'
    try:
        with open(abs_file_path, "w") as f:
            _ = f.write(content)
    except Exception as e:
        return f'Error unable to write "{content}" to "{file_path}" file: {e}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

