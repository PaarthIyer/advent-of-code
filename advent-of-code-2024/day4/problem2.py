from pprint import pprint

input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()


def findMAS(arr):
    m = len(arr)
    n = len(arr[0])

    count = 0
    valis = {"MS", "SM"}

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if arr[i][j] != "A":
                continue
            s1 = arr[i - 1][j - 1] + arr[i + 1][j + 1]
            s2 = arr[i - 1][j + 1] + arr[i + 1][j - 1]
            if (s1 in valis) and (s2 in valis):
                count += 1

    return count


print(findMAS(data))
