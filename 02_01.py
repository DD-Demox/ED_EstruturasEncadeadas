from pilhaEncadeada import Pile


def largest_element_pile(pile: Pile):
    current = pile.head
    largest_element = current.data
    current = current.next

    while current:
        if current.data > largest_element:
            largest_element = current.data
        current = current.next

    return largest_element


pilha = Pile()
pilha.insert(24)
pilha.insert(256)
pilha.insert(225)
print(pilha)
print(largest_element_pile(pilha))
