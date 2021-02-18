a = list(map(int, input().split()))
n = len(a)


def maxlen(arr, n):

    hash = {}
    curr_sum = 0
    max_len = 0

    for i in range(n):
        curr_sum += arr[i]

        if arr[i] == 0 and max_len == 0:
            max_len = 1

        if curr_sum == 0:
            max_len = i+1

        if curr_sum in hash:
            max_len = max(max_len, i-hash[curr_sum])
        else:
            hash[curr_sum] = i

    return max_len


print(maxlen(a, n))
