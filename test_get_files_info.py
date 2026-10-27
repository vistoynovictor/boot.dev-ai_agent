from functions.get_files_info import get_files_info


def print_result(wd: str, td: str):
    result = get_files_info(wd, td)

    print("Result for current directory:")
    print(result)


print_result("calculator", ".")
print_result("calculator", "pkg")
print_result("calculator", "/bin")
print_result("calculator", "../")
