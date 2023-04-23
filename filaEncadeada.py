class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next: Node = next_node

    def __repr__(self):
        if self.next is None:
            return str(self.data)
        else:
            return str(self.data) + ", " + str(self.next)


class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __repr__(self):
        return "["+str(self.head)+"]"

    def push(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            tail = self.tail
            node = Node(data)
            self.tail.next = node
            self.tail = node

    def pop(self):
        assert self.head, "Nao pode remover de uma fila vazia"
        data = self.head.data
        self.head = self.head.next
        return data

    def search(self, data):
        previous = None
        current = self.head
        index = 0
        while current and current.data != data:
            previous = current
            current = current.next
            index += 1
        if current is None:
            return None
        return previous, current, index

    def get_index_value(self, value):
        node = self.search(value)
        assert node, f"{value} nao esta na fila"

        return node[2]

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current= current.next
        return size

    def empty_queue(self):
        self.head = None


