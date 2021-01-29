import os
import time

input_file = "input"
path = os.path.dirname(os.path.realpath(__file__))


def parse_line(line, data):
    l, w, h = map(int, line.split('x'))
    data.append((l, w, h))


def calculate_box(dims):
    l, w, h = dims
    a, b, c = l*w, l*h, w*h
    return 2 * (a + b + c) + min(a, b, c)


def calculate_ribbon(dims):
    l, w, h = dims
    present = 2 * ((l + w + h) - max(l, w, h))
    bow = l * w * h
    return present + bow


def solve(data):
    return sum(map(calculate_box, data))


def solve2(data):
    return sum(map(calculate_ribbon, data))


def main(infile=input_file):
    infile = f"{path}/resources/{infile}"
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            parse_line(line, data)
    start = time.monotonic()
    result = [None] * 2
    result[0] = solve(data)
    result[1] = solve2(data)
    end = time.monotonic()
    return result[0], result[1], end - start


def display(p1, p2, duration_seconds):
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    print(f"Elapsed time: {duration_seconds}")


if __name__ == '__main__':
    part_1, part_2, elapsed_time = main()
    display(part_1, part_2, elapsed_time)
