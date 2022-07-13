import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()
t_2 = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if(t == t_2):
    print("ON TIME")
if(t < t_2):
    print("DELAYED")
if(t > t_2):
    print("EARLY")