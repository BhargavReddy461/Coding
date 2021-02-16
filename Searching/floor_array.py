a=list(map(int, input().split()))
n=len(a)
x=int(input())
def floor(arr,n,x):
    l=0
    h=n-1
    while l<=h:
        mid =(l+h)//2
        if arr[mid]>x:
            h=mid-1
        else:
            if mid<n-1 and arr[mid+1]>x:
                return mid
            l=mid+1
    return -1
print(floor(a,n,x))                     
