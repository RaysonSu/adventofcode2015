OUTPUT_TYPE = int


def mod_exp(base: int, exp: int, mod: int) -> int:
    base = base % mod
    ret: int = base
    extra: int = 1
    while exp > 1:
        if exp % 2 == 0:
            ret = (ret * ret) % mod
        else:
            extra = (extra * ret) % mod
            exp -= 1
            ret = (ret * ret) % mod
        exp = exp >> 1
    ret = (ret * extra) % mod
    return ret


def triangular(n: int) -> int:
    return n * (n + 1) // 2


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    data: list[int] = [
        int(x)
        for x in "".join([
            char
            for char in inp[0]
            if char.isnumeric() or char in " "
        ]).split(" ")
        if x != ""
    ]

    exp: int = triangular(data[0] + data[1] - 2) + data[1] - 1
    ret: int = 20151125
    ret *= mod_exp(252533, exp, 33554393)
    ret %= 33554393
    return ret


def main() -> None:
    test_input: str = """To continue, please consult the code grid in the manual.  Enter the code at row 5, column 4."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 6899651

    file_location: str = "python/Advent of Code/2015/Day 25/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()


if __name__ == "__main__":
    main()
