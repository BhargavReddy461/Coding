a = list(map(int, input().split()))
n = len(a)
y = int(input())


def triplets(a, n, y):
    count = 0
    if n < 3:
        return "size is less than three"
    a.sort()
    z = False
    for i in range(0, n-1):
        l = i+1
        r = n-1
        x = a[i]
        while l < r:
            if x+a[l]+a[r] == y:
                count += 1
                l += 1
                r -= 1
                z = True

            elif x+a[l]+a[r] < y:
                l += 1
            else:
                r -= 1
    if not z and n > 3:
        return "no triplets"
    return count


print(triplets(a, n, y))
