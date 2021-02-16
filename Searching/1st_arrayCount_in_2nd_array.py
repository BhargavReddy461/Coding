a=list(map(int, input().split()))
b=list(map(int, input().split()))
m=len(a)
n=len(b)
def bin(arr,n,x):
    l=0
    h=n-1
    while l<=h:
        mid= (l+h)//2
        if arr[mid]<=x:
            l=mid+1
        else:
            h=mid-1
    return h
def countele(arr1,arr2,m,n):
    arr2.sort()
    for i in range(m):
        index=bin(arr2,n,arr1[i])
        arr1[i]=index+1
    return arr1
print(countele(a,b,m,n))                       
