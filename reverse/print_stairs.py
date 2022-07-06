import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

str1 = ""

for x in range(0, n):
    str1 = ""
    for y in range(1, n-x + 1):
        str1 += str(y)
    print((x)*"+" + str1)  # print(" ", end="")
    