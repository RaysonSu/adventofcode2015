OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    points: list[list[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    for row in inp:
        row = row.replace("toggle", "toggle blahaj")
        parsed: list[str] = row.split(" ")
        x_low: int = int(parsed[2].split(",")[0])
        x_high: int = int(parsed[4].split(",")[0])
        y_low: int = int(parsed[2].split(",")[1])
        y_high: int = int(parsed[4].split(",")[1])

        for x in range(x_low, x_high + 1):
            for y in range(y_low, y_high + 1):
                if parsed[1] == "on":
                    points[y][x] = 1
                elif parsed[1] == "off":
                    points[y][x] = 0
                else:
                    points[y][x] = 1 - points[y][x]

    return sum(map(sum, points))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    points: list[list[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    for row in inp:
        row = row.replace("toggle", "toggle blahaj")
        parsed: list[str] = row.split(" ")
        x_low: int = int(parsed[2].split(",")[0])
        x_high: int = int(parsed[4].split(",")[0])
        y_low: int = int(parsed[2].split(",")[1])
        y_high: int = int(parsed[4].split(",")[1])

        for x in range(x_low, x_high + 1):
            for y in range(y_low, y_high + 1):
                if parsed[1] == "on":
                    points[y][x] += 1
                elif parsed[1] == "off":
                    points[y][x] = max(0, points[y][x] - 1)
                else:
                    points[y][x] += 2

    return sum(map(sum, points))


def main() -> None:
    test_input: str = """turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 998996
    test_output_part_2_expected: OUTPUT_TYPE = 1001996

    file_location: str = "python/Advent of Code/2015/Day 6/input.txt"
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
