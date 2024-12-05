input_file = "./input.in"

with open(input_file, 'r') as file:
    data = file.read()

reports = [[int(x) for x in d.split()] for d in data.split("\n")][:1000]

def is_sorted(ls):
    return (sorted(ls) == ls) or (sorted(ls, reverse=True) == ls)

def valid_report(report):     
    if not is_sorted(report): return False
    for i in range(len(report)- 1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

valid_bool = list(map(valid_report, reports))

print(sum(valid_bool))