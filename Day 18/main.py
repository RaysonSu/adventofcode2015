OUTPUT_TYPE = int


class CellularAutomata1:
    def __init__(self, bound: int = 100, stuck: bool = False) -> None:
        self.points: set[tuple[int, int]] = set()
        self.bound: int = bound
        self.stuck: bool = stuck

        if stuck:
            self.points.add((0, 0))
            self.points.add((0, self.bound - 1))
            self.points.add((self.bound - 1, 0))
            self.points.add((self.bound - 1, self.bound - 1))

    def add_point(self, points: tuple[int, int] | list[tuple[int, int]]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.add(point)
        else:
            self.points.add(points)

    def generate_neighbours(self, point: tuple[int, int]) -> list[tuple[int, int]]:
        neighbours: list[tuple[int, int]] = []
        for y_diff in range(-1, 2):
            for x_diff in range(-1, 2):
                if x_diff == 0 and y_diff == 0:
                    continue
                neighbours.append((point[0] + x_diff, point[1] + y_diff))

        return neighbours

    def determine_future_point(self, point: tuple[int, int]) -> int:
        lookup: int = 0
        for point in self.generate_neighbours(point):
            if point in self.points:
                lookup += 1

        return lookup

    def in_bound(self, point: tuple[int, int]) -> int:
        return min(point) >= 0 and max(point) < self.bound

    def tick(self) -> None:
        new_points: set[tuple[int, int]] = set()
        for point in self.points:
            if self.determine_future_point(point) in [2, 3]:
                new_points.add(point)

            for neighbour in self.generate_neighbours(point):
                if not self.in_bound(neighbour):
                    continue

                count: int = self.determine_future_point(neighbour)
                if neighbour not in self.points and count == 3:
                    new_points.add(neighbour)

        if self.stuck:
            new_points.add((0, 0))
            new_points.add((0, self.bound - 1))
            new_points.add((self.bound - 1, 0))
            new_points.add((self.bound - 1, self.bound - 1))

        self.points = new_points


def main_part_1(inp: list[str], steps: int = 100) -> OUTPUT_TYPE:
    cell: CellularAutomata1 = CellularAutomata1(len(inp))
    grid: list[tuple[int, int]] = []

    for y, row in enumerate(inp):
        for x, char in enumerate(row.strip()):
            if char == "#":
                grid.append((x, y))

    cell.add_point(grid)
    for _ in range(steps):
        cell.tick()

    return len(cell.points)


def main_part_2(inp: list[str], steps: int = 100) -> OUTPUT_TYPE:
    cell: CellularAutomata1 = CellularAutomata1(len(inp), True)
    grid: list[tuple[int, int]] = []

    for y, row in enumerate(inp):
        for x, char in enumerate(row.strip()):
            if char == "#":
                grid.append((x, y))

    cell.add_point(grid)
    for _ in range(steps):
        cell.tick()

    return len(cell.points)


def main() -> None:
    test_input: str = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 4
    test_output_part_2_expected: OUTPUT_TYPE = 17

    file_location: str = "python/Advent of Code/2015/Day 18/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed, 4)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed, 5)

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
