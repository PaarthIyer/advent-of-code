input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

total_priority = 0

for i in range(0, len(data), 3):
    s1 = data[i]
    s2, s3 = set(data[i + 1]), set(data[i + 2])
    common = s2 & s3

    for k in s1:
        if k in common:
            total_priority += ord(k) - (96 if ord(k) > 91 else 38)
            break

print(total_priority)
