import random
from pilhaEncadeada import Pile


def t_pilha(array: list):
    pile = Pile()
    for i in array:
        if i % 2 == 0:
            pile.insert(i)
        else:
            try:
                pile.remove()
            except AssertionError:
                continue
    return pile


numbers_array = [random.randint(1, 100) for i in range(15)]
print(numbers_array)
pilha = t_pilha(numbers_array)
print(pilha)
for i in range(pilha.size()):
    print(pilha.remove())
