from collections import defaultdict
a = list(map(int, input().split()))
n = len(a)
k = int(input())


def countDis(arr, n, k):
    d = defaultdict(lambda: 0)

    dis_count = 0

    for i in range(k):
        if d[arr[i]] == 0:
            dis_count += 1
        d[arr[i]] += 1

    print(dis_count)
    for i in range(k, n):

        if d[arr[i-k]] == 1:
            dis_count -= 1
        d[arr[i-k]] -= 1

        if d[arr[i]] == 0:
            dis_count += 1
        d[arr[i]] += 1

        print(dis_count)


countDis(a, n, k)
