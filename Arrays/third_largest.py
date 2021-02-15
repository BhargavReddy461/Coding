a=list(map(int, input().split()))
n=len(a)
def third_largest(arr,n):
    a1=-99999
    a2=-99999
    a3=-99999
    for i in range(n):
        if arr[i]>a1:
            a3=a2
            a2=a1
            a1=arr[i]
        elif arr[i]>a2:
            a3=a2
            a2=arr[i]
        elif arr[i]>a3:
            a3=arr[i]        
    return a3
print(third_largest(a,n))

