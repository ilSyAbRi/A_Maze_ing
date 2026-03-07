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
        print("Error: expected config.txt as argument")
        sys.exit(1)
    try:
        with open("config.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Error: config.txt file not found!")
        sys.exit(1)
    except PermissionError:
        print("Error: Permission denied for config.txt!")
        sys.exit(1)
    except Exception as e:
        print(f"Other error1: {e}")
        sys.exit(1)


def return_content_as_lines(content):
    """
    split content into lines to work whit it as key value in the future
    """
    lines = content.splitlines()
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


def check_coordinates_in_range(
        entry_x, entry_y, exit_x, exit_y, width, height
        ):
    """
    CHECK (: ENTRY and EXIT coordinates are inside the grid and not equal
    """
    if not (width >= 2) or not (height >= 2):
        raise ValueError(f"width or height are too small :"
                         f"width : {width} or height : {height} < 2")
    if not (0 <= entry_x < width) or not (0 <= entry_y < height):
        raise ValueError(f"ENTRY coordinates out of bounds"
                         f" -> {entry_x},{entry_y}")

    if not (0 <= exit_x < width) or not (0 <= exit_y < height):
        raise ValueError(f"EXIT coordinates out of bounds"
                         f"-> {exit_x},{exit_y}")

    if entry_x == exit_x and entry_y == exit_y:
        raise ValueError("ENTRY and EXIT cannot be the same point")


def check_key_value_element(config_dict):
    try:

        REQUIRED_KEYS = {"WIDTH", "HEIGHT", "ENTRY",
                         "EXIT", "OUTPUT_FILE", "PERFECT"}

        for key in config_dict:
            if key not in REQUIRED_KEYS:
                print(f"Error: extra key found -> {key}")
                sys.exit(1)

        width = int(config_dict["WIDTH"])
        height = int(config_dict["HEIGHT"])

        entry_x, entry_y = config_dict["ENTRY"].split(",")
        entry_x = int(entry_x)
        entry_y = int(entry_y)

        exit_x, exit_y = config_dict["EXIT"].split(",")
        exit_x = int(exit_x)
        exit_y = int(exit_y)

        check_coordinates_in_range(
                entry_x, entry_y, exit_x, exit_y, width, height
                )

        perfect = config_dict["PERFECT"].lower()
        if perfect not in ("true", "false"):
            raise ValueError("PERFECT must be True or False")

        output_file = config_dict["OUTPUT_FILE"].strip()
        if not output_file:
            raise ValueError("OUTPUT_FILE cannot be empty")

    except KeyError as missing_key:
        print(f"Error: missing required key -> {missing_key}")
        sys.exit(1)
    except ValueError as spongbob:
        print(f"Error: {spongbob}")
        sys.exit(1)
    except Exception as unknown:
        print(f"Other error: {unknown}")
        sys.exit(1)


if __name__ == "__main__":

    print("====== Start parsing ======")

    print("\n === Read file and return content whit the check of arg ===")
    print("     processing...")
    content = check_arg_AND_file_exist_AND_return_it()
    print(" [File read successfully!]")
    print(" [content of file returned successfuly!]")
    print("                                     ->  Done")

    print("\n === Make content i have into several lines ===")
    print("     processing...")
    lines = return_content_as_lines(content)
    print("                                     ->  Done")

    print("\n === Make lines i have into key value dict ===")
    print("     processing...")
    ma_dict = get_config_dict(lines)
    print("                                     ->  Done")

    print("\n === Check validation of key value i have ===")
    print("     processing...")
    check_key_value_element(ma_dict)
    print("                                     ->  Done")

    print("\n       ****** parsing status : DONE ~")
