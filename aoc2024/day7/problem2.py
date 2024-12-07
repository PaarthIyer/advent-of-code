from time import perf_counter_ns

start_time = perf_counter_ns()
input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

temp = [x.split() for x in data]
targets = [int(x[0][:-1]) for x in temp]
nums = [[int(y) for y in x[1:]] for x in temp]


def ends_with(a, b):
    return str(a).endswith(str(b))


def trim(a, b):
    return int(str(a)[: -len(str(b))])


def valid_ops(target, nums):
    if len(nums) == 1:
        return target == nums[0]

    last_num = nums[-1]
    remaining_nums = nums[:-1]

    if target % last_num == 0 and valid_ops(target // last_num, remaining_nums):
        return True

    if target > last_num and valid_ops(target - last_num, remaining_nums):
        return True

    if (
        target > last_num
        and ends_with(target, last_num)
        and valid_ops(trim(target, last_num), remaining_nums)
    ):
        return True

    return False


total_possible = 0
for i in range(len(data)):
    if valid_ops(targets[i], nums[i]):
        total_possible += targets[i]
end_time = perf_counter_ns()

print(total_possible)
print("time taken = ", (end_time - start_time) / 1000, "us")
