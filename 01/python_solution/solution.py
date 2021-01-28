import os
import time
from functools import reduce
import sys
sys.setrecursionlimit(100_000)

infile = "input"
path = os.path.dirname(os.path.realpath(__file__))


def parse_line(line):
    return list(line)


def solve(data):
    return reduce(lambda acc, item: acc+1 if item == '(' else acc-1, data, 0)


def solve2(data):
    def find_floor(i, curr):
        if i >= len(data):
            raise Exception
        nxt = curr+1 if data[i] == '(' else curr-1
        if nxt == -1:
            return i+1
        return find_floor(i+1, nxt)
    return find_floor(0, 0)


def main(infile=infile):
    input_file = f"{path}/resources/{infile}"
    data = None
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            data = parse_line(line)
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
