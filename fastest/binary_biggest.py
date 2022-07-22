import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
b = ''
a = bin(n).count('1')
c = bin(n).count('0')
for x in range(0, a):
    b += '1'
for x in range (1, c):
    b += '0'
#print(b)
print(int(b, 2))
