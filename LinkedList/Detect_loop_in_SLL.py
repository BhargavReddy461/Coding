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

    def detectloop(self):
        res = False

        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr.next is not None and slow_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                res = True
                break
        if res == True:
            c = 1
            slow_ptr = slow_ptr.next
            while slow_ptr != fast_ptr:
                c += 1
                slow_ptr = slow_ptr.next
            print(c)

        return res


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(12)
llist.head.next.next.next.next = llist.head

# Create a loop for testing
print(llist.detectloop())
