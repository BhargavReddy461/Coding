a = list(map(int, input().split()))
n = len(a)


def triplets(a, n):
    if n < 3:
        print("size is less than three")
    a.sort()
    z = False
    for i in range(0, n-1):
        l = i+1
        r = n-1
        x = a[i]
        while l < r:
            if x+a[l]+a[r] == 0:
                print(x, a[l], a[r])
                l += 1
                r -= 1
                z = True

            elif x+a[l]+a[r] < 0:
                l += 1
            else:
                r -= 1
    if not z and n > 3:
        print("no triplets")


triplets(a, n)
