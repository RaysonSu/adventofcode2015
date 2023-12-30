from typing import Any
OUTPUT_TYPE = int


def evaluate(data: Any) -> int:
    if isinstance(data, int):
        return data

    if isinstance(data, list):
        return sum(map(evaluate, data))

    if isinstance(data, dict):
        if "red" in data.values():
            return 0

        return sum(map(evaluate, data.values()))

    return 0


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    return sum(map(int, [
        int(number)
        for number
        in "".join(
            char.replace(",", " ")
            for char
            in inp[0]
            if char.isnumeric() or char in "-,"
        ).split(" ")
        if number != ""]))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    data: Any = eval(inp[0])
    return evaluate(data)


def main() -> None:
    test_input: str = """[{"a":2,"b":4},[[[3]]],{"a":{"b":4},"c":-1, "d": "red"}]"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 12
    test_output_part_2_expected: OUTPUT_TYPE = 9

    file_location: str = "python/Advent of Code/2015/Day 12/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
