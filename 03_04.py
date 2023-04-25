from filaEncadeada import Queue
from listaEncadeada import ListaEncadeada


def invert_queue(queue_to_invert: Queue):
    lista = ListaEncadeada()
    for i in range(queue_to_invert.size()):
        lista.inserir_no_inicio(queue_to_invert.pop())
    for i in range(lista.size()):
        queue_to_invert.push(lista.get_value_index(i))


queue = Queue()
queue.push(1)
queue.push(4)
queue.push(5)
queue.push(2)
print(queue)
invert_queue(queue)
print(queue)
