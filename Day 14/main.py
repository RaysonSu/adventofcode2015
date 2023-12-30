from collections import defaultdict
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> list[tuple[int, int, int]]:
    ret: list[tuple[int, int, int]] = []
    for row in inp:
        data: list[int] = [
            int(number)
            for number
            in "".join(
                char.replace(",", " ")
                for char
                in row
                if char.isnumeric() or char in "-, "
            ).split(" ")
            if number != ""
        ]
        ret.append((data[0], data[1], data[2]))

    return ret


def simulate(reindeer: tuple[int, int, int], time: int) -> int:
    speed: int
    active: int
    inactive: int
    speed, active, inactive = reindeer

    cycles: int
    remainder: int
    cycles, remainder = divmod(time, active + inactive)

    return (cycles * active + min(remainder, active)) * speed


def main_part_1(inp: list[str], time: int = 2503) -> OUTPUT_TYPE:
    reindeers: list[tuple[int, int, int]] = parse_inp(inp)

    ret: int = 0
    for reindeer in reindeers:
        ret = max(ret, simulate(reindeer, time))

    return ret


def main_part_2(inp: list[str], time: int = 2503) -> OUTPUT_TYPE:
    reindeers: list[tuple[int, int, int]] = parse_inp(inp)
    scores: list[int] = [0 for _ in inp]

    for t in range(1, time + 1):
        distances: list[int] = [
            simulate(reindeer, t)
            for reindeer in reindeers
        ]

        best: int = max(distances)
        for reindeer, distance in enumerate(distances):
            if distance == best:
                scores[reindeer] += 1

    return max(scores)


def main() -> None:
    test_input: str = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 1120
    test_output_part_2_expected: OUTPUT_TYPE = 689

    file_location: str = "python/Advent of Code/2015/Day 14/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 1000)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed, 1000)

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
