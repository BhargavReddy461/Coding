a = list(map(int, input().split()))
n = len(a)


def posneg(arr, n):

    hash = {}

    for i in arr:
        if abs(i) in hash:
            print(-i, i, end=" ")
        else:
            hash[abs(i)] = 1


posneg(a, n)
