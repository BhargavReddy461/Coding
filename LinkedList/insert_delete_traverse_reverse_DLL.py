import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)
        temp = self.head

        if self.head is None:
            self.head = new_node
            return
        while(temp.next):
            temp = temp.next
        new_node.prev = temp
        temp.next = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print(" wrong input")
            return
        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def insertBefore(self, next_node, new_data):

        if next_node is None:
            print("wrong input")

        new_node = Node(new_data)

        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node

        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def delete(self, d):

        if self.head is None or d is None:
            return

        if self.head == d:
            self.head = d.next

        if d.next is not None:
            d.prev.next = d.next

        if d.prev is not None:
            d.next.prev = d.prev

        gc.collect()

    def length(self):
        c = 0

        temp = self.head

        while(temp):
            c += 1
            temp = temp.next
        print(c)

    def reverse(self):

        curr = self.head
        temp = None

        if curr is None or curr.next is None:
            return

        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        self.head = temp.prev

    def traversal(self):

        print("\nforward traversal")
        last = None
        curr = self.head

        while curr:
            print(curr.data, end=" ")
            last = curr
            curr = curr.next

        print("\nreverse traversal")

        while last:
            print(last.data, end=" ")
            last = last.prev


dlist = DoublyLinkedList()
dlist.push(1)
dlist.push(2)
dlist.push(3)
dlist.push(4)
dlist.push(5)
dlist.insertAfter(dlist.head.next.next, 6)
dlist.insertBefore(dlist.head.next.next, 7)
dlist.append(8)
dlist.delete(dlist.head.next)
dlist.length()
dlist.traversal()
dlist.reverse()
dlist.traversal()
