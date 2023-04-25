from listaEncadeada import ListaEncadeada


def remove_duplicatas(lista: ListaEncadeada):
    corrente = lista.cabeca
    while corrente:
        proximo_nodo = corrente.proximo
        while proximo_nodo and corrente.dado == proximo_nodo.dado:
            proximo_nodo = proximo_nodo.proximo
        corrente.proximo = proximo_nodo
        corrente = proximo_nodo
    return lista


lista = ListaEncadeada()
lista.append(0)
lista.append(1)
lista.append(1)
lista.append(1)
lista.append(1)
lista.append(5)
lista.append(7)
lista.append(7)
lista.append(10)
lista.append(10)
print(lista)
print(remove_duplicatas(lista))
