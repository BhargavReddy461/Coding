class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


st = []
s = set()


def buildtree(inorder, preorder, n):
    root = None
    pre = 0
    inn = 0
    while pre < n:
        node = None

        while True:
            node = Node(preorder[pre])
            if root == None:
                root = node

            if len(st) > 0:
                if st[-1] in s:
                    s.discard(st[-1])
                    st[-1].right = node
                    st.pop()
                else:
                    st[-1].left = node

            st.append(node)
            if pre >= n or preorder[pre] == inorder[inn]:
                pre += 1
                break
            pre += 1
        node = None

        while len(st) > 0 and inn < n and st[-1].data == inorder[inn]:

            node = st.pop()
            inn += 1

        if node is not None:

            s.add(node)
            st.append(node)
    return root


def _inorder(root):
    temp = root
    if(not temp):
        return
    _inorder(temp.left)
    print(temp.data, end=" ")
    _inorder(temp.right)


inorder = [9, 8, 4, 2, 10, 5, 10, 1, 6, 3, 13, 12, 7]
preorder = [1, 2, 4, 8, 9, 5, 10, 10, 3, 6, 7, 12, 13]

length = len(inorder)

root = buildtree(inorder, preorder, length)

_inorder(root)
