a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=len(a)
n=len(b)
a=set(a)
b=set(b)
a=a.intersection(b)
print(a)