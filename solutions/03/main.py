#!/usr/bin/env python3

from sys import stdin

alpha = '9876543210'


def get_max(line, digits):
    n = ''
    last_found = '9'
    while (len(n) < digits):
        try:
            i = line.index(last_found)
        except:
            i = -1
        if (i == -1 or i >= len(line)-digits+len(n)+1):
            last_found = chr(ord(last_found)-1)
            continue

        n += last_found
        last_found = '9'
        line = line[i+1:]
    return int(n)


def find_joltage(input, digits):
    sum = 0
    for line in input:
        sum += get_max(line, digits)
    return sum


def solve() -> None:
    input = stdin.read().splitlines()
    print(find_joltage(input, 2))
    print(find_joltage(input, 12))


if __name__ == '__main__':
    solve()
