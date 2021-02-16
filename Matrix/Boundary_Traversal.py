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


def boundary(mat, n, m):
    if n == 1:
        for i in range(m):
            print(mat[0][i], end=" ")
    elif m == 1:
        for i in range(n):
            print(mat[i][0], end=" ")
    else:
        for i in range(m):
            print(mat[0][i], end=" ")
        for i in range(1, n):
            print(mat[i][m-1], end=" ")
        for i in range(m-2, -1, -1):
            print(mat[n-1][i], end=" ")
        for i in range(n-2, 0, -1):
            print(mat[i][0], end=" ")


boundary(mat, n, m)
