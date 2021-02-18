arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def realtivesorting(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    hash = {}
    res = []

    for i in range(n):
        if arr1[i] not in hash:
            hash[arr1[i]] = 1
        else:
            hash[arr1[i]] += 1

    for i in range(m):
        if arr2[i] in hash:
            res += [arr2[i]]*hash[arr2[i]]
            hash[arr2[i]] = 0

    rem = []
    for i in hash:
        rem += [i]*hash[i]
    rem.sort()
    res += rem
    return res


print(realtivesorting(arr1, arr2))
