a=list(map(int, input().split()))
x=int(input())
n=len(a)
a.sort()
def closesum(arr,n,x):
    closesum=99999
    for i in range(n-2):
        ptr1=i+1
        ptr2=n-1

        while ptr1<ptr2:
            summ=arr[i]+arr[ptr1]+arr[ptr2]
            if abs(x-summ)<abs(x-closesum):
                closesum=summ
            if summ>x:
                ptr2-=1
            else:
                ptr1+=1
    return closesum
print(closesum(a,n,x))                        