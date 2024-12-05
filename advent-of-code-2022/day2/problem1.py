from itertools import permutations
from pprint import pprint

input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().split("\n")

shape_scores = {"A": 1, "B": 2, "C": 3}
beats = {"A": "C", "B": "A", "C": "B"}

plays = list(map(lambda x: x.split(), data))


def calc_scores(plays_ac, dec_key):
    dec_map = {"X": dec_key[0], "Y": dec_key[1], "Z": dec_key[2]}
    score = 0

    for play in plays_ac:
        pl = dec_map[play[1]]
        score += shape_scores[pl]
        score += (play[0] == pl) * 3 + (play[0] == beats[pl]) * 6

    return score


perms = list(permutations(["A", "B", "C"]))
score_finals = list(map(lambda x: calc_scores(plays, x), perms))

pprint(list(zip(perms, score_finals)))
