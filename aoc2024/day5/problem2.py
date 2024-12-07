from pprint import pprint
from functools import cmp_to_key
from time import perf_counter

start_time = perf_counter()

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


def sorting_key(a, b):
    if a not in greater_than.keys() and b not in greater_than.keys():
        return 0
    if a in greater_than.keys() and b in greater_than[a]:
        return -1
    return 1


sort_worng = lambda x: sorted(x, key=cmp_to_key(sorting_key))


def valid_order(po):
    for i in range(1, len(po)):
        for j in range(i):
            if po[i] in greater_than.keys() and po[j] in greater_than[po[i]]:
                return False
    return True


final_sum = 0

for dd in print_list:
    if not valid_order(dd):
        dd = sort_worng(dd)
        final_sum += dd[len(dd) // 2]

end_time = perf_counter()

print(final_sum)
print("time taken : ", end_time - start_time)
