import sys
import math

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n%i) == 0:
                return False
        return True
    else:
        return False

n = int(input())
#print(n)
res = 0
for x in range(n + 1):
    if is_prime(x):
        r = 0
        for y in str(x):
            r += int(y)
        if r%2 == 0:
            res += x

print(res)