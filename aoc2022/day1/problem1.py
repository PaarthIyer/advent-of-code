input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.readlines()


dls = []
cur = []
for d in data:
    if d == "\n":
        dls.append(cur)
        cur = []
    else:
        cur.append(int(d[:-1]))
dls.append(cur)

cals = list(map(sum, dls))
cals.sort(reverse=True)
print(sum(cals[:3]))

## :1 for problem 1
