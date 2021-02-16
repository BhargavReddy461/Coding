a=list(map(int, input().split()))
n=len(a)

def majindex(arr,n):
    maj_index=0
    count=1
    for i in range(n):
        if arr[maj_index]==arr[i]:
            count+=1
        else:
            count-=1
        if count==0:
            maj_index=i
            count=1
    return arr[maj_index]
if a.count(majindex(a,n))>n/2:
    print(majindex(a,n))
else:
    print(-1)    
        
                 