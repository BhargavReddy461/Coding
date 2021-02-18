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
        return c

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


def Addtwonumbers(list1, list2):

    m = list1.length()
    n = list2.length()
    z = max(m, n)
    if m < n:
        for i in range(m, n):
            list1.push(0)
    elif m > n:
        for i in range(n, m):
            list2.push(0)

    list1.reverse()
    list2.reverse()

    list3 = LinkedList()
    i = 0
    temp1 = list1.head
    temp2 = list2.head
    while i < z-1:

        p = temp1.data + temp2.data
        if p >= 10:
            temp1.next.data += 1
        list3.push(p % 10)

        temp1 = temp1.next
        temp2 = temp2.next

        i += 1
    if temp1.data + temp2.data >= 10:
        list3.push((temp1.data + temp2.data) % 10)
        list3.push(1)
    else:
        list3.push((temp1.data + temp2.data) % 10)

    list3.traversal()


list1 = LinkedList()
list2 = LinkedList()
list1.push(9)
list1.push(9)
list1.push(8)
list1.push(6)
list2.push(6)
list2.push(7)
list2.push(8)
list2.push(9)
list2.push(9)
list1.traversal()
print("========================================\n")
list2.traversal()
print("========================================\n")
Addtwonumbers(list1, list2)
