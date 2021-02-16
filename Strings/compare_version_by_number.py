
def versionCompare(v1, v2):
    n = len(v1)
    m = len(v2)

    if n > m:
        for i in range(m, n):
            v2.append(0)
    elif m > n:
        for i in range(n, m):
            v1.append(0)

    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return 1
        elif v2[i] > v1[i]:
            return -1
    return 0


version1 = list(map(int, input().split(".")))
version2 = list(map(int, input().split(".")))

print(versionCompare(version1, version2))
