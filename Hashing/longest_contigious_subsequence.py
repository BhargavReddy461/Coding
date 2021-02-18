a = list(map(int, input().split()))
n = len(a)


def maxlen(arr, n):
    hash = {}
    ans = 0

    for i in range(n):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            hash[arr[i]] += 1
    for i in range(n):

        if arr[i]-1 not in hash:

            j = arr[i]

            while j in hash:
                j += 1
            ans = max(ans, j-arr[i])
    return ans


print(maxlen(a, n))
