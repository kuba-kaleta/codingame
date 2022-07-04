import re

s = "1+2*3"
a, *d = re.findall('\d+', s)
o = re.findall('[^\d]', s)

for i,j in zip(o, d):
    a = str(eval(a+i+j))

print(a)