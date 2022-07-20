import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
res = 0
n, q = [int(i) for i in input().split()]
mon = []
for x in range(0, n):
    mon.append(0)
for i in range(q):
    l, r = [int(j) for j in input().split()]
    for x in range(l,r):
        if mon[x] == 0:
             mon[x] = 1
        if mon[x] == 1:
             mon[x] = 0

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(mon.count(0))