input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()

total_priority = 0

for sack in data:
    l = len(sack) // 2
    pkt1 = set(sack[:l])

    for k in sack[l:]:
        if k in pkt1:
            total_priority += ord(k) - (96 if ord(k) > 91 else 38)
            break

print(total_priority)
