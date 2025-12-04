#!/usr/bin/env python3

from sys import stdin


def number_of_adj(input, x, y, n, m):
    adj = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            dx = x+i
            dy = y+j
            if (dx >= 0 and dx < n and dy >= 0 and dy < m and input[dx][dy] == '@'):
                adj += 1

    return adj


def forklifts(input, remove=False):
    forklifts = 0
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if (c == '@' and number_of_adj(input, i, j, len(input), len(line)) < 5):
                forklifts += 1
                if (remove):
                    l = list(input[i])
                    l[j] = '.'
                    input[i] = ''.join(l)
    return forklifts


def remove_rolls(input):
    forklifts_found = forklifts(input, remove=True)
    all = 0
    while (forklifts_found > 0):
        all += forklifts_found
        forklifts_found = forklifts(input, remove=True)
    return all


def solve() -> None:
    input = stdin.read().splitlines()
    print(forklifts(input))
    print(remove_rolls(input))


if __name__ == '__main__':
    solve()
