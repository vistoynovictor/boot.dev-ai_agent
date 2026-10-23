from functions.get_files_info import get_files_info

test_cases = [("calculator", "."), ("calculator", "pkg"), ("calculator", "/bin"), ("calculator", "../")]

for wk_dir, target in test_cases:
    print(f"Result for {target} directory:")
    print(get_files_info(wk_dir, target) + '\n')
