"""Aula 7 — min-heap em array."""


class MinHeap:
    def __init__(self):
        self.dados = []

    def _pai(self, i):
        return (i - 1) // 2

    def _esq(self, i):
        return 2 * i + 1

    def _dir(self, i):
        return 2 * i + 2

    def _sobe(self, i):
        while i > 0:
            p = self._pai(i)
            if self.dados[i] < self.dados[p]:
                self.dados[i], self.dados[p] = self.dados[p], self.dados[i]
                i = p
            else:
                break

    def _desce(self, i):
        n = len(self.dados)
        while True:
            menor = i
            e, d = self._esq(i), self._dir(i)
            if e < n and self.dados[e] < self.dados[menor]:
                menor = e
            if d < n and self.dados[d] < self.dados[menor]:
                menor = d
            if menor == i:
                break
            self.dados[i], self.dados[menor] = self.dados[menor], self.dados[i]
            i = menor

    def inserir(self, valor):
        self.dados.append(valor)
        self._sobe(len(self.dados) - 1)

    def extrair_min(self):
        if not self.dados:
            raise IndexError("Heap vazio.")
        minimo = self.dados[0]
        ultimo = self.dados.pop()
        if self.dados:
            self.dados[0] = ultimo
            self._desce(0)
        return minimo


if __name__ == "__main__":
    heap = MinHeap()
    for n in (5, 1, 4, 2):
        heap.inserir(n)
    print(
        "Extrai em ordem:",
        heap.extrair_min(),
        heap.extrair_min(),
        heap.extrair_min(),
        heap.extrair_min(),
    )
