OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[set[str], dict[str, dict[str, int]]]:
    keys: set[str] = set()
    for row in inp:
        keys = keys.union({
            part for part in row.strip().split(" ")
            if not part.isnumeric()
        })

    keys.remove("to")
    keys.remove("=")

    ret: dict[str, dict[str, int]] = {key: {} for key in keys}
    for row in inp:
        data: list[str] = row.strip().split(" ")
        ret[data[2]][data[0]] = int(data[4])
        ret[data[0]][data[2]] = int(data[4])
    return keys, ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    points: set[str]
    paths: dict[str, dict[str, int]]
    points, paths = parse_inp(inp)

    checking: list[tuple[int, tuple[str, ...]]] = [
        (0, (point,)) for point in points]
    best: int = 1000000000000
    while checking:
        score: int
        path: tuple[str, ...]
        score, path = checking.pop(0)

        if len(path) == len(points):
            best = min(score, best)

        for location, length in paths[path[-1]].items():
            if location in path:
                continue

            checking.append((
                score + length,
                path + (location,)
            ))

    return best


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    points: set[str]
    paths: dict[str, dict[str, int]]
    points, paths = parse_inp(inp)

    checking: list[tuple[int, tuple[str, ...]]] = [
        (0, (point,)) for point in points]
    best: int = 0
    while checking:
        score: int
        path: tuple[str, ...]
        score, path = checking.pop(0)

        if len(path) == len(points):
            best = max(score, best)

        for location, length in paths[path[-1]].items():
            if location in path:
                continue

            checking.append((
                score + length,
                path + (location,)
            ))

    return best


def main() -> None:
    test_input: str = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 605
    test_output_part_2_expected: OUTPUT_TYPE = 982

    file_location: str = "python/Advent of Code/2015/Day 9/input.txt"
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
