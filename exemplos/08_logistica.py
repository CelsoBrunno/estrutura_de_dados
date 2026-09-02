"""Aula 8 — referência do simulador de logística."""

from collections import deque


class TabelaHash:
    def __init__(self, tamanho=16):
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


class Grafo:
    def __init__(self):
        self.vizinhos = {}

    def adicionar_vertice(self, nome):
        self.vizinhos.setdefault(nome, [])

    def adicionar_aresta(self, a, b):
        self.adicionar_vertice(a)
        self.adicionar_vertice(b)
        self.vizinhos[a].append(b)
        self.vizinhos[b].append(a)

    def bfs(self, inicio, destino):
        fila = deque([inicio])
        veio_de = {inicio: None}
        while fila:
            atual = fila.popleft()
            if atual == destino:
                break
            for vizinho in self.vizinhos.get(atual, []):
                if vizinho not in veio_de:
                    veio_de[vizinho] = atual
                    fila.append(vizinho)
        if destino not in veio_de:
            return None
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = veio_de[atual]
        caminho.reverse()
        return caminho


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


class SistemaLogistica:
    def __init__(self):
        self.rotas = Grafo()
        self.pacotes = TabelaHash()
        self.prioridade = MinHeap()
        self.ordem = 0

    def cadastrar_rota(self, origem, destino):
        self.rotas.adicionar_aresta(origem, destino)

    def registrar_pacote(self, id_pacote, destino, urgencia):
        self.pacotes.inserir(id_pacote, {"destino": destino, "urgencia": urgencia})
        self.prioridade.inserir((urgencia, self.ordem, id_pacote))
        self.ordem += 1

    def processar_entregas(self, deposito="CD"):
        while self.prioridade.dados:
            urgencia, _, id_pacote = self.prioridade.extrair_min()
            info = self.pacotes.buscar(id_pacote)
            caminho = self.rotas.bfs(deposito, info["destino"])
            print(f"{id_pacote} urgência {urgencia}: {caminho}")


if __name__ == "__main__":
    sistema = SistemaLogistica()
    sistema.cadastrar_rota("CD", "Centro")
    sistema.cadastrar_rota("Centro", "Asa Norte")
    sistema.cadastrar_rota("Centro", "Asa Sul")
    sistema.cadastrar_rota("Asa Norte", "Lago Norte")
    sistema.registrar_pacote("P1", "Asa Sul", 3)
    sistema.registrar_pacote("P2", "Lago Norte", 1)
    sistema.registrar_pacote("P3", "Asa Norte", 2)
    sistema.processar_entregas()
