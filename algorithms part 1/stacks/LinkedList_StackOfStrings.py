''' This code is exactly the same with the princeton algorithm part 1 class'''
''' Please refer to the Stacks lesson specifically '''

class LinkedList_StackOfStrings:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = self.Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = self.Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        #nodes.append("None")
        return " ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def pop(self):
        removed_node = self.head
        self.head = self.head.next
        return removed_node.data
        
    def push(self, data):
        node = self.Node(data)
        node.next = self.head
        self.head = node

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return self.data
        

stack = LinkedList_StackOfStrings()
popped = []
while True:
    s = input("Enter string: ")
    if s == "":
        break
    elif s == "-":
        popped.append(stack.pop())
    else:
        stack.push(s)

print(" ".join(popped))
