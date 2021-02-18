a = list(map(int, input().split()))
n = len(a)
k = int(input())


def twosum(arr, n, k):
    mp = {}
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i], 0) + 1
    print(mp)

    for i in range(n):
        if k-arr[i] in mp:
            return "YES"

    return "NO"


print(twosum(a, n, k))
