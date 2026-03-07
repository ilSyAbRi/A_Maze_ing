import sys

def check_arg_AND_file_exist_AND_return_it():

    """Try to open 'config.txt' and read it."""
    """we try to check the error while doing that by the way"""
    """we check argument error and all open error"""
    """just check the exist of file and arg as it should be (:"""
    """return the file content also """

    if len(sys.argv) != 2:
        print("should be 2 argument")
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


def return_content_as_lines(content):
    """
    split content into lines to work whit it as key value in the future
    """
    lines = content.split("\n")
    return lines


def get_config_dict(lines):
    """
    Convert config file lines into a dictionary.
    - Skip empty lines and comments
    - Check '=' exists in each line
    """
    config_element = {}

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
        config_element[key] = value
    return config_element


def check_the_main_key_element(config_dict):
    """
    check mandatory key existence and no extra key there
    """

    REQUIRED_KEYS = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}

    for key in config_dict:
        if key not in REQUIRED_KEYS:
            print(f"Error: extra key found -> {key}")
            sys.exit(1)
    try:
        width = config_dict["WIDTH"]
        height = config_dict["HEIGHT"]
        entry = config_dict["ENTRY"]
        exit_ = config_dict["EXIT"]
        output_file = config_dict["OUTPUT_FILE"]
        perfect = config_dict["PERFECT"]
    except KeyError as missing_key:
        print(f"Error: missing required key -> {missing_key}")
        sys.exit(1)

    print("All required keys found.")


if __name__ == "__main__":

    content = check_arg_AND_file_exist_AND_return_it()

    lines = return_content_as_lines(content)

    ma_dict = get_config_dict(lines)

    check_the_main_key_element(ma_dict)
