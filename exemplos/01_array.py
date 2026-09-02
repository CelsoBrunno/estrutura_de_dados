"""Aula 1 — array estático simulado."""


class ArrayEstatico:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho_atual = 0
        self.dados = [None] * capacidade

    def acessar(self, indice):
        if 0 <= indice < self.tamanho_atual:
            return self.dados[indice]
        raise IndexError("Índice fora dos limites.")

    def inserir_no_final(self, valor):
        if self.tamanho_atual < self.capacidade:
            self.dados[self.tamanho_atual] = valor
            self.tamanho_atual += 1
        else:
            raise OverflowError("Array cheio.")

    def exibir(self):
        print("Estado da memória:", self.dados)


if __name__ == "__main__":
    lista = ArrayEstatico(5)
    lista.inserir_no_final(10)
    lista.inserir_no_final(20)
    lista.inserir_no_final(30)
    lista.exibir()
    print("posição 1:", lista.acessar(1))
    try:
        cheio = ArrayEstatico(2)
        cheio.inserir_no_final("a")
        cheio.inserir_no_final("b")
        cheio.inserir_no_final("c")
    except OverflowError as erro:
        print("Erro esperado:", erro)
