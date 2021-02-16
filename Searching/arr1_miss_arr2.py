a=list(map(int, input().split()))
b=list(map(int, input().split()))
n=len(b)
def miss(arr1,arr2,n):
    l=0
    h=n-1
    index=n
    while l<=h:
        mid = (l+h)//2
        if arr1[mid]==arr2[mid]:
            l=mid+1
        else:
            index=mid
            h=mid-1
    return index        
print(miss(a,b,n))            


