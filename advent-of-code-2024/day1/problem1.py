import sys

# Read all input from stdin
data = sys.stdin.read()
print("Input data read")

data_split = [a.split() for a in data.split("\n")[:-1]]
l1 = [int(x) for x, _ in data_split]
l2 = [int(y) for _, y in data_split]

l1.sort()
l2.sort()

print(sum([abs(a - b) for a,b in zip(l1, l2)]))