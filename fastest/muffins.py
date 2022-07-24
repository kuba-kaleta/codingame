import sys
import math

n, m, r, t = [int(i) for i in input().split()]

for i in range(m):

    if (t == i):
        if m >= n:
            print("HAPPY")
        else:
            print("NOT HAPPY")
    m -= r