a = list(map(int, input().split()))
size = list(map(int, input().split()))
x = int(input())
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


def find(mat, n, m, x):
    i = 0
    j = m-1
    while i < n and j >= 0:
        if mat[i][j] == x:
            return [i, j]
        elif mat[i][j] < x:
            i += 1
        else:
            j -= 1
    return -1


print(find(mat, n, m, x))
