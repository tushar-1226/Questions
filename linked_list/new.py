class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(14)
b = Node(13)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)
print(b.next.data)
