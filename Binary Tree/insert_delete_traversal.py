class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):

    if root is None:
        root = Node(key)
        return root
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


def delete(root, key):

    if root == None:
        return None
        if root.left == None or root.right == None:
            if root.data == key:
                return None
            else:
                return root
    q = []
    q.append(root)
    key_node = None
    temp = None
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data

        q = []
        q.append(root)
        while(len(q)):
            tem = q.pop(0)
            if tem is temp:
                tem = None
                return
            if tem.right:
                if tem.right is temp:
                    tem.right = None
                    return
                else:
                    q.append(tem.right)
            if tem.left:
                if tem.left is temp:
                    tem.left = None
                    return
                else:
                    q.append(tem.left)
        key_node.data = x
    return root


def inorder(root):
    temp = root
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


def preorder(root):
    temp = root
    if(not temp):
        return
    print(temp.data, end=" ")
    preorder(temp.left)
    preorder(temp.right)


def postorder(root):
    temp = root
    if(not temp):
        return
    postorder(temp.left)
    postorder(temp.right)
    print(temp.data, end=" ")


if __name__ == '__main__':

    root = Node(9)
    a = list(map(int, input().split()))
    for i in range(len(a)):
        insert(root, a[i])
    inorder(root)
    print()
    preorder(root)
    print()
    postorder(root)
    delete(root, 12)
    print()
    inorder(root)
