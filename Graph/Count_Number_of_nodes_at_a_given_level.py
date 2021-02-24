from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s, l):

        visited = [False for i in range(self.V+1)]
        level = [0 for i in range(self.V+1)]

        q = []
        q.append(s)
        visited[s] = True
        level[s] = 0

        while len(q):

            temp = q.pop(0)

            for i in self.graph[temp]:
                if visited[i] == False:
                    q.append(i)
                    level[i] = level[temp]+1
                    visited[i] = True
        count = 0
        for i in range(len(level)):
            if level[i] == l:
                count += 1
        return count


if __name__ == '__main__':

    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)

    level = 0

    print(g.BFS(0, level))
