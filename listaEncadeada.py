class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo: NodoLista = proximo_nodo

    def __repr__(self):
        return str(self.dado)+"->"+str(self.proximo)


class ListaEncadeada:

    """ Esta classe representa uma lista encadeada """

    def __init__(self):
        self.cabeca: NodoLista = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def inserir_no_inicio(self, dado):

        novo_nodo = NodoLista(dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        return self.cabeca

        # nodoInicial = self.cabeca
        # nodo = NodoLista(dado, nodoInicial)
        # self.cabeca = nodo

    def insere_depois(self, valor_a_encontrar, dado_insercao):
        nodo_busca = self.busca(valor_a_encontrar)
        assert nodo_busca, "Nao existe na lista"
        novo_nodo = NodoLista(dado_insercao, nodo_busca[1].proximo)
        nodo_busca[1].proximo = novo_nodo

    def append(self, dado):
        if self.cabeca is None:
            nodo = NodoLista(dado)
            self.cabeca = nodo
            return self.cabeca
        else:
            corrente = self.cabeca
            while True:
                if corrente.proximo is None:
                    break
                else:
                    corrente = corrente.proximo
            nodo = NodoLista(dado)
            corrente.proximo = nodo
            return nodo

    def busca(self, dado):
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != dado:
            anterior = corrente
            corrente = corrente.proximo
        if corrente is None:
            return None
        return anterior, corrente

    def remover(self, valor_a_remover):
        assert self.cabeca, "Nao pode remover de uma lista vazia"
        if self.cabeca.dado == valor_a_remover:
            self.cabeca = self.cabeca.proximo
        else:
            anterior = self.cabeca
            corrente = self.cabeca.proximo
            while corrente and corrente.dado != valor_a_remover:
                anterior = corrente
                corrente = corrente.proximo
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                anterior.proximo = None

    def remove_com_busca(self, valor_a_remover):
        assert self.cabeca, "Nao pode remover de uma lista vazia"
        busca = self.busca(valor_a_remover)
        if busca[0] is None:
            self.cabeca = self.cabeca.proximo
        else:
            if busca[1]:
                busca[0].proximo = busca[1].proximo
            else:
                busca[0].proximo = None

    def get_value_index(self,index):
        current = self.cabeca
        assert current, "Nao há elemento nessa lista"
        if index == 0:
            return current.dado
        else:
            for i in range(index):
                assert current, "Nao existe esse Index nessa lista "
                current = current.proximo
            return current.dado

    def size(self):
        size = 0
        current = self.cabeca
        while current:
            size +=1
            current = current.proximo
        return size



