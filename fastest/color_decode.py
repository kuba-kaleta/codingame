import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

color = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


for i in range(len(color)//2):
    print(int(color[2*i+1:2*i+3], 16))