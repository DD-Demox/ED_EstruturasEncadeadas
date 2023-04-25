import random

from pilhaEncadeada import Pile


def compare_pile(pile1: Pile, pile2: Pile):
    if pile1.size() != pile2.size():
        return False
    for i in range(pile1.size()):
        if pile1.get_value_index(i) != pile2.get_value_index(i):
            return False
    return True


pilha1 = Pile()
pilha2 = Pile()
pilha3 = Pile()
for i in range(10):
    pilha1.insert(i)
    pilha2.insert(i)
    pilha3.insert(random.randint(0, 10))

print(compare_pile(pilha1, pilha2))
print(pilha3)
print(compare_pile(pilha1, pilha3))
