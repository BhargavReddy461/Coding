a=list(map(int,input().split()))
n=len(a)
def maxloot(arr,n):
    if n==0:
        return 0
    v1=arr[0]
    if n==1:
        return v1
    v2=max(arr[0],arr[1])
    if n==2:
        return v2
    max_val=0
    for i in range(2,n):
        max_val=max(arr[i]+v1,v2)
        v1=v2
        v2=max_val
    return max_val 
print(maxloot(a,n))                  