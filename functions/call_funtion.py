from collections.abc import Callable
from google.genai import types

import config

from functions.get_fies_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

function_name_to_function: dict[str, Callable] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}

def call_function(function_call_part: types.FunctionCall, verbose: bool=False) -> types.Content:
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    called_function = function_name_to_function.get(function_call_part.name)
    if not called_function:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    called_function_args = function_call_part.args
    called_function_args.update(working_directory=config.WORKING_DIRECTORY)
    function_call_result = called_function(**called_function_args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_call_result},
            )
        ],
    )


