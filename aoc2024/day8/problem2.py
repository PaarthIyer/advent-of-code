from time import perf_counter_ns
import numpy as np

input_file = "./input.in"

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
    mult = 0
    for i, a in enumerate(coords_array[:-1]):
        mask = True
        b_array = coords_array[i + 1 :]

        while np.any(mask):
            temp1 = (a - b_array) * mult + a
            temp2 = (b_array - a) * mult + b_array
            potential = np.vstack([temp1, temp2])

            mask = np.all((0 <= potential) & (potential < [m, n]), axis=1)

            valid_antinodes.update(twodarray(potential[mask]))
            mult += 1
        mult = 0

    return valid_antinodes


m = len(data)
n = len(data[0])

antinodes = set()

for node in nodes:
    antinodes.update(get_anitnodes(nodes[node], m, n))

print(len(antinodes))
