"""Aula 4 — tabela hash que cresce pelo fator de carga."""


class TabelaHash:
    def __init__(self, tamanho=8, limite=0.75):
        self.tamanho = tamanho
        self.limite = limite
        self.quantidade = 0
        self.baldes = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return sum(ord(c) for c in str(chave)) % self.tamanho

    def fator_carga(self):
        return self.quantidade / self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.baldes[indice].append([chave, valor])
        self.quantidade += 1
        if self.fator_carga() > self.limite:
            self._crescer()

    def buscar(self, chave):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                return par[1]
        return None

    def _crescer(self):
        antigos = []
        for balde in self.baldes:
            antigos.extend(balde)
        self.tamanho *= 2
        self.baldes = [[] for _ in range(self.tamanho)]
        for chave, valor in antigos:
            indice = self._hash(chave)
            self.baldes[indice].append([chave, valor])


if __name__ == "__main__":
    catalogo = TabelaHash(4)
    for codigo, nome in [
        ("u001", "Ana"),
        ("u002", "Bia"),
        ("u003", "Caio"),
        ("u004", "Duda"),
    ]:
        catalogo.inserir(codigo, nome)
        print(
            f"depois de {codigo}: tamanho={catalogo.tamanho} "
            f"itens={catalogo.quantidade} "
            f"fator={catalogo.fator_carga():.2f}"
        )
    print("Busca u001:", catalogo.buscar("u001"))
    print("Baldes:", catalogo.baldes)
