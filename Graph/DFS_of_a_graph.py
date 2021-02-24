from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self):
        visited = set()

        for i in self.graph:
            if i not in visited:
                self.DFSUtil(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS()
