a=list(map(int, input().split()))
n=len(a)
def trans(arr,n):
    l=0
    h=n-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==0:
            l=mid+1
        else:
            if mid==0 or (mid>0 and arr[mid-1]==0):
                return mid
            h=mid-1
    return -1
print(trans(a,n))                    