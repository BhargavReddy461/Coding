a = list(map(int, input().split()))
size = list(map(int, input().split()))
n = size[0]
m = size[1]

mat = []
k = 0
for i in range(n):
    row = []
    for j in range(m):
        p = a[k]
        k += 1
        row.append(p)
    mat.append(row)


def transpose(mat, n, m):
    for i in range(n):
        for j in range(i, m):
            mat[i][j], mat[j][i] == mat[j][i], mat[i][j]


def revcol(mat, n, m):
    for i in range(m):
        for j in range(n//2):
            mat[j][i], mat[n-i-1][i] = mat[n-i-1][i], mat[j][i]


transpose(mat, n, m)
revcol(mat, n, m)
print(mat)
