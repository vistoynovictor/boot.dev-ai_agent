import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    valid_target = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    content = ""

    try:
        with open(target_dir, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except:
        return f'Error: Unable to read file: "{file_path}"'

    return content
