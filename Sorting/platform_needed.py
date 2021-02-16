arv = list(map(int, input().split()))
dep = list(map(int, input().split()))

n = len(arv)


def number(arv, dep, n):
    arv.sort()
    dep.sort()
    l = 1
    r = 0
    plat = 1
    res = 1
    while l < n and r < n:

        if arv[l] <= dep[r]:
            plat += 1
            l += 1
        else:
            plat -= 1
            r += 1
        if plat > res:
            res = plat
    return res


print(number(arv, dep, n))
