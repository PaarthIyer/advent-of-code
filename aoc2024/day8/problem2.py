from time import perf_counter_ns
import numpy as np


##########################
def get_antinode(coords_array, m, n) -> set:
    valid_antinodes = set()
    for i, a in enumerate(coords_array[:-1]):
        b_array = coords_array[i + 1 :]
        mult = 0

        while True:
            temp1 = (a - b_array) * mult + a
            temp2 = (b_array - a) * mult + b_array
            potential = np.concatenate([temp1, temp2], 0)

            mask = (
                (potential[:, 0] >= 0)
                & (potential[:, 0] < m)
                & (potential[:, 1] >= 0)
                & (potential[:, 1] < n)
            )

            if not np.any(mask):
                break

            valid_antinodes.update(map(tuple, potential[mask]))
            mult += 1

    return valid_antinodes


##########################
def main():
    start_time = perf_counter_ns()

    input_file = "./input.in"

    with open(input_file, "r") as file:
        data = file.read().splitlines()

    nodes = {}
    for i, line in enumerate(data):
        for j, cell in enumerate(line):
            if cell != ".":
                nodes.setdefault(cell, []).append([i, j])

    nodes = {key: np.array(value) for key, value in nodes.items()}

    m = len(data)
    n = len(data[0])

    antinodes = set()

    for node in nodes:
        antinodes.update(get_antinode(nodes[node], m, n))

    end_time = perf_counter_ns()

    print(len(antinodes))
    print("time taken = ", (end_time - start_time) / 1000, "us")


##########################

if __name__ == "__main__":
    main()
