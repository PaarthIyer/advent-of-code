from time import perf_counter_ns

start_time = perf_counter_ns()
input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

temp = [x.split() for x in data]
targets = [int(x[0][:-1]) for x in temp]
nums = [[int(y) for y in x[1:]] for x in temp]


def valid_ops(target, nums):
    if len(nums) == 1:
        return target == nums[0]
    if target % nums[-1] == 0:

        if valid_ops(target // nums[-1], nums[:-1]):
            return True
    if target < nums[-1]:
        return False
    else:
        return valid_ops(target - nums[-1], nums[:-1])


total_possible = 0
for i in range(len(data)):
    if valid_ops(targets[i], nums[i]):
        total_possible += targets[i]

end_time = perf_counter_ns()

print("Time taken to execute:", (end_time - start_time) / 1000, "us")
print("Answer:", total_possible)
