class Node:
    def __init__(self, id_processo, name, priority, wait=0, next_node=None):
        self.id: int = id_processo
        self.name: str = name
        self.priority: int = priority
        self.wait: int = wait
        self.next: Node = next_node

    def __repr__(self):
        if self.next is None:
            return f"[{self.name}, {self.id}, {self.priority}, {self.wait}]"
        else:
            return f"[{self.name}, {self.id}, {self.priority}, {self.wait}], " + str(self.next)


class Queue:
    def __init__(self):
        self.head: Node = None

    def __repr__(self):
        return "["+str(self.head)+"]"

    def push(self, id_processo, name, priority, wait):
        if self.head is None:
            node = Node(id_processo, name, priority, wait)
            self.head = node
        else:
            current = self.head
            while True:
                if current.next is None:
                    break
                else:
                    current = current.next
            node = Node(id_processo, name, priority, wait)
            current.next = node

    def pop(self):
        data = [self.head.id, self.head.name, self.head.priority, self.head.wait]
        self.head = self.head.next
        return data

    def search(self, id_processo):
        previous = None
        current = self.head
        index = 0
        while current and current.id != id_processo:
            previous = current
            current = current.next
            index += 1
        if current is None:
            return None
        return previous, current, index

    def get_index_id(self, id_processo):
        node = self.search(id_processo)
        assert node, f"O processo com id {id_processo} nao esta na fila"

        return node[2]

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def empty_queue(self):
        self.head = None

    def remove_with_search(self,id_processo):
        assert self.head, "Nao pode remover se file vazia"
        search = self.search(id_processo)
        if search[0] is None:
            self.head = self.head.next
        else:
            search[0].next = search[1].next

    def kill_process_highest_process_wait(self):
        node_to_kill = self.head
        current = self.head
        while current:
            if node_to_kill.wait < current.wait:
                node_to_kill = current
            current = current.next
        self.remove_with_search(node_to_kill.id)





