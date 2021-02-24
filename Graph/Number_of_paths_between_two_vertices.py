from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def countpathUtil(self, u, d, visited, pathcount):
        visited[u] = True

        if u == d:
            pathcount[0] += 1
        else:

            for i in self.graph[u]:
                if not visited[i]:
                    self.countpathUtil(i, d, visited, pathcount)
        visited[u] = False

    def countPath(self, s, d):

        visited = [False for i in range(self.V)]
        pathcount = [0]
        self.countpathUtil(s, d, visited, pathcount)
        return pathcount[0]


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2
d = 3
print(g.countPath(s, d))
