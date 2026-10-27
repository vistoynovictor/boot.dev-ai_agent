import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        workdir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(workdir, file_path))

        valid_path = os.path.commonpath([workdir, target_file]) == workdir
        valid_file = os.path.isfile(target_file)
        python_file = target_file.endswith(".py")

        if not valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not valid_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not python_file:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)

        task = subprocess.run(command, capture_output=True, text=True, timeout=30)

        task_output = f"\n---[{file_path}]---\n"

        if task.returncode != 0:
            task_output += f"\tProcess exited with code {task.returncode}\n"

        if not task.stdout and not task.stderr:
            task_output += "\tNo output produced\n"
        else:
            task_output += f"\tSTDOUT: {task.stdout}\n\tSTDERR: {task.stderr}\n"

        task_output += f"---[End of {file_path}]---\n\n"
        return task_output
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_pyhon_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a pyhton file in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the pyton file to run, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array[string]",
                    "description": "Array of arguments to add to the command intended to run",
                },
            },
        },
    },
}
