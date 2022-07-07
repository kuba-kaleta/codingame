i = input
s = int(i())
p = int(i())
l=[]
for i in range(p):
    l.append(int(input()))
l.sort(reverse=True)
print(sum(l)-(l[0]*s//100))

# tanakha:

s=int(input())
p=[int(input())for i in range(int(input()))]
print(sum(p)-max(p)*s//100)