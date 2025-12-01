#!/usr/bin/env python3

from sys import stdin


def solve_dial(lines):
    d, max, part1, part2 = 50, 100, 0, 0
    for line in lines:
        direction, number = line[0], int(line[1:])
        sign = 1 if direction == 'R' else -1
        for _ in range(0, number):
            d = (d+sign) % max
            if (d == 0):
                part2 += 1
        if (d == 0):
            part1 += 1
    print(part1)
    print(part2)


def solve() -> None:
    input = stdin.read().splitlines()
    solve_dial(input)


if __name__ == '__main__':
    solve()
