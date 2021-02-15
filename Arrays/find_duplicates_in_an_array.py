arr=list(map(int, input().split()))
for i in arr:
    m=abs(i)
    if arr[m-1]<0:
        print(m)
    else:
        arr[m-1]*=-1    