"""Aula 2 — lista simplesmente encadeada."""


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, dado):
        novo = No(dado)
        novo.proximo = self.cabeca
        self.cabeca = novo
        print(f"[{dado}] inserido no início.")

    def exibir(self):
        atual = self.cabeca
        partes = []
        while atual is not None:
            partes.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(partes) + " -> None")


if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.inserir_no_inicio("Terceiro")
    lista.inserir_no_inicio("Segundo")
    lista.inserir_no_inicio("Primeiro")
    lista.exibir()
