"""Aula 5 — a BST pende; uma rotação à esquerda equilibra."""


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


def rotacionar_esquerda(no):
    """O filho direito sobe; o nó desce para a esquerda. 10-20-30 vira 20 no topo."""
    novo_topo = no.direita
    no.direita = novo_topo.esquerda
    novo_topo.esquerda = no
    return novo_topo


if __name__ == "__main__":
    arvore = ArvoreBusca()
    for codigo in (50, 30, 70, 20, 40, 35, 36, 37):
        arvore.inserir(codigo)
    print("Com 35, 36, 37 (ramo vira lista). Em-ordem:")
    arvore.em_ordem(arvore.raiz)
    print()

    vareta = NoArvore(10)
    vareta.direita = NoArvore(20)
    vareta.direita.direita = NoArvore(30)
    print("Antes da rotação, raiz =", vareta.valor)
    equilibrada = rotacionar_esquerda(vareta)
    print("Depois, raiz =", equilibrada.valor)
    print("esquerda =", equilibrada.esquerda.valor, "direita =", equilibrada.direita.valor)
