arr=list(map(int,input().split()))
n=len(arr)
d=int(input())
def gcd(a,b):
    if b == 0: 
        return a
    else: 
        return gcd(b, a % b)
def arrayRotate(arr,d,n):
    d=d%n
    g=gcd(n,d)
    for i in range(g):
        temp=arr[i]
        j=i
        while 1:
            k=j+d
            if k>=n:
                k=k-n
            if k==i:
                break
            arr[j]=arr[k]    
            j=k
        arr[j]=temp
    return arr        
print(arrayRotate(arr,d,n))



