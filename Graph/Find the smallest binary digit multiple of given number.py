def getMinimumMultipleOfBinaryDigit(A):

    q = []

    visitedRem = set([])
    t = '1'
    q.append(t)
    while q:
        t = q.pop(0)
        rem = int(t) % A
        if rem == 0:
            return t
        if rem not in visitedRem:
            visitedRem.add(rem)
            q.append(t+'0')
            q.append(t+'1')


n = 12
print(getMinimumMultipleOfBinaryDigit(n))
