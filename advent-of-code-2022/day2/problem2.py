from pprint import pprint

input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().split("\n")

plays = list(map(lambda x: x.split(), data))

shape_scores = {"A": 1, "B": 2, "C": 3}

lose = {"A": "C", "B": "A", "C": "B"}
eql = {x: x for x in shape_scores}
win = {y: x for x, y in lose.items()}

res = {"X": lose, "Y": eql, "Z": win}

plays_actual = list(map(lambda x: [x[0], res[x[1]][x[0]], x[1]], plays))


def calc_scores(plays_ac):
    score = 0

    for play in plays_ac:
        score += shape_scores[play[1]]
        score += (play[2] == "Y") * 3 + (play[2] == "Z") * 6

    return score


print(calc_scores(plays_actual))
