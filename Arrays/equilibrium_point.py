a=list(map(int, input().split()))
b=sum(a)
c=0
for i in range(len(a)):
    if c==((b-a[i])/2):
        print(i)
        break
    c+=a[i]
else:
    print(-1)    

    