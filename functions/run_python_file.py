import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args=None) -> str:
    abs_file_path  = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_path = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_work_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    command = ["python", f"{abs_file_path}"]
    if args:
        command.append(args)
    try:
        python_run = subprocess.run(
            command,
            cwd=working_directory,
            timeout=30,
            capture_output=True,
            text=True
        )
    except Exception as e:
        return f'Error: executing Python file: {e}'
    results = []
    if python_run.stdout:
        results.append(f"STDOUT: {python_run.stdout}.")
    if python_run.stderr:
        results.append(f"STDERR: {python_run.stderr}.")
    if return_code := python_run.returncode != 0:
        results.append(f"Process exited with code {return_code}")
    return "\n".join(results) if results else "No output produced."


