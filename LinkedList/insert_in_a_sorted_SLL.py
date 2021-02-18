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

    def traversal(self):
        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def sortedInsert(self, new_data):
        new_node = Node(new_data)
        curr = self.head
        if self.head == None:
            self.head = new_node
            return

        if curr.data > new_node.data:
            new_node.next = curr
            self.head = new_node
            return

        while curr.next and curr.next.data < new_node.data:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node


if __name__ == '__main__':
    start = LinkedList()
    start.push(8)
    start.push(7)
    start.push(4)
    start.push(3)

    start.sortedInsert(5)
    start.traversal()
