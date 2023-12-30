OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    values: dict[str, int] = {}
    while len(values.keys()) < len(inp):
        for row in inp:
            row = row.strip()
            data: list[str] = row.split(" -> ")
            if data[1] in values.keys():
                continue

            if data[0].isnumeric():
                values[data[1]] = int(data[0])
                continue

            left: list[str] = data[0].split(" ")

            v1: int
            v2: int

            if len(left) == 1:
                if left[0] not in values.keys():
                    continue
                values[data[1]] = values[left[0]]
                continue

            if left[0] == "NOT":
                if left[1] not in values.keys():
                    continue

                values[data[1]] = ~values[left[1]]
                continue

            if left[0] not in values.keys() and not left[0].isnumeric():
                continue

            if left[2] not in values.keys() and not left[2].isnumeric():
                continue

            if left[0].isnumeric():
                v1 = int(left[0])
            else:
                v1 = values[left[0]]

            if left[2].isnumeric():
                v2 = int(left[2])
            else:
                v2 = values[left[2]]

            if left[1] == "AND":
                values[data[1]] = v1 & v2
            elif left[1] == "OR":
                values[data[1]] = v1 | v2
            elif left[1] == "LSHIFT":
                values[data[1]] = v1 << v2
            elif left[1] == "RSHIFT":
                values[data[1]] = v1 >> v2
            else:
                continue

    return values["a"]


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    values: dict[str, int] = {}
    values["b"] = main_part_1(inp)
    while len(values.keys()) < len(inp):
        for row in inp:
            row = row.strip()
            data: list[str] = row.split(" -> ")
            if data[1] in values.keys():
                continue

            if data[0].isnumeric():
                values[data[1]] = int(data[0])
                continue

            left: list[str] = data[0].split(" ")

            v1: int
            v2: int

            if len(left) == 1:
                if left[0] not in values.keys():
                    continue
                values[data[1]] = values[left[0]]
                continue

            if left[0] == "NOT":
                if left[1] not in values.keys():
                    continue

                values[data[1]] = ~values[left[1]]
                continue

            if left[0] not in values.keys() and not left[0].isnumeric():
                continue

            if left[2] not in values.keys() and not left[2].isnumeric():
                continue

            if left[0].isnumeric():
                v1 = int(left[0])
            else:
                v1 = values[left[0]]

            if left[2].isnumeric():
                v2 = int(left[2])
            else:
                v2 = values[left[2]]

            if left[1] == "AND":
                values[data[1]] = v1 & v2
            elif left[1] == "OR":
                values[data[1]] = v1 | v2
            elif left[1] == "LSHIFT":
                values[data[1]] = v1 << v2
            elif left[1] == "RSHIFT":
                values[data[1]] = v1 >> v2
            else:
                continue

    return values["a"]


def main() -> None:
    test_input: str = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
d AND e -> p
f AND g -> q
h AND i -> r
q AND r -> n
n OR p -> z
z -> a"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 72
    test_output_part_2_expected: OUTPUT_TYPE = 72

    file_location: str = "python/Advent of Code/2015/Day 7/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = [x.replace("\n", "") for x in input_file]

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
