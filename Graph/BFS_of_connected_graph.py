from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False]*(max(self.graph)+1)

        q = []
        q.append(s)
        visited[s] = True

        while len(q):
            temp = q.pop(0)
            print(temp, end=" ")

            for i in self.graph[temp]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(0)
print(g.graph)
