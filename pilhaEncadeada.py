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

    def busca(self, dado):
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != dado:
            anterior = corrente
            corrente = corrente.proximo
        if corrente is None:
            return None
        return anterior, corrente


