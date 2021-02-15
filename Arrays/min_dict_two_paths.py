a=list(map(int, input().split()))
x=int(input())
y=int(input())
n=len(a)
def mindiff(a,n,x,y):
    mindiff=99999
    i=0
    p=-1
    for i in range(n):
        if a[i]==x or a[i]==y:
            if p!=-1 and a[p]!=a[i]:
                mindiff=min(mindiff,i-p)
            p=i
    if mindiff==99999:
        return -1
    return mindiff
print(mindiff(a,n,x,y))                   