class cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


def inside(x, y, N):
    if x > 0 and x <= N and y > 0 and y <= N:
        return True
    return False


def minSteps(k, T, N):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    q = []
    q.append(cell(k[0], k[1], 0))

    visited = [[False for i in range(N + 1)] for j in range(N + 1)]

    visited[k[0]][k[1]] = True

    while len(q):
        t = q.pop(0)

        if t.x == T[0] and t.y == T[1]:
            return t.dist

        for i in range(8):

            x = t.x + dx[i]
            y = t.y + dy[i]

            if inside(x, y, N) and not visited[x][y]:
                visited[x][y] = True
                q.append(cell(x, y, t.dist+1))


N = 30
knightpos = [1, 1]
targetpos = [30, 30]
print(minSteps(knightpos, targetpos, N))
