import sys

# Read all input from stdin
data = sys.stdin.read()
print("Input data read")

data_split = [a.split() for a in data.split("\n")[:-1]]
l1 = [int(x) for x, _ in data_split]
l2 = [int(y) for _, y in data_split]

l1.sort()
l2.sort()

sim = 0
for x in l1:
    sim += x * sum([x == y for y in l2])
    
print(sim)