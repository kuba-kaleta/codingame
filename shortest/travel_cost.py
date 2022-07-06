import math
e=float(input())
f=float(input())
p=float(input())
d=float(input())
l=d/e
if(l>f):print(round(math.ceil((l-f)*p*100)/100, 2))
else: print(0.00)