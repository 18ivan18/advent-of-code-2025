#!/usr/bin/env python3

from functools import reduce
from sys import stdin
import operator


def col_to_num(col):
    n = 0
    for c in col:
        if (c.isdigit()):
            n = n*10+int(c)
    return n


def apply_sign(nums, sign):
    if (sign == '+'):
        return sum(nums)
    if (sign == '*'):
        return reduce(operator.mul, nums)
    raise KeyError()


def cephalopod_math_right_to_left_column(input):
    nums, signs = input[:-1], input[-1].split()
    ans = []
    for i in range(len(nums[0])):
        ans.append([])
        for j in range(len(nums)):
            ans[i].append(nums[j][i])
    cols, i = [[]], 0
    for col in ans:
        if (all(map(lambda x: x == ' ', col))):
            i += 1
            cols.append([])
            continue
        n = col_to_num(col)
        cols[i].append(n)

    final = []
    for i, nums in enumerate(cols):
        final.append(apply_sign(nums, signs[i]))
    return sum(final)


def cephalopod_math(input):
    nums = input[:-1]
    signs = input[-1].split()
    ans = {}
    for line in nums:
        for i, n in enumerate(map(int, line.split())):
            if (signs[i] == '*'):
                if (i not in ans):
                    ans[i] = 1
                ans[i] *= n
            if (signs[i] == '+'):
                if (i not in ans):
                    ans[i] = 0
                ans[i] += n
    return sum(ans.values())


def solve() -> None:
    input = stdin.read().splitlines()
    print(cephalopod_math(input))
    print(cephalopod_math_right_to_left_column(input))


if __name__ == '__main__':
    solve()
