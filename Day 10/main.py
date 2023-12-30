OUTPUT_TYPE = int


def main_part_1(inp: list[str], iterations: int = 40) -> OUTPUT_TYPE:
    seq: str = inp[0].strip()
    for _ in range(iterations):
        replacements = [
            ("111", "a"),
            ("11", "b"),
            ("1", "c"),
            ("222", "d"),
            ("22", "e"),
            ("2", "f"),
            ("333", "g"),
            ("33", "h"),
            ("3", "i"),
            ("a", "31"),
            ("b", "21"),
            ("c", "11"),
            ("d", "32"),
            ("e", "22"),
            ("f", "12"),
            ("g", "33"),
            ("h", "23"),
            ("i", "13")
        ]

        for ori, new in replacements:
            seq = seq.replace(ori, new)
    return len(seq)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    return main_part_1(inp, 50)


def main() -> None:
    test_input: str = """1"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 6
    test_output_part_2_expected: OUTPUT_TYPE = 1166642

    file_location: str = "python/Advent of Code/2015/Day 10/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 5)
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
