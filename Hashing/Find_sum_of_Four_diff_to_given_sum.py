a = list(map(int, input().split()))
n = len(a)
k = int(input())


def difffoursum(arr, n, k):
    data = {}
    for i in range(n-1):
        for j in range(i+1, n):
            data[arr[i]+arr[j]] = [i, j]

    for i in range(n-1):
        for j in range(i+1, n):
            summ = arr[i]+arr[j]

            if k-summ in data:
                p = data[k-summ]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):

                    print(arr[i], ", ", arr[j], ", ",
                          arr[p[0]], ", ", arr[p[1]], sep="")

                    return data


print(difffoursum(a, n, k))
