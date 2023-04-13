from filaEncadeada import Queue
from listaEncadeada import ListaEncadeada


def invert_queue(queue: Queue):
    list = ListaEncadeada()
    for i in range(queue.size()):
        list.inserir_no_inicio(queue.pop())
    queue.empty_queue()
    for i in range(list.size()):
        queue.push(list.get_value_index(i))



queue = Queue()
queue.push(1)
queue.push(4)
queue.push(5)
queue.push(2)
print(queue)
invert_queue(queue)
print(queue)
