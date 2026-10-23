import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    valid_path = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    try:
        dir_list = os.listdir(target_dir)
    except:
        return f'Error: "{directory}" could not be accessed or listing proccess failed'

    items = []
    for item in dir_list:
        size = os.path.getsize(os.path.join(target_dir, item))
        is_dir = not os.path.isfile(os.path.join(target_dir, item))
        items.append(f"- {item} file_size={size}, is_dir={is_dir}")

    return "\n".join(items)
