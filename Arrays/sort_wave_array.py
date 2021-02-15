a=list(map(int, input().split()))
n=len(a)
def sortwave(arr,n):


    for i in range(0,n,2):
        if i>0 and arr[i]<arr[i-1]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
        if i<n-1 and arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]    
    return arr
print(sortwave(a,n))            