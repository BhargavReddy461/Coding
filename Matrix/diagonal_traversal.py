a = list(map(int, input().split()))
size = list(map(int, input().split()))
n = size[0]
m = size[1]

mat = []
k = 0
for i in range(n):
    row = []
    for i in range(m):
        p = a[k]
        k += 1
        row.append(p)
    mat.append(row)


def diatra(mat, n, m):
    mode = 0
    lower = 0

    for t in range(2*n-1):
        t1 = t
        if t1 >= n:
            mode += 1
            lower += 1
            t1 = n-1
        else:
            lower = 0

        for i in range(t1, lower-1, -1):
            if (t1+lower) % 2 == 0:
                print(mat[t1+lower-i][i], end=" ")
            else:
                print(mat[i][t1+lower-i], end=" ")


diatra(mat, n, m)
