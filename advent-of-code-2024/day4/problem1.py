import re
from pprint import pprint

input_file = "./input.in"

with open(input_file, "r") as file:
    data = file.read().splitlines()


def findXMAS(arr):
    return sum([sent.count("XMAS") + sent.count("SAMX") for sent in arr])


def transpose(arr):
    m = len(arr)
    n = len(arr[0])
    brr = [""] * n
    for i in range(m):
        for j in range(n):
            brr[j] += arr[i][j]
    return brr


def staggerup(arr):
    m = len(arr)
    n = len(arr[0])
    brr = [""] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            brr[j - i] += arr[i][j]
    return brr


def staggerdown(arr):
    m = len(arr)
    n = len(arr[0])
    brr = [""] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            brr[j + i] += arr[i][j]
    return brr


print(
    findXMAS(data)
    + findXMAS(transpose(data))
    + findXMAS(staggerdown(data))
    + findXMAS(staggerup(data))
)
