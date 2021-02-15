ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))
def maxpath(ar1,ar2):
    res=sum1=sum2=0
    m=len(ar1)
    n=len(ar2)
    i=j=0
    while i<m and j<n:

        if ar1[i]<ar2[j]:
            sum1+=ar1[i]
            i+=1
        elif ar1[i]>ar2[j]:
            sum2+=ar1[j] 
            j+=1
        else:
            res+=max(sum1,sum2)
            sum1=sum2=0
            temp=i
            while i<m and ar1[i]==ar2[j]:
                sum1+=ar1[i]
                i+=1
            while j<n and ar1[temp]==ar2[j]:
                sum2+=ar2[j]
                j+=1
            res+=max(sum1,sum2)    
            sum1=sum2=0
    while i < m:
        sum1 += ar1[i]
        i += 1
    while j < n:
        sum2 += ar2[j]
        j += 1   
    res += max(sum1, sum2)        
    return [res,sum1,sum2]          
print(maxpath(ar1,ar2))            