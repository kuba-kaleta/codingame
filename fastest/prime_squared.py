import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n%i) == 0:
                return False
        return True
    else:
        return True

n = int(input())
if(is_prime(n)):
    print(n**2)
else:
    m = str(n**2)
    sum = 0
    for x in m:
        sum += int(x)
    print(sum)