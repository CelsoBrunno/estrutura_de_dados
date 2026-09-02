"""Aula 3 — pilha e fila sobre lista encadeada."""


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, dado):
        novo = No(dado)
        novo.proximo = self.topo
        self.topo = novo

    def desempilhar(self):
        if self.topo is None:
            raise IndexError("Pilha vazia.")
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado

    def vazia(self):
        return self.topo is None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, dado):
        novo = No(dado)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def desenfileirar(self):
        if self.inicio is None:
            raise IndexError("Fila vazia.")
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return dado

    def vazia(self):
        return self.inicio is None


if __name__ == "__main__":
    pilha = Pilha()
    pilha.empilhar("Página 1")
    pilha.empilhar("Página 2")
    pilha.empilhar("Página 3")
    print("Desempilhou:", pilha.desempilhar())

    fila = Fila()
    fila.enfileirar("Ana")
    fila.enfileirar("Bia")
    fila.enfileirar("Caio")
    print("Atendeu:", fila.desenfileirar())
    print("Atendeu:", fila.desenfileirar())
