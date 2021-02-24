from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, u, visited):
        visited[u] = True

        for i in self.graph[u]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def CountTrees(self):
        visited = [False for i in range(self.V)]

        res = 0
        for i in range(self.V):
            if not visited[i]:
                self.DFSUtil(i, visited)
                res += 1
        return res


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 4)
print(g.CountTrees())
