a=list(map(int,input().split()))
def max2(a):
    first=second=-999999
    for i in a:
        if i>first:
            second=first
            first =i
        elif i<first and i>second:
            second=i
    return [first, second]  
print(max2(a))              