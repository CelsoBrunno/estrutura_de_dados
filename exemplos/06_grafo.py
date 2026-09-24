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
    rua = Grafo()
    rua.adicionar_aresta("Karla", "Brunno")
    rua.adicionar_aresta("Brunno", "Carlos")
    rua.adicionar_aresta("Carlos", "Erik")
    rua.adicionar_aresta("Erik", "Natan")
    rua.adicionar_aresta("Natan", "Gabriel")
    rua.adicionar_aresta("Juan", "Gabriel")
    print("Vizinhos do Gabriel:", rua.vizinhos["Gabriel"])
    print("Caminho Gabriel -> Karla:", rua.bfs("Gabriel", "Karla"))
    print("Amigos em comum Brunno e Erik:", rua.amigos_em_comum("Brunno", "Erik"))
