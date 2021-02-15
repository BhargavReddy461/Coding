a=list(map(int, input().split()))
n=len(a)
def max_sum(a,n):
    max_so_far=0
    curr_max=0
    for i in a:
        curr_max=max(i,curr_max+i)
        max_so_far=max(max_so_far, curr_max)
    return max_so_far
print(max_sum(a,n))        