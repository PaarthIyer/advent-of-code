from time import perf_counter_ns
import numpy as np

input_file = "./test_input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

nodes = {}

for i, line in enumerate(data):
    for j, cell in enumerate(line):
        if cell != ".":
            nodes.setdefault(cell, []).append([i, j])

nodes = {key: np.array(value) for key, value in nodes.items()}


def twodarray(arr):
    return list(tuple(map(int, x)) for x in arr)


def get_anitnodes(coords_array, m, n) -> set:
    valid_antinodes = set()
    for i, a in enumerate(coords_array[:-1]):
        mask1 = [True]
        mask2 = [True]
        b_array = coords_array[i + 1 :]

        temp1 = (a - b_array) + a
        temp2 = (b_array - a) + b_array

        mask1 = (0 <= temp1[:, 0]) & (temp1[:, 0] < m) & (0 <= temp1[:, 1]) & (temp1[:, 1] < n)
        mask2 = (0 <= temp2[:, 0]) & (temp2[:, 0] < m) & (0 <= temp2[:, 1]) & (temp2[:, 1] < n)

        valid_antinodes.update(twodarray(temp1[mask1]))
        valid_antinodes.update(twodarray(temp2[mask2]))

    return valid_antinodes


m = len(data)
n = len(data[0])

antinodes = set()

for node in nodes:
    antinodes.update(get_anitnodes(nodes[node], m, n))

print(len(antinodes))
print(sorted(list(antinodes)))
