a = list(input().split())
n = len(a)
pat = input()


def hashing(pat):
    hash = ""
    i = 0
    map = {}

    for j in pat:
        if j not in map:
            map[j] = i
            i += 1
        hash += str(map[j])
    return hash


def mathched(a, pat):
    hash = hashing(pat)

    for i in a:
        if len(hash) == len(i) and hash == hashing(i):
            print(i, end=" ")


mathched(a, pat)
