from pprint import pprint

input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

split_at = data.index("")

rules_raw = data[:split_at]
rules = [list(map(int, x.split("|"))) for x in rules_raw]

print_list = data[split_at + 1 :]
print_list = [list(map(int, x.split(","))) for x in print_list]

greater_than = {}

for rr in rules:
    if rr[0] not in greater_than.keys():
        greater_than[rr[0]] = set()
    greater_than[rr[0]].add(rr[1])


def valid_order(po):
    for i in range(1, len(po)):
        for j in range(i):
            if po[i] in greater_than.keys() and po[j] in greater_than[po[i]]:
                return False
    return True


final_sum = 0

for dd in print_list:
    if valid_order(dd):
        final_sum += dd[len(dd) // 2]

print(final_sum)
