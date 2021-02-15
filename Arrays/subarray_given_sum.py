arr=list(map(int, input().split()))
n=len(arr)
s=int(input())
def subsum(arr,n,s):
    a=0
    i=0
    min=0
    while i<n:
        if a<s:
            a+=arr[i]
            i+=1
        elif a==s:
            return [min,i-1]
        elif a>s:
            a=a-arr[min]
            min+=1
    return -1
print(subsum(arr,n,s))                

