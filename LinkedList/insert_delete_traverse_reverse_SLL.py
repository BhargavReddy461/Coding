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

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def length(self):
        temp = self.head
        c = 0
        while(temp):
            c += 1
            temp = temp.next
        print(c)

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


llist = LinkedList()
llist.append(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.insertAfter(llist.head.next, 6)
llist.length()
llist.traversal()
llist.reverse()
print("\n")
llist.traversal()
