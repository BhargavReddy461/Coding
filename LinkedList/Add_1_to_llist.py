class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("prev node doesn't exist")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def traversal(self):
        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev


def Add1(llist):
    llist.reverse()
    temp = llist.head
    temp.data += 1
    while temp.next:
        if temp.data >= 10:
            temp.data = temp.data % 10
            temp.next.data += 1
        temp = temp.next
    if temp.data >= 10:
        temp.data = temp.data % 10
        llist.insertAfter(temp, 1)
    llist.reverse()

    return


llist = LinkedList()
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    llist.push(a[n-1-i])
Add1(llist)
llist.traversal()
