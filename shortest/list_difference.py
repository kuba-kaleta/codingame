i=input
i()
a=sorted(map(int,i().split()))
print(a[-1]-a[0])

# Romisi:

l=input
l()
n=[int(i)for i in l().split()]
print(max(n)-min(n))