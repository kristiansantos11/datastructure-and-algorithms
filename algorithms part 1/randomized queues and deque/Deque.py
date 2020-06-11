class Deque:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def isEmpty(self):
        return self.head is None

    def add_first(self, data):
        if data is None:
            raise AttributeError
        newnode = self.Node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
            self.size += 1
            return
        self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def add_last(self, data):
        if not self.head:
            newnode = self.Node(data)
            self.head = newnode
            self.tail = newnode
            self.size += 1
            return
        newtail = self.Node(data)
        oldtail = self.tail
        oldtail.next = newtail
        newtail.prev = oldtail
        self.tail = newtail
        self.size += 1

    def remove_first(self):
        if self.head is None:
            raise AttributeError
        node = self.head
        data = node.data
        if self.head.next is None:
            self.head = None
        else:
            self.head = node.next
            node.prev = None
        self.size -= 1
        return data

    def remove_last(self):
        if self.head is None:
            raise AttributeError
        node = self.tail
        data = node.data
        self.tail = node.prev
        self.tail.next = None
        node.data = None
        self.size -= 1
        return data

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __repr__(self):
            return self.data

deque = Deque()
dequeued = []
'''
while True:
    s = input("Input (Enter empty string to print dequeued list): ")
    if s == "":
        break
    elif s == "-":
        try:
            dequeued.append(deque.dequeue())
        except AttributeError:
            print("List is already empty!")
            continue
    else:
        deque.enqueue(s)
'''
try:
    deque.add_first("a")
    deque.add_first("b")
    deque.add_last("c")
    dequeued.append(deque.remove_last())
    dequeued.append(deque.remove_first())
    deque.add_last("d")
    deque.add_last("e")
    print(deque.size)
    print(deque)

    print(" ".join(dequeued))
except AttributeError:
    print("List is empty.")
