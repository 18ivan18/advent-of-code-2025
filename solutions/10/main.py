#!/usr/bin/env python3

from sys import stdin
from itertools import combinations
from z3 import Optimize, Int, sat, Sum


def fewest_presses_to_configure(positions, button_wirings):
    bitmap = [x == '#' for x in positions]
    buttons_size = len(button_wirings)
    for n in range(buttons_size):
        for c in combinations(button_wirings, n):
            bm = [False]*len(bitmap)
            for option in c:
                option = option[1:-1]
                indexes = [int(x) for x in option.split(',')]
                for i in indexes:
                    bm[i] = not bm[i]
            if (bitmap == bm):
                return n
    raise Exception("Should have solution")


def fewest_presses_to_configure_joltage(button_wirings, joltage):
    joltage = [int(x) for x in joltage.split(',')]
    l = len(joltage)
    vectors = []
    solver = Optimize()
    for button in button_wirings:
        button = button[1:-1]
        v = [0]*l
        for i in button.split(','):
            v[int(i)] = 1
        vectors.append(v)
    variables = [Int(f"x{i}") for i in range(len(vectors))]
    for v in variables:
        solver.add(v >= 0)
    for j in range(l):
        solver.add(Sum([vectors[i][j] * variables[i]
                   for i in range(len(variables))]) == joltage[j])
    solver.minimize(Sum(variables))

    if (solver.check() == sat):
        m = solver.model()
        total = sum(m[v].as_long() for v in variables)
        return total
    raise Exception("Should have solution")


def fewest_presses(lines):
    presses, joltage_presses = 0, 0
    for line in lines:
        positions, *button_wirings, joltage = line.split(' ')
        presses += fewest_presses_to_configure(positions[1:-1], button_wirings)
        joltage_presses += fewest_presses_to_configure_joltage(
            button_wirings, joltage[1:-1])

    print(presses)
    print(joltage_presses)


def solve() -> None:
    input = stdin.read().splitlines()
    fewest_presses(input)


if __name__ == '__main__':
    solve()
