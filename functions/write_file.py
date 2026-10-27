import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        workdir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(workdir, file_path))

        valid_path = os.path.commonpath([workdir, target_file]) == workdir

        if not valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        return "Success: file written with the specified content"
    except Exception as e:
        return f"Error: Something went wrong when writing to file {file_path}: {e}"


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write to, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "The content to be written to the specified file",
                },
            },
        },
    },
}
