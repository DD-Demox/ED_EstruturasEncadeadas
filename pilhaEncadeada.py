class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next: Node = next_node

    def __repr__(self):
        if self.next is None:
            return str(self.data)
        else:
            return str(self.data)+", " + str(self.next)


class Pile:
    def __init__(self):
        self.head: Node = None

    def __repr__(self):
        return "["+str(self.head)+"]"

    def insert(self,value):
        new_node = Node(value,self.head)
        self.head = new_node

    def remove(self):
        assert self.head, "Nao pode remover de uma pilha vazia"
        data = self.head.data
        self.head = self.head.next
        return data

    def search(self, data):
        previous = None
        current = self.head
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return None
        return previous, current

    def get_value_index(self, index):
        current = self.head
        assert current, "Nao há elemento nessa pilha"
        if index == 0:
            return current.data
        else:
            for i in range(index):
                assert current, "Nao existe esse Index nessa pilha "
                current = current.next
            return current.data

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

