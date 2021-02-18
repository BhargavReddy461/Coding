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


def countPairs(list1, list2, x):
    hash_map = {}
    temp = list2.head

    while temp is not None:
        hash_map[temp.data] = hash_map.get(temp.data, 0)+1
        temp = temp.next
    temp1 = list1.head
    c = 0
    while temp1 is not None:
        if x-temp1.data in hash_map:
            c += 1
        temp1 = temp1.next
    return c


list1 = LinkedList()
list2 = LinkedList()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = int(input())

for i in range(len(a)):
    list1.push(a[i])
for i in range(len(b)):
    list2.push(b[i])

print(countPairs(list1, list2, x))
