class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self): #__repr__ exists so you don't have to type cast the class into String data type
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self): #enables LinkedList to have a DEFAULT string representation
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self): #enables LinkedList to become an iterable object
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self: #After the entire list is iterated, the pointer does not return back to 0.
            pass                # Linked lists cannot be indexed.
        current_node.next = node #current_node pointer is at the last item

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")

        if target_node_data == self.head.data:
            self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if target_node_data == node.data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data %s is not found!" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty!")

        if target_node_data == self.head.data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if target_node_data == node.data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Node with data %s is not found!" % target_node_data)
    

'''linked_list = LinkedList()
print(linked_list)

first_node = Node("c")
second_node = Node("b")
third_node = Node("a")
linked_list.head = first_node
first_node.next = second_node
second_node.next = third_node
linked_list.add_first(Node("d"))
print(linked_list)


linked_list2 = LinkedList(["a","b","c","d","e","f"])
print(linked_list2)'''

linked_list = LinkedList()
linked_list.add_last(Node("b"))
linked_list.add_last(Node("c"))
linked_list.add_last(Node("d"))
linked_list.add_first(Node("a"))
linked_list.add_last(Node("e"))
linked_list.add_after("c", Node("cx"))
linked_list.add_before("c", Node("bx"))

print(linked_list)
