"""Aula 5 — fórmulas AVL e os quatro casos (z = novo, y = pai, x = avô)."""


class NoArvore:
    def __init__(self, valor, pai=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.pai = pai


def altura(no):
    if no is None:
        return -1
    return 1 + max(altura(no.esquerda), altura(no.direita))


def balance(no):
    if no is None:
        return 0
    return altura(no.esquerda) - altura(no.direita)


def ligar(pai, filho, lado):
    if lado == "esq":
        pai.esquerda = filho
    else:
        pai.direita = filho
    if filho is not None:
        filho.pai = pai


def rotacionar_direita(x):
    y = x.esquerda
    ligar(x, y.direita, "esq")
    y.pai = x.pai
    ligar(y, x, "dir")
    return y


def rotacionar_esquerda(x):
    y = x.direita
    ligar(x, y.esquerda, "dir")
    y.pai = x.pai
    ligar(y, x, "esq")
    return y


def mostrar(no, prefixo=""):
    if no is None:
        return
    print(f"{prefixo}{no.valor}  b={balance(no)}  h={altura(no)}")
    mostrar(no.esquerda, prefixo + "  ")
    mostrar(no.direita, prefixo + "  ")


if __name__ == "__main__":
    print("Formulas: h(None)=-1;  balance = h(esq)-h(dir);  |b|<=1 e AVL\n")

    print("Caso 1 LL — inserir 10 em 30-20, rotateRight(x=30)")
    x = NoArvore(30)
    y = NoArvore(20, x)
    z = NoArvore(10, y)
    ligar(x, y, "esq")
    ligar(y, z, "esq")
    print("  balance(x) depois de z:", balance(x), " (antes pendia +1)")
    print("  detectar LL:", x.esquerda is y and y.esquerda is z)
    raiz = rotacionar_direita(x)
    mostrar(raiz)

    print("\nCaso 2 RR — inserir 30 em 10-20, rotateLeft(x=10)")
    x = NoArvore(10)
    y = NoArvore(20, x)
    z = NoArvore(30, y)
    ligar(x, y, "dir")
    ligar(y, z, "dir")
    print("  balance(x) depois de z:", balance(x), " (antes pendia -1)")
    print("  detectar RR:", x.direita is y and y.direita is z)
    raiz = rotacionar_esquerda(x)
    mostrar(raiz)

    print("\nCaso 3 RL — inserir 20 em 10-30 (Z)")
    x = NoArvore(10)
    y = NoArvore(30, x)
    z = NoArvore(20, y)
    ligar(x, y, "dir")
    ligar(y, z, "esq")
    print("  detectar RL:", x.direita is y and y.esquerda is z)
    ligar(x, rotacionar_direita(y), "dir")
    raiz = rotacionar_esquerda(x)
    mostrar(raiz)

    print("\nCaso 4 LR — inserir 20 em 30-10 (Z)")
    x = NoArvore(30)
    y = NoArvore(10, x)
    z = NoArvore(20, y)
    ligar(x, y, "esq")
    ligar(y, z, "dir")
    print("  detectar LR:", x.esquerda is y and y.direita is z)
    ligar(x, rotacionar_esquerda(y), "esq")
    raiz = rotacionar_direita(x)
    mostrar(raiz)
