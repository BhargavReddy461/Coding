from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s):

        visited = [False for i in range(self.V)]

        stack = []
        stack.append(s)

        while len(stack):
            temp = stack.pop()

            if not visited[temp]:
                print(temp, end=" ")
                visited[temp] = True

            for i in self.graph[temp]:
                if not visited[i]:
                    stack.append(i)


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)

print("Following is Depth First Traversal")
g.DFS(0)
