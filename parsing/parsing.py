import sys
from typing import TypedDict

from mazegen.Generator import MazeGenerator


class ParsedConfig(TypedDict):
    """Store validated config values with concrete runtime types."""
    WIDTH: int
    HEIGHT: int
    ENTRY: tuple[int, int]
    EXIT: tuple[int, int]
    OUTPUT_FILE: str
    PERFECT: str
    SEED: int | None


def check_arg_and_file_exist_and_return_it() -> str:
    """Try to open 'config.txt' and read it."""
    if len(sys.argv) != 2:
        print("\n Error: Argument should be == 2")
        sys.exit(1)
    if sys.argv[1] != "config.txt":
        print("\nError: expected config.txt as argument")
        sys.exit(1)
    try:
        with open("config.txt", "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError as exc:
        print(f"\nFile not found1: {exc}")
        sys.exit(1)
    except PermissionError as exc:
        print(f"\nPermission error1: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"\nException error1: {exc}")
        sys.exit(1)


def return_content_as_lines(content: str) -> list[str]:
    """
    split content into lines to work whit it as key value in the future
    """
    lines = content.splitlines()
    return lines


def get_config_dict(lines: list[str]) -> dict[str, str]:
    """
    Convert config file lines into a dictionary.
    - Skip empty lines and comments
    - Check '=' exists in each line
    """
    config_element: dict[str, str] = {}

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
    entry_x: int,
    entry_y: int,
    exit_x: int,
    exit_y: int,
    width: int,
    height: int,
) -> None:
    """
    CHECK (: ENTRY and EXIT coordinates are inside the grid and not equal
    """
    if not (width <= 383) or not (height <= 201):
        raise ValueError("Check : 'width (and or) height' <= 383 (or and) 201")
    if not (width >= 9) or not (height >= 7):
        raise ValueError("Check : 'width (and or) height' < 7 (and or) 9")

    if not (0 <= entry_x < width) or not (0 <= entry_y < height):
        raise ValueError(
            f"ENTRY coordinates out of bounds -> {entry_x},{entry_y}"
        )

    if not (0 <= exit_x < width) or not (0 <= exit_y < height):
        raise ValueError(f"EXIT coordinates out of bounds-> {exit_x},{exit_y}")

    if entry_x == exit_x and entry_y == exit_y:
        raise ValueError("ENTRY and EXIT cannot be the same point")


def check_key_value_element(config_dict: dict[str, str]) -> ParsedConfig:
    """Validate config values and return a typed normalized mapping."""
    try:
        width = int(config_dict["WIDTH"])
        height = int(config_dict["HEIGHT"])

        entry_x_str, entry_y_str = config_dict["ENTRY"].split(",")
        entry_x = int(entry_x_str)
        entry_y = int(entry_y_str)
        entry = (entry_x, entry_y)

        exit_x_str, exit_y_str = config_dict["EXIT"].split(",")
        exit_x = int(exit_x_str)
        exit_y = int(exit_y_str)
        exit_ = (exit_x, exit_y)

        seed_raw = config_dict.get("SEED")
        seed = int(seed_raw) if seed_raw is not None else None

        check_coordinates_in_range(
            entry_x, entry_y, exit_x, exit_y, width, height
        )

        perfect = config_dict["PERFECT"].lower()
        if perfect not in ("true", "false"):
            raise ValueError("PERFECT must be True or False")

        output_file = config_dict["OUTPUT_FILE"].strip()
        if output_file == "config.txt":
            raise ValueError("move config.txt from config file as ouput file")
        if not output_file:
            raise ValueError("OUTPUT_FILE cannot be empty")
        if " " in output_file:
            raise ValueError(
                "OUTPUT_FILE must be a single name without spaces "
                f"-> {output_file}"
            )
        if not output_file.endswith(".txt"):
            raise ValueError(
                f"OUTPUT_FILE must end with .txt -> {output_file}"
            )

        return {
            "WIDTH": width,
            "HEIGHT": height,
            "ENTRY": entry,
            "EXIT": exit_,
            "OUTPUT_FILE": output_file,
            "PERFECT": perfect,
            "SEED": seed,
        }

    except KeyError as exc:
        print(f"\nkey error : {exc}")
        sys.exit(1)
    except ValueError as exc:
        print(f"\nValueError: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"\nException error2: {exc}")
        sys.exit(1)


def check_entry_exit_42(
    entry: tuple[int, int],
    exit_: tuple[int, int],
    lst1: list[tuple[int, int]],
    lst2: list[tuple[int, int]],
) -> None:
    """Ensure entry and exit are not in forbidden 42 coordinates."""
    try:
        if entry in lst1 or entry in lst2:
            raise ValueError("entry in 42")
        if exit_ in lst1 or exit_ in lst2:
            raise ValueError("exit in 42")
    except ValueError as exc:
        print("check 42:", exc)
        sys.exit(1)


def config_parser() -> MazeGenerator:
    """Parse config file and return a validated MazeGenerator instance."""
    try:
        content = check_arg_and_file_exist_and_return_it()
        lines = return_content_as_lines(content)
        raw_dict = get_config_dict(lines)
        cfg = check_key_value_element(raw_dict)

        maze = MazeGenerator(
            width=cfg["WIDTH"],
            height=cfg["HEIGHT"],
            entry=cfg["ENTRY"],
            exit=cfg["EXIT"],
            output_file=cfg["OUTPUT_FILE"],
            perfect=cfg["PERFECT"],
            seed=cfg["SEED"],
        )
        lst1, lst2 = maze.find_42()
        check_entry_exit_42(maze.entry, maze.exit, lst1, lst2)

        maze.mark_42()
        return maze
    except Exception as exc:
        print(exc)
        sys.exit(1)
