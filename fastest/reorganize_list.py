import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = {}
for i in range(n):
    a, b, c = [int(j) for j in input().split()]
    l[a*b + c] = (str(a) + " " + str(b) + " " + str(c))

for w, t in sorted(l.items(), key=lambda x: x[0]):
    print(t)
