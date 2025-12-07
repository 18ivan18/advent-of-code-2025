#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def timelines(input):
    all = defaultdict(int)
    all[input[0].index('S')] = 1
    all_y = set([input[0].index('S')])
    for line in input[1:]:
        new_all_y = set()
        for y in sorted(list(all_y)):
            if (line[y] == '^'):
                before = all[y]
                all[y] = 0
                all[y+1] += before
                all[y-1] += before
                new_all_y.add(y+1)
                new_all_y.add(y-1)
            else:
                new_all_y.add(y)
        all_y = new_all_y
    return sum(all.values())


def times_split(input):
    t = 0
    all_y = set([input[0].index('S')])
    for line in input[1:]:
        new_all_y = set()
        for y in all_y:
            if (line[y] == '^'):
                t += 1
                new_all_y.add(y+1)
                new_all_y.add(y-1)
            else:
                new_all_y.add(y)
        all_y = new_all_y
    return t


def solve() -> None:
    input = stdin.read().splitlines()
    print(times_split(input))
    print(timelines(input))


if __name__ == '__main__':
    solve()
