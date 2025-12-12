#!/usr/bin/env python3

from sys import stdin


class Distance():
    def __init__(self, from_index, to_index, distance):
        self.from_index = from_index
        self.to_index = to_index
        self.distance = distance

    def __str__(self):
        return f"{self.from_index=},{self.to_index=},{self.distance=},"


def dist(p, q):
    return (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2


def largest_circuits(input, iterations=10):
    input = [[int(line.split(',')[0]), int(line.split(',')[1]),
              int(line.split(',')[2])] for line in input]
    distances = []
    for i, p in enumerate(input):
        for j, q in enumerate(input[i+1:]):
            distances.append(Distance(i, i+j+1, dist(p, q)))
    distances.sort(key=lambda d: d.distance)
    clusters = []
    for i in range(iterations):
        distance = distances[i]
        for cluster in clusters:
            if (distance.from_index in cluster or distance.to_index in cluster):
                cluster.add(distance.from_index)
                cluster.add(distance.to_index)
                break
        else:
            clusters.append(set([distance.from_index, distance.to_index]))
    combined = True
    while (combined == True):
        combined = False
        i = 0
        while (i < len(clusters)):
            j = i+1
            while (j < len(clusters)):
                if (len(clusters[i] & clusters[j]) > 0):
                    clusters[i] = clusters[i] | clusters[j]
                    clusters = clusters[:j]+clusters[j+1:]
                    combined = True
                else:
                    j += 1
            i += 1
    clusters.sort(key=lambda c: -len(c))
    return (len(clusters[0])*len(clusters[1])*len(clusters[2]))


def combine_until_one_is_left(input):
    input = [[int(line.split(',')[0]), int(line.split(',')[1]),
              int(line.split(',')[2])] for line in input]
    distances = []
    used, all = set(), len(input)
    for i, p in enumerate(input):
        for j, q in enumerate(input[i+1:]):
            distances.append(Distance(i, i+j+1, dist(p, q)))
    distances.sort(key=lambda d: d.distance)
    clusters = []
    i = 0
    distance = None
    while (all != len(used) or len(clusters) != 1):
        distance = distances[i]
        i += 1
        used.add(distance.from_index)
        used.add(distance.to_index)

        for cluster in clusters:
            if (distance.from_index in cluster or distance.to_index in cluster):
                cluster.add(distance.from_index)
                cluster.add(distance.to_index)
                break
        else:
            clusters.append(set([distance.from_index, distance.to_index]))
        combined = True
        while (combined == True):
            combined = False
            c_len = 0
            while (c_len < len(clusters)):
                j = c_len+1
                while (j < len(clusters)):
                    if (len(clusters[c_len] & clusters[j]) > 0):
                        clusters[c_len] = clusters[c_len] | clusters[j]
                        clusters = clusters[:j]+clusters[j+1:]
                        combined = True
                    else:
                        j += 1
                c_len += 1

    return (input[distance.from_index][0]*input[distance.to_index][0])


def solve() -> None:
    input = stdin.read().splitlines()
    # print(largest_circuits(input, 10))
    print(largest_circuits(input, 1000))
    print(combine_until_one_is_left(input))


if __name__ == '__main__':
    solve()
