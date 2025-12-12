#!/usr/bin/env python3

from sys import stdin
from intervaltree import Interval, IntervalTree


class Range:
    def __init__(self, f, t):
        self.f = f
        self.t = t
        self.r = range(self.f, self.t+1)

    def contains(self, num):
        return num in self.r

    def extend(self, other_f, other_t):
        if (self.f >= other_f and self.f <= other_t and self.t >= other_t):
            self.f = other_f
            self.r = range(self.f, self.t+1)
            # print('case1')
            return True
        if (self.f <= other_f and self.t >= other_f and self.t <= other_t):
            self.t = other_t
            self.r = range(self.f, self.t+1)
            # print('case2')
            return True
        if (self.f >= other_f and self.t <= other_t):
            self.f = other_f
            self.t = other_t
            self.r = range(self.f, self.t+1)
            # print('case3')
            return True
        if (self.f <= other_f and self.t >= other_t):
            return True
        return False

    def __str__(self):
        return f"{self.f}-{self.t}"


def merge(ranges, i):
    r = ranges[i]
    i += 1
    while (i < len(ranges)):
        if (r.extend(ranges[i].f, ranges[i].t)):
            ranges = ranges[:i]+ranges[i+1:]
        else:
            i += 1
    return ranges


def number_of_fresh_ingrediants(input):
    fresh = 0
    ranges = []
    r, prods = input
    r = r.splitlines()
    prods = prods.splitlines()
    asd = 0
    for line in r:
        asd += 1
        # print(asd)
        f, t = line.split('-')
        f, t = int(f), int(t)
        extended = False
        for i, possible_range in enumerate(ranges):
            if (possible_range.extend(f, t)):
                # print('etending', possible_range, f, t)
                extended = True
                ranges = merge(ranges, i)
                break
        if (not extended):
            # print('appending', f, t)
            ranges.append(Range(f, t+1))

    all_fresh = 0
    for possible_range in ranges:
        # print(possible_range)
        all_fresh = all_fresh + possible_range.t-possible_range.f

    for p in prods:
        p = int(p)
        for possible_range in ranges:
            if (possible_range.contains(p)):
                fresh += 1
                break

    print(fresh)
    print(all_fresh)


def solve() -> None:
    input = stdin.read().split('\n\n')
    number_of_fresh_ingrediants(input)


if __name__ == '__main__':
    solve()


# 332998283036739
# 332998283036769
