import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())

b = input()
# print(b)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

movements = ""
skok = False
bb = b[1:]

for x in bb:
    if(skok):
        skok = False
    else:
        if x == "#":
            movements += "w"
            skok = False
        else:
            movements += "j"
            skok = True

print(movements)


# BSoD:

l = int(input())
b = input()

s = []
b = b[1:]
while b:
    c = b[0]
    s += {'#': 'w', ' ': 'j'}[c]
    if c == ' ':
        b = b[2:]
    else:
        b = b[1:]

print(*s, sep='')