import numpy as np
class GausAlgo():
    def __init__(self):
        n = int(input("amount of variables"))
        self.variabls = np.zeros(n)
        numbers = np.zeros((n, n + 1))
        for i in range(len(numbers)):
            for c in range(len(numbers[0])):
                numbers[i][c] = float(input("input value"))
        self.solve(numbers,n)
        print(self.variabls)

    def solve(self,numbers,n):
        for m in range(n - 1):
            for i in range(n - 1 - m):
                c = numbers[i + 1 + m][m] / numbers[m][m]
                numbers[i + 1][0] = 0
                for v in range(n - m):
                    numbers[i + 1 + m][v + 1] -= numbers[m][v + 1] * c
        print(numbers)
        for m in range(n - 1):
            for i in range(n - 1 - m):
                c = numbers[i][n - 1 - m] / numbers[n - 1 - m][n - 1 - m]
                numbers[i][n - 1 - m] = 0
                numbers[i][n] -= numbers[n - 1 - m][n] * c
        print(numbers)
        self.solve2(numbers,n)

    def solve2(self,numbers,n):
        for i in range(n):
            self.variabls[i] = numbers[i][n] / numbers[i][i]
Solver = GausAlgo()

