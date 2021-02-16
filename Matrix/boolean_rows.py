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


def bin(mat, n, m):
    binlist = []
    for i in range(n):
        a = ""
        for j in range(m):
            a += str(mat[i][j])
        binlist.append(int(a))
    return binlist


binlist = bin(mat, n, m)


def find(binlist, n):
    list = []
    for i in range(n):
        if binlist[i] not in list:
            print(mat[i])
            list.append(binlist[i])
    return 1


find(binlist, n)
