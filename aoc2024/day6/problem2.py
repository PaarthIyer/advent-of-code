import numpy as np
import time
import os
from tqdm import tqdm


def print_grid(grid):
    os.system("clear" if os.name == "posix" else "cls")  # Clear the terminal
    for row in grid:
        print_row = []
        for rr in row:
            match rr:
                case -2:
                    print_row.append("O")
                case -1:
                    print_row.append("#")
                case 0:
                    print_row.append(".")
                case _:
                    print_row.append(str(rr))
        print(" ".join(print_row))


input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

# 0 - unvisited, -1 - obstruction, 1 - visited, 2,3,4,5 - states of guard
states = {"#": -1, ".": 0, "^": 1}

coords = []
state = 1


def init_coords(i, j):
    global coords
    coords = [i + 1, j + 1]
    return 1


grid = np.array(
    (
        [[-2] * (len(data[0]) + 2)]
        + [
            [-2] + [states[x] if x != "^" else init_coords(i, j) for j, x in enumerate(row)] + [-2]
            for i, row in enumerate(data)
        ]
        + [[-2] * (len(data[0]) + 2)]
    )
)

base_grid = grid.copy()
base_coords = coords.copy()


def move():
    global state, coords
    match state:
        case 1:
            next_step = [coords[0] - 1, coords[1]]
        case 2:
            next_step = [coords[0], coords[1] + 1]
        case 3:
            next_step = [coords[0] + 1, coords[1]]
        case 4:
            next_step = [coords[0], coords[1] - 1]
    next_cell = grid[*next_step]

    if next_cell == -1:
        state = (state % 4) + 1
    elif next_cell >= 0:
        coords = next_step
        grid[*coords] = state
    elif next_cell == -2:
        grid[*coords] = state
        return True

    return False


ended = False
while not ended:
    ended = move()
    # print_grid(grid)

cells_visited = np.vstack((grid > 0).nonzero()).T

# print("\n points traversed = ", cells_visited, "\n")

grid = base_grid.copy()


def islooping(grid):
    coords = base_coords
    state = 1

    while True:
        match state:
            case 1:
                next_step = [coords[0] - 1, coords[1]]
            case 2:
                next_step = [coords[0], coords[1] + 1]
            case 3:
                next_step = [coords[0] + 1, coords[1]]
            case 4:
                next_step = [coords[0], coords[1] - 1]
        next_cell = grid[*next_step]

        if next_cell == -1:
            state = (state % 4) + 1
        elif next_cell == 0:
            coords = next_step
            grid[*coords] = state
        elif next_cell == -2:
            grid[*coords] = state
            return False
        elif next_cell == state:
            return True
        else:
            coords = next_step
            grid[*coords] = state


valid_places = cells_visited[~np.all(a=cells_visited == np.array(base_coords), axis=1)]

ff = 0
for pos in tqdm(valid_places):
    inp = base_grid.copy()
    inp[*pos] = -1
    looping = islooping(inp)
    if looping:
        ff += 1

print("\nAnswer : ", ff, "\n")
