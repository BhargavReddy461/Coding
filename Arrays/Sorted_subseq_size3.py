a=list(map(int, input().split()))
def subseq3(arr):
    if len(arr)<3:
        return -1
    min_sum=arr[0]
    seq=1
    max_seq=-99999
    store_min=min_sum
    for i in range(1,len(arr)):
        if arr[i]==min_sum:
            continue
        elif arr[i]<min_sum:
            min_sum=arr[i]
        elif arr[i]<max_seq:
            max_seq=arr[i]
            store_min=min_sum
        elif arr[i]>max_seq:
            seq+=1
            if seq==3:
                print(store_min,max_seq,arr[i])
                return
            max_seq=arr[i]     
    return -1
subseq3(a)                       
