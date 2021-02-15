arr=list(map(int, input().split()))
n=len(arr)
for i in range(n):
    arr[i]+=(arr[arr[i]]%n)*n
for i in range(n):
    arr[i]=arr[i]//n    
print(*arr)    