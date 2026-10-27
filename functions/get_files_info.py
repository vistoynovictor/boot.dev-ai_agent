import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        is_dir = os.path.isdir(target_dir)
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if is_dir == False:
            return f"Error: {directory} is not a directory"

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        item_list = []

        items = os.listdir(target_dir)

        for i in items:
            item_path = f"{target_dir}/{i}"
            size = os.path.getsize(item_path)
            item_dir = os.path.isdir(item_path)

            item_list.append(f"\t- {i}: file_size={size} bytes, is_dir={item_dir}")

        return "\n".join(item_list)

    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
