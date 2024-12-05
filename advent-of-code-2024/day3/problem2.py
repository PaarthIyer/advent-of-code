import re

input_file = "./input2.in"

with open(input_file, "r") as file:
    data = file.read()

valid_re = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"

all_matches = re.findall(valid_re, data)

to_mul = []

prev = "do()"

for kk in all_matches:
    if prev == "do()":
        if kk != "don't()":
            if kk != "do()":
                to_mul.append(kk)
        else:
            prev = kk
    if kk == "do()":
        prev = "do()"

# print(to_mul)


def get_nums(st):
    numm = st[4:-1].split(",")
    return int(numm[0]), int(numm[1])


num_ls = list(map(get_nums, to_mul))

summation = 0
for l in num_ls:
    summation += l[0] * l[1]

print(summation)
