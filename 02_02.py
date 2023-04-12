from pilhaEncadeada import Pile
from listaEncadeada import ListaEncadeada

pilha = Pile()
print(pilha)
sequencia = ListaEncadeada()
for i in range(10):
    sequencia.append(i)

print(sequencia)

for i in range(sequencia.size()):
    pilha.insert(sequencia.get_value_index(i))

print(pilha)
