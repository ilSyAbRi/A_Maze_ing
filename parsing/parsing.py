import sys

def check_arg_AND_file_exist():
    """Try to open 'config.txt' and read it."""
    """we try to check the error while doing that by the way"""
    """we check argument error and all open error"""
    """just check the exist of file and arg as it should be (:"""
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


def check_valid_element():
    lines = content.split("\n")
    for line in lines:
        line = line.strip()

    if line.startswith("#"):
        continue

    key,value = line.split("=",1)
    key = key.strip()
    value = value.strip()

    if not value.replace(" ", "").isdigit():
            print(f"Error: invalid number in line -> {line}")
            sys.exit(1)

if __name__ == "__main__":
    content = check_arg_AND_file_exist()
    check_valid_element(content)
