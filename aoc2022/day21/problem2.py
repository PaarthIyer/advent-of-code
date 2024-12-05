input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

monkey_name_ls = [x[:4] for x in data]
monkey_name_lut = {k: i for i, k in enumerate(monkey_name_ls)}

monkey_nums = {}

for dat in data:
    if len(dat[6:]) < 9:
        monkey_nums[dat[:4]] = int(dat[6:])


def calc_sign(sg, x, y):
    match sg:
        case "+":
            return x + y
        case "-":
            return x - y
        case "/":
            return x // y
        case "*":
            return x * y
        case "=":
            return x == y


def calc(monkey_name):
    if monkey_name in monkey_nums.keys():
        return monkey_nums[monkey_name]

    idx = monkey_name_lut[monkey_name]
    mn1 = data[idx][6:10]
    mn2 = data[idx][13:17]
    sign = data[idx][11] if monkey_name != "root" else "="

    xx = calc_sign(sign, calc(mn1), calc(mn2))

    # print(mn1, sign, mn2, "=", xx)

    monkey_nums[monkey_name] = xx

    return xx


# print(monkey_nums)
print(calc("root"))
