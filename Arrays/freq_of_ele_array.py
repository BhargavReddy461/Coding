a=list(map(int, input().split()))
n=len(a)
for i in range(n):
    a[i]+=-1
for i in range(n):
    a[(a[i]%n)]+=n
for i in range(n):
    a[i]=a[i]//n  
print(*a)        