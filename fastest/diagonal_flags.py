import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for x in range(2*n+3):
    for y in range(2*n+3):
        if x == 0 or y == 0 or x == 2*n+2 or y == 2*n+2:
            print("#", end='')
        elif x == y or x == 2*n+2-y:
            print("X", end='')
        else:
            print(' ', end='')
    print("")