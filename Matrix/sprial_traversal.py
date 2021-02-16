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


def spiral(mat, n, m):
    if n == 1:
        for i in range(m):
            print(mat[0][i], end=" ")
    elif m == 1:
        for i in range(n):
            print(mat[i][0], end=" ")
    else:
        k = 0
        l = 0
        while k < m and l < n:

            for i in range(k, m):
                print(mat[k][i], end=" ")

            l += 1

            for i in range(l, n):
                print(mat[i][m-1], end=" ")

            m -= 1

            if l < n:

                for i in range(m-1, k-1, -1):
                    print(mat[n-1][i], end=" ")
                n -= 1

            if k < m:

                for i in range(n-1, l-1, -1):
                    print(mat[i][0], end=" ")
                k += 1


spiral(mat, n, m)
