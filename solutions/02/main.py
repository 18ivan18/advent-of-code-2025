#!/usr/bin/env python3

from sys import stdin
import re

pettern1 = re.compile(r'^(\d+)\1$')
pettern2 = re.compile(r'^(\d+)(?:\1)+$')


def invalid_ids(input):
    sum1 = 0
    sum2 = 0
    for r in input:
        f, t = r.split('-')
        start, stop = int(f), int(t)
        for i in range(start, stop+1):
            if (pettern1.fullmatch(str(i))):
                sum1 += i
            if (pettern2.fullmatch(str(i))):
                sum2 += i

    print(sum1)
    print(sum2)


def solve() -> None:
    input = stdin.read().split(',')
    invalid_ids(input)


if __name__ == '__main__':
    solve()
