# functions.py

from os.path import isdir, abspath, getsize
import os

def get_files_info(working_directory: str, directory: str|None=None):
    abs_working_dir = abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        results: list[str] = []
        for file in os.listdir(target_dir):
            full_file_path = os.path.join(target_dir, file)
            file_size = getsize(full_file_path)
            file_info = f"- {file}: file_size={file_size} bytes, is_dir={isdir(full_file_path)}"
            results.append(file_info)
        return "\n".join(results)
    except Exception as e:
        print(f"Error listing files: {e}")

