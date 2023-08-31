import numpy as np
def solve():
    for m in range(n-1):
        for i in range(n -1-m):
            c = numbers[i + 1+m][m] / numbers[m][m]
            numbers[i + 1][0] = 0
            for v in range(n-m):
                numbers[i + 1+m][v + 1] -= numbers[m][v + 1] * c
    print(numbers)

n = float(input("amount of variables"))
variabls = np.zeros((n))
numbers = np.zeros((n,n+1))
length = len(numbers)*len(numbers[0])
for i in range(len(numbers)):
    for c in range(len(numbers[0])):
        numbers[i][c]=float(input("input value"))

solve()
def solve2():
    for i in range(n-1):
        c = numbers[i][i+1] / numbers[i+1][i+1]
