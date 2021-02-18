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

    def deleteallocc(self, x):

        temp = self.head
        while temp != None and temp.data == x:
            self.head = temp.next
            temp = self.head
        prev = self.head
        while temp:

            if temp.data == x:
                prev.next = temp.next
                temp = None
                temp = prev.next
            else:
                prev = temp
                temp = temp.next

        return self.head


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.push(1)
    llist.push(2)
    llist.push(2)
    llist.push(4)
    llist.push(2)
    llist.push(5)
    llist.push(3)
    llist.push(2)

    x = 2
    llist.deleteallocc(x)
    llist.traversal()
