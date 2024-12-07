import numpy as np
import time
import os


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
                case 9:
                    print_row.append("X")
        print(" ".join(print_row))


input_file = "./test_input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

# 0 - unvisited, -1 - obstruction, 1 - visited, 2,3,4,5 - states of guard
states = {"#": -1, ".": 0, "^": 1}

coords = []
state = 1


def init_coords(i, j):
    global coords
    coords = [i + 1, j + 1]
    return 9


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
    next_state = grid[*next_step]

    if next_state == -1:
        state = (state % 4) + 1
    elif next_state == 0 or next_state == 9:
        coords = next_step
        grid[*coords] = 9
    elif next_state == -2:
        grid[*coords] = 9
        return True

    return False


ended = False
while not ended:
    ended = move()
    print_grid(grid)

print("\n points traversed = ", np.sum(grid == 9), "\n")
