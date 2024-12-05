import re
import time

input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read()

valid_re = r"mul\(\d+,\d+\)"


def get_nums(st):
    numm = st[4:-1].split(",")
    return int(numm[0]), int(numm[1])


a = time.perf_counter()
all_matches = re.findall(valid_re, data)
num_ls = list(map(get_nums, all_matches))

summation = 0
for l in num_ls:
    summation += l[0] * l[1]

b = time.perf_counter()

print(summation)
print(b - a)
