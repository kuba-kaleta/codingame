import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
cows = str(input())
result = ""
for i in range(n):
    x = input()
    k = 0
    result = "Valid"
    for y in str(x):
        if(cows[k] == x[k]):
            result = "Invalid"
        k += 1
    print(result)
            

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# NglQ:

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = input()
for i in range(n):
    x = input()
    print("Invalid" if any([v==x[i] for i,v in enumerate(c)]) else "Valid")
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("Valid or Invalid")
