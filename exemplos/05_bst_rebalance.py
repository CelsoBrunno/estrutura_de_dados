"""Aula 5 — rotação com filhos, reconstruir pelo meio e inserir o 32."""


class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoArvore(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoArvore(valor)
            else:
                self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = NoArvore(valor)
            else:
                self._inserir(no.direita, valor)

    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.em_ordem(no.direita)


def mostrar(no, prefixo=""):
    if no is None:
        return
    esq = no.esquerda.valor if no.esquerda else None
    dir_ = no.direita.valor if no.direita else None
    print(f"{prefixo}{no.valor}  esq={esq}  dir={dir_}")
    mostrar(no.esquerda, prefixo + "  ")
    mostrar(no.direita, prefixo + "  ")


def rotacionar_esquerda(no):
    novo_topo = no.direita
    no.direita = novo_topo.esquerda
    novo_topo.esquerda = no
    return novo_topo


def construir_equilibrada(valores):
    if not valores:
        return None
    meio = len(valores) // 2
    no = NoArvore(valores[meio])
    no.esquerda = construir_equilibrada(valores[:meio])
    no.direita = construir_equilibrada(valores[meio + 1 :])
    return no


if __name__ == "__main__":
    pendente = ArvoreBusca()
    for codigo in (50, 30, 70, 20, 40, 35, 36, 37):
        pendente.inserir(codigo)
    print("Pendente (20, 30, 40, 35, 36, 37, 50, 70):")
    mostrar(pendente.raiz)
    print("Em-ordem:", end=" ")
    pendente.em_ordem(pendente.raiz)
    print()

    pendente.raiz.esquerda = rotacionar_esquerda(pendente.raiz.esquerda)
    print("\nDepois de girar o 30 (pai que ja tinha filhos):")
    mostrar(pendente.raiz)
    print("Em-ordem (continua crescente):", end=" ")
    pendente.em_ordem(pendente.raiz)
    print()

    reset = ArvoreBusca()
    reset.raiz = construir_equilibrada([20, 30, 35, 36, 37, 40, 50, 70])
    print("\nReconstruida pelo meio (raiz 37):")
    mostrar(reset.raiz)

    reset.inserir(32)
    print("\nDepois de inserir o 32 (30 fica pai de 20 e 32):")
    mostrar(reset.raiz)
    print("Em-ordem:", end=" ")
    reset.em_ordem(reset.raiz)
    print()
