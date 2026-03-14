import sys


def check_arg_AND_file_exist_AND_return_it():

    """Try to open 'config.txt' and read it."""
    """we try to check the error while doing that by the way"""
    """we check argument error and all open error"""
    """just check the exist of file and arg as it should be (:"""
    """return the file content also """

    if len(sys.argv) != 2:
        print("\n Error: Argument should be == 2")
        sys.exit(1)
    if sys.argv[1] != "config.txt":
        print("\nError: expected config.txt as argument")
        sys.exit(1)
    try:
        with open("config.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("\nError: config.txt file not found!")
        sys.exit(1)
    except PermissionError:
        print("\nError: Permission denied for config.txt!")
        sys.exit(1)
    except Exception as e:
        print(f"\nOther error1: {e}")
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
            print(f"\nError: line missing '=' -> {line}")
            sys.exit(1)
        key, value = line.split("=", 1)
        key = key.strip().upper()
        value = value.strip()
        if key in config_element:
            print(f"\nError: duplicate key found -> {key}")
            sys.exit(1)

        config_element[key] = value
    return config_element


def check_coordinates_in_range(
        entry_x, entry_y, exit_x, exit_y, width, height
        ):
    """
    CHECK (: ENTRY and EXIT coordinates are inside the grid and not equal
    """
    if not (width <= 400) or not (height <= 400):
        raise ValueError("Check : 'width (and or) height' <= 400")
    if not (width >= 2) or not (height >= 2):
        raise ValueError("Check : 'width (and or) height' < 2")

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
                print(f"\nError: extra key found -> {key}")
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
        if " " in output_file:
            raise ValueError(f"OUTPUT_FILE must be a single name"
                             f"without spaces -> {output_file}")
        if not output_file.endswith(".txt"):
            raise ValueError(f"OUTPUT_FILE must end with .txt "
                             f"-> {output_file}")

    except KeyError as missing_key:
        print(f"\nError: missing required key -> {missing_key}")
        sys.exit(1)
    except ValueError as spongbob:
        print(f"\nError: {spongbob}")
        sys.exit(1)
    except Exception as unknown:
        print(f"\nOther error: {unknown}")
        sys.exit(1)


def main():
    content = check_arg_AND_file_exist_AND_return_it()
    lines = return_content_as_lines(content)
    ma_dict = get_config_dict(lines)
    check_key_value_element(ma_dict)
    return ma_dict


if __name__ == "__main__":
    main()
