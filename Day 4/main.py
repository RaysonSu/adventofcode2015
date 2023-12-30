from hashlib import md5 as md
OUTPUT_TYPE = int


def md5(x: str) -> str:
    return md(x.encode()).hexdigest().zfill(32)


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    key: str = inp[0].strip()

    guess: int = 0
    while True:
        hashed: str = md5(key + str(guess))
        if hashed.startswith("00000"):
            return guess

        guess += 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    key: str = inp[0].strip()

    guess: int = 0
    while True:
        hashed: str = md5(key + str(guess))
        if hashed.startswith("000000"):
            return guess

        guess += 1


def main() -> None:
    test_input: str = """pqrstuv"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1048970

    file_location: str = "python/Advent of Code/2015/Day 4/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    print(f"Part 2: {main_part_2(input_file)}")


if __name__ == "__main__":
    main()
