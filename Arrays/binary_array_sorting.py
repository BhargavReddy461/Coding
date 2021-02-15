n=int(input())
a=list(map(int, input().split()))
c=0
for i in a:
    if i==0:
        c+=1
b=[0]*c + [1]*(n-c)
print(*b)        
