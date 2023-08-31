import numpy as np
n = 3
numbers = np.zeros((n,n+1))
length = len(numbers)*len(numbers[0])
for i in range(len(numbers)):
    for c in range(len(numbers[0])):
        numbers[i][c]=float(input("input value"))

def solve():
    for m in range(n-1):
        for i in range(n -1-m):
            c = numbers[i + 1+m][m] / numbers[m][m]
            numbers[i + 1][0] = 0
            for v in range(n-m):
                numbers[i + 1+m][v + 1] -= numbers[m][v + 1] * c
    print(numbers)
solve()