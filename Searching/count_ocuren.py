from collections import Counter
a=list(map(int, input().split()))
k=int(input())
n=len(a)
x=n//k
a=Counter(a)
c=0
for i in a:
    if a[i]>x:
        c+=1
print(c)        