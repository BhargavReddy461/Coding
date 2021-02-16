a = list(map(int, input().split()))
n = len(a)


def counttriangles(a, n):
    a.sort()
    count = 0
    for i in range(n-1, 0, -1):
        l = 0
        r = i-1
        while l < r:
            if a[l]+a[r] > a[i]:
                count += r-l
                r -= 1
            else:
                l += 1
    return count


print(counttriangles(a, n))
