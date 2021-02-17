class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reversepath(node, key, q):

    if node is None:
        return

    if node.data == key:
        q.insert(0, node.data)

        node.data = q[-1]
        q.pop()

        return
    elif node.data > key:
        q.insert(0, node.data)
        reversepath(node.left, key, q)

        node.data = q[-1]

        q.pop()

    elif node.data < key:
        q.insert(0, node.data)
        reversepath(node.right, key, q)

        node.data = q[-1]

        q.pop()

    return


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def insert(node, key):

    if node == None:
        return Node(key)

    if key < node.data:
        node.left = insert(node.left, key)
    elif key > node.data:
        node.right = insert(node.right, key)

    return node


root = None
q1 = []

k = 80
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print("Before Reverse :")

inorder(root)

reversepath(root, k, q1)
print()
print("After Reverse :")

inorder(root)
