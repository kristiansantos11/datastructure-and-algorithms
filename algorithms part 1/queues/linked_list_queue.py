class LinkedListQueue:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            node = self.Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = self.Node(data=elem)
                node = node.next
            self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def isEmpty(self):
        return self.head is None

    def dequeue(self):
        if self.head is None:
            raise AttributeError
        node = self.head
        data = node.data
        if self.head.next is None:
            self.head = None
        else:
            self.head = node.next
        return data

    def enqueue(self, data):
        if not self.head:
            newnode = self.Node(data)
            self.head = newnode
            self.tail = newnode
            return self.head
        newtail = self.Node(data)
        oldtail = self.tail
        self.tail = newtail
        oldtail.next = newtail

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return self.data


queue = LinkedListQueue()
dequeued = []
while True:
    s = input("Input (Enter empty string to print dequeued list): ")
    if s == "":
        break
    elif s == "-":
        try:
            dequeued.append(queue.dequeue())
        except AttributeError:
            print("List is already empty!")
            continue
    else:
        queue.enqueue(s)

print(" ".join(dequeued))
