def fillHeight(parent, i, visited, height):
    if parent[i] == -1:
        visited[i] = 1
        return 0
    if visited[i]:
        return height[i]

    visited[i] = 1
    height[i] = 1+fillHeight(parent, parent[i], visited, height)
    return height[i]


def findHeight(parent):
    n = len(parent)

    visited = [0]*n
    height = [0]*n
    h = 0
    for i in range(n):
        if not visited[i]:
            height[i] = fillHeight(parent, i, visited, height)
        h = max(h, height[i])
    return h


if __name__ == '__main__':

    parent = [-1, 0, 0, 0, 3, 1, 1, 2]

    print("Height of N-ary Tree =", findHeight(parent))
