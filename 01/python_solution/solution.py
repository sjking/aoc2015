import os
import time

infile = "input"
path = os.path.dirname(os.path.realpath(__file__))


def parse_line(line):
    pass


def main(infile=infile):
    input_file = f"{path}/resources/{infile}"
    data = None
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            data = parse_line(line, data)
    start = time.monotonic()
    result = [None] * 2
    result[0] = solve(data)
    result[1] = solve2(data)
    end = time.monotonic()
    return result[0], result[1], end - start


def display(part_1, part_2, elapsed_time):
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    print(f"Elapsed time: {elapsed_time}")


if __name__ == '__main__':
    part_1, part_2, elapsed_time = main()
    display(part_1, part_2, elapsed_time)
