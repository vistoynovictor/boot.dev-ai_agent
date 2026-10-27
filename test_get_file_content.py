from functions.get_file_content import get_file_content


def print_result(wd: str, fp: str):
    result = get_file_content(wd, fp)
    print(result)
    if result[:6] != "Error:":
        print(f"{fp} length: {len(result)}")
        print(f"{fp} truncated: {'truncated' in result}")


print_result("calculator", "lorem.txt")
print_result("calculator", "main.py")
print_result("calculator", "pkg/calculator.py")
print_result("calculator", "/bin/cat")
print_result("calculator", "pkg/does_not_exist.py")
