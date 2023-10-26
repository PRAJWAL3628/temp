#Assignment no-3

import numpy as np
def floyds(b, n, m):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (b[i][k] * b[k][j] != 0) and (i != j):
                    if (b[i][k] + b[k][j] < b[i][j]) or (b[i][j] == 0):
                        b[i][j] = b[i][k] + b[k][j]
    for i in range(n):
        print("\nMinimum amount With Respect to office: ", i)
        for j in range(n):
            print(b[i][j], end="\t")

n=int(input("Enter the no of offices: "))
m=int(input("Enter the no of telephone lines: "))
            
b = np.zeros((n,m), dtype=int)

for i in range(m):
        x=int(input("Enter the start vertex: "))
        y=int(input("Enter the end vertex: "))
        z=int(input("Enter the amount: "))

        b[x][y]=z

floyds(b, n, m)