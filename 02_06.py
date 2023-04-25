import random

from pilhaEncadeada import Pile


def t_pilha2(pile_positive: Pile, pile_negative: Pile, array: list):
    for i in array:
        if i < 0:
            pile_negative.insert(i)
        elif i > 0:
            pile_positive.insert(i)
        else:
            try:
                pile_positive.remove()
            except AssertionError:
                pass
            try:
                pile_negative.remove()
            except AssertionError:
                pass


numbers_array_random = [random.randint(-10, 10) for i in range(15)]
numbers_array = [0, 2, -2, -3, -3, -5, 0, 0, 2, 4, 5, -2, 3, -4]
pile_n = Pile()
pile_p = Pile()
pile_n_random = Pile()
pile_p_random = Pile()


t_pilha2(pile_p, pile_n, numbers_array)
print(numbers_array)
print(pile_p)
print(pile_n)
print()
t_pilha2(pile_p_random, pile_n_random, numbers_array_random)
print(numbers_array_random)
print(pile_p_random)
print(pile_n_random)
