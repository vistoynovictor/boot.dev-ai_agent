import os

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file= os.path.normpath(os.path.join(working_dir_abs, file_path))
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    valid_target = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    os.makedirs(file_path, exist_ok=True)

    try:
        with open(target_file, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f'Error: Failed to write to "{file_path}" due to an unexpected error'

