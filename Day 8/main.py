OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    mem_val: int = 0
    real_val: int = 0
    for row in inp:
        if not row:
            continue
        row = row.strip()
        mem_val += len(row)
        real_val += len(eval(row))

    return mem_val - real_val


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    mem_val: int = 0
    real_val: int = 0
    for row in inp:
        if not row:
            continue
        row = row.strip()
        mem_val += len(row)
        real_val += len(repr(row).replace("\"", "\\\""))

    return real_val - mem_val


def main() -> None:
    test_input: str = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 12
    test_output_part_2_expected: OUTPUT_TYPE = 19

    file_location: str = "python/Advent of Code/2015/Day 8/input.txt"
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
