n=int(input())
p=print
l=[]
for i in range(1,n):
    if(n%i == 0):
        l.append(i)
s = 0
for x in l:
    s += int(x)
if(s == n):
    p("perfect")
else:
    p("not perfect")