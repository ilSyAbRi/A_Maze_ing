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


def check_valid_element(content):
    lines = content.split("\n")
    config = {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            print(f"Error: line missing '=' -> {line}")
            sys.exit(1)
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        config[key] = value

    try:
        width = config["WIDTH"]
        height = config["HEIGHT"]
        entry = config["ENTRY"]
        exit_ = config["EXIT"]
        output_file = config["OUTPUT_FILE"]
        perfect = config["PERFECT"]
    except KeyError as missing_key:
        print(f"Error: missing required key -> {missing_key}")
        sys.exit(1)

    print("All required keys found.")
    return config

if __name__ == "__main__":
    content = check_arg_AND_file_exist()
    check_valid_element(content)
