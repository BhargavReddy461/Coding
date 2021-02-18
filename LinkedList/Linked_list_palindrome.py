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


def reverse(llist, half):
    prev = None
    current = half
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    shalf = prev
    return shalf


def palindrome(llist):
    n = llist.length()
    temp = llist.head

    if n % 2 == 0:
        m = n//2
    else:
        m = n//2+1
    mid = llist.head
    for _ in range(m):
        mid = mid.next
    second_half = reverse(llist, mid)
    res = True
    while second_half is not None:
        if temp.data == second_half.data:
            temp = temp.next
            second_half = second_half.next
        else:
            res = False
    return res


if __name__ == '__main__':

    llist = LinkedList()
    s = ['a', 'b', 'a', 'c', 'c', 'a', 'b']

    for i in range(7):
        llist.push(s[i])

    print(palindrome(llist))
