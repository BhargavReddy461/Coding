from collections import deque


def BFS(a, b, target):
    map = {}
    ans = False
    path = []

    q = deque()
    q.append([0, 0])

    while len(q) > 0:

        u = q.popleft()

        if ((u[0], u[1]) in map):
            continue
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue
        path.append([u[0], u[1]])

        map[(u[0], u[1])] = 1

        if u[0] == target or u[1] == target:
            ans = True
            if u[0] == target:
                if u[1] != 0:
                    path.append([u[0], 0])
            else:
                if u[0] != 0:
                    path.append([0, u[1]])
            return path

        q.append([u[0], b])
        q.append([a, u[1]])

        for i in range(max(a, b)+1):
            c = u[0]+i
            d = u[1]-i
            if c == a or (d == 0 and d >= 0):
                q.append([c, d])

            c = u[0]-i
            d = u[1]+i
            if (c == 0 and c >= 0) or d == b:
                q.append([c, d])
        q.append([a, 0])
        q.append([0, b])

    if not ans:
        print("No solution")
        return 0


Jug1, Jug2, target = 4, 3, 2


print(BFS(Jug1, Jug2, target))
