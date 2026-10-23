from functions.get_file_content import get_file_content

test_cases = [("calculator", "lorem.txt"), ("calculator", "main.py"), ("calculator", "pkg/calculator.py"), ("calculator", "/bin/cat"), ("calculator", "pkg/does_not_exist.py")]
 
for wd, target in test_cases:
    print(get_file_content(wd, target) + "\n")
