#!/usr/bin/env python3

from sys import stdin


# def dfs(adj_matrix, x, visited, to, must_include):
#     if x == to and visited & must_include == must_include:
#         return 1
#     visited.add(x)

#     paths = 0
#     for adj in adj_matrix[x]:
#         if (adj not in visited):
#             paths += dfs(adj_matrix, adj, visited, to, must_include)
#     visited.remove(x)
#     return paths


def get_all_paths(input, fro, to):
    adj = {}
    for line in input:
        f, t = line.split(': ')
        adj[f] = set(t.split(' '))
    adj['out'] = []
    # visited = set()
    # return dfs(adj, fro, visited, to, must_include)
    reachable = {}
    new_reachable = {node: (1 if node == to else 0) for node in adj}

    while new_reachable != reachable:
        reachable = new_reachable
        new_reachable = {
            node: (1 if node == to
                   else sum(reachable[child] for child in adj[node]))
            for node in reachable
        }

    return new_reachable[fro]


def solve() -> None:
    input = stdin.read().splitlines()
    print(get_all_paths(input, 'you', 'out'))
    print(get_all_paths(input, 'svr', 'fft')
          * get_all_paths(input, 'fft', 'dac')
          * get_all_paths(input, 'dac', 'out')
          + get_all_paths(input, 'svr', 'dac')
          * get_all_paths(input, 'dac', 'fft')
          * get_all_paths(input, 'fft', 'out'))


if __name__ == '__main__':
    solve()
