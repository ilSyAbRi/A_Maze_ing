import sys


def check_arg_AND_file_exist():
    """Try to open 'config.txt' and read it."""
    if len(sys.argv) != 2:
        print("ONLY 2 ARGUMENT HERE NEGA")
        sys.exit(1)
    if sys.argv[1] != "config.txt":
        print("argv[1] : I AM NOT config.txt AND I SHOULD BE")
        sys.exit(1)
    try:
        with open("config.txt", "r") as file:
            content = file.read()
            print("File read successfully!")
            return content
    except FileNotFoundError:
        print("Error: config.txt file not found!")
        sys.exit(1)
    except PermissionError:
        print("Error: Permission denied for config.txt!")
        sys.exit(1)
    except Exception as e:
        print(f"Other error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    check_arg_AND_file_exist()
