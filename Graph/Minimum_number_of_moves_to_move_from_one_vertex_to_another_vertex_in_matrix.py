class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, s, d):
        self.adj[s].append(d)

    def BFS(self, s, d):

        level = [-1] * self.V

        queue = []

        level[s] = 0
        queue.append(s)

        while (len(queue) != 0):

            s = queue.pop()

            for i in range(len(self.adj[s])):

                if (level[self.adj[s][i]] < 0 or
                        level[self.adj[s][i]] > level[s] + 1):
                    level[self.adj[s][i]] = level[s] + 1
                    queue.append(self.adj[s][i])

        return level[d]


def isSafe(i, j, M):
    global N
    if ((i < 0 or i >= N) or
            (j < 0 or j >= N) or M[i][j] == 0):
        return False
    return True


def MinimumPath(M):
    global N
    s, d = None, None
    V = N * N + 2
    g = Graph(V)

    k = 1
    for i in range(N):
        for j in range(N):
            if (M[i][j] != 0):

                if (isSafe(i, j + 1, M)):
                    g.addEdge(k, k + 1)
                if (isSafe(i, j - 1, M)):
                    g.addEdge(k, k - 1)
                if (j < N - 1 and isSafe(i + 1, j, M)):
                    g.addEdge(k, k + N)
                if (i > 0 and isSafe(i - 1, j, M)):
                    g.addEdge(k, k - N)

            if(M[i][j] == 1):
                s = k

            if (M[i][j] == 2):
                d = k
            k += 1

    return g.BFS(s, d)


N = 4
M = [[3, 3, 1, 0], [3, 0, 3, 3],
     [2, 3, 0, 3], [0, 3, 3, 3]]

print(MinimumPath(M))
