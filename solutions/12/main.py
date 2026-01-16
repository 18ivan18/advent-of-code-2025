#!/usr/bin/env python3

from sys import stdin


def solve() -> None:
    input = stdin.read().split('\n\n')
    figures = [x[3:] for x in input[:-1]]
    success = 0
    for test in input[-1].splitlines():
        field, fs = test.split(': ')
        x, y = field.split('x')
        area = int(x)*int(y)
        area_figures = 0
        for i, f in enumerate(fs.split(' ')):
            area_figures += figures[i].count('#') * int(f)
        if (area - area_figures >= 0):
            success += 1
    print(success)


if __name__ == '__main__':
    solve()
