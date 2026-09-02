"""Aula 4 — tabela hash com encadeamento."""


class TabelaHash:
    def __init__(self, tamanho=8):
        self.tamanho = tamanho
        self.baldes = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return sum(ord(c) for c in str(chave)) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.baldes[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                return par[1]
        return None


if __name__ == "__main__":
    catalogo = TabelaHash(5)
    catalogo.inserir("u001", "João Silva")
    catalogo.inserir("u002", "Maria Souza")
    print("Busca u001:", catalogo.buscar("u001"))
    print("Busca u999:", catalogo.buscar("u999"))
    print("Baldes:", catalogo.baldes)
