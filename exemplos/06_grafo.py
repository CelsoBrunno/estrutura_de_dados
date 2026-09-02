"""Aula 6 — grafo não direcionado e BFS."""

from collections import deque


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
            for vizinho in self.vizinhos[atual]:
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

    def amigos_em_comum(self, u1, u2):
        a = set(self.vizinhos.get(u1, []))
        b = set(self.vizinhos.get(u2, []))
        return sorted(a & b)


if __name__ == "__main__":
    rede = Grafo()
    rede.adicionar_aresta("Alice", "Bruno")
    rede.adicionar_aresta("Bruno", "Carlos")
    rede.adicionar_aresta("Alice", "Duda")
    rede.adicionar_aresta("Duda", "Carlos")
    print("Amigos de Bruno:", rede.vizinhos["Bruno"])
    print("Caminho Alice -> Carlos:", rede.bfs("Alice", "Carlos"))
    print("Amigos em comum Alice e Carlos:", rede.amigos_em_comum("Alice", "Carlos"))
