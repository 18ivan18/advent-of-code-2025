#!/usr/bin/env python3

from sys import stdin
from intervaltree import IntervalTree


def number_of_fresh_ingrediants(input):
    fresh, tree = 0, IntervalTree()
    r, prods = input
    r = r.splitlines()

    prods = prods.splitlines()
    for line in r:
        f, t = line.split('-')
        f, t = int(f), int(t)
        tree[f:t+1] = line

    for prod in map(int, prods):
        if (tree[prod]):
            fresh += 1

    tree.merge_overlaps()
    total = sum(i.end - i.begin for i in tree)
    print(fresh)
    print(total)


def solve() -> None:
    input = stdin.read().split('\n\n')
    number_of_fresh_ingrediants(input)


if __name__ == '__main__':
    solve()
