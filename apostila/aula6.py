"""Rascunho isolado da Aula 6 — não altera a apostila completa.

Gera Word/PDF só desta aula:

    cd apostila
    python aula6.py
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import estilo as e  # noqa: E402
import figuras  # noqa: E402
import figuras_grafo  # noqa: E402

SAIDA = HERE / "Apostila-Aula-6.docx"

SUMARIO = [
    (
        "Aula 6 — Grafos e Algoritmos de Travessia",
        [
            "O que é (e o que não é)",
            "Peças: vértice e aresta",
            "Não direcionado e direcionado",
            "Vértices adjacentes e grau",
            "Caminhos (e ciclo)",
            "Grafos ponderados",
            "Como guardar: lista ou matriz",
            "BFS com fila",
        ],
    ),
]

TRES_CAMADAS = '''grafo          = o mapa (pontos + ligações)
lista / matriz = como o mapa é guardado na RAM
fila (deque)   = como a BFS anda no mapa
'''

LISTA_ADJ = '''vizinhos = {
    "Alice": ["Bruno", "Duda"],
    "Bruno": ["Alice", "Carlos"],
    "Carlos": ["Bruno"],
    "Duda": ["Alice"],
}
# Bruno e adjacente a Alice e Carlos
# grau("Bruno") = len(vizinhos["Bruno"])  →  2
'''

MATRIZ = '''#         Alice Bruno Carlos Duda
# Alice     0     1      0     1
# Bruno     1     0      1     0
# Carlos    0     1      0     0
# Duda      1     0      0     0
# 1 = tem aresta. Olhar a célula é O(1). A tabela inteira gasta O(V²).
'''

ARESTA_NAO_DIR = '''def adicionar_aresta(self, a, b):
    self.adicionar_vertice(a)
    self.adicionar_vertice(b)
    self.vizinhos[a].append(b)
    self.vizinhos[b].append(a)   # mao dupla
'''

ARESTA_DIR = '''def adicionar_arco(self, origem, destino):
    self.adicionar_vertice(origem)
    self.adicionar_vertice(destino)
    self.vizinhos[origem].append(destino)  # so um sentido
    # destino NÃO ganha origem
'''

ARESTA_PESO = '''def adicionar_aresta(self, a, b, km):
    self.vizinhos[a].append((b, km))
    self.vizinhos[b].append((a, km))
# CD --4km--> Centro   vira   ("Centro", 4) na listinha do CD
'''

GRAFO = '''from collections import deque


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


rua = Grafo()
rua.adicionar_aresta("Karla", "Brunno")
rua.adicionar_aresta("Brunno", "Carlos")
rua.adicionar_aresta("Carlos", "Erik")
rua.adicionar_aresta("Erik", "Natan")
rua.adicionar_aresta("Natan", "Gabriel")
rua.adicionar_aresta("Juan", "Gabriel")
print("Vizinhos do Gabriel:", rua.vizinhos["Gabriel"])
print("Caminho Gabriel → Karla:", rua.bfs("Gabriel", "Karla"))
'''


def escrever_aula6(doc, quebrar=True):
    if quebrar:
        e.quebra(doc)
    e.h1(doc, "Aula 6 — Grafos e Algoritmos de Travessia")
    e.objetivo(
        doc,
        "Entender o grafo como modelo de relações (não como lista nem como fila), "
        "ler vocabulário (direção, adjacência, grau, caminho, peso), escolher como "
        "guardar e achar caminho com BFS.",
    )
    e.aviso_ferramenta(doc, "VS Code")

    e.h_secao(doc, "O que é (e o que não é)")
    e.corpo(
        doc,
        "Grafo *não* é lista, *não* é fila, *não* é [[deque]] e *não* é um jeito de ler "
        "uma lista. Grafo é o *modelo*: pontos e ligações. Serve quando o dado não cabe "
        "numa fila única — mapa, amizades, ruas, dependências.",
    )
    e.codigo(doc, TRES_CAMADAS)
    e.bullets(
        doc,
        [
            "*Grafo* — o mapa (quem se liga a quem).",
            "*Lista / matriz* — como esse mapa mora na memória.",
            "*Fila (deque)* — só a BFS usa, para visitar camada por camada.",
        ],
    )
    e.dica(
        doc,
        "Árvore é um grafo *sem ciclo* e com um começo (raiz). Grafo é o caso geral: "
        "pode ter ciclo (Alice–Bruno–Carlos–Alice) e mais de um caminho entre dois pontos.",
    )
    e.figura(
        doc,
        "06_grafo.png",
        "Exemplo da aula: Karla–Brunno–Carlos–Erik–Natan–Gabriel–Juan. Vértices = pessoas, arestas = amizades.",
    )

    e.h_secao(doc, "Peças: vértice e aresta")
    e.bullets(
        doc,
        [
            "*Vértice* (ou nó) — um ponto: pessoa, bairro, `CD`.",
            "*Aresta* — uma ligação entre dois vértices. No não direcionado escrevemos "
            "`{Alice, Bruno}`; no direcionado, `CD → Centro`.",
        ],
    )
    e.corpo(
        doc,
        "No projeto final: o grafo *é o mapa*. Hash é a ficha do pacote. Heap é quem sai "
        "primeiro. Sem grafo você tem endereços soltos, sem rua entre eles — pergunta da Aula 8.",
    )

    e.h_secao(doc, "Não direcionado e direcionado")
    e.corpo(
        doc,
        "*Não direcionado* (o da aula e da logística simples): a ligação vale nos dois "
        "sentidos. Amizade, rua de mão dupla. Se A liga B, B liga A. Por isso o código "
        "faz *dois* `append`.",
    )
    e.codigo(doc, ARESTA_NAO_DIR, "mão dupla")
    e.corpo(
        doc,
        "*Direcionado*: a ligação tem seta. Rua de mão única, “seguir” numa rede, voo "
        "Congonhas → Galeão. CD chega no Centro; o inverso pode não existir. Só um `append`.",
    )
    e.codigo(doc, ARESTA_DIR, "mão única")
    e.figura(
        doc,
        "06_tipos.png",
        "Esquerda: aresta sem seta. Direita: arco com seta. No direcionado, grau de saída e grau de entrada separam.",
    )
    e.atencao(
        doc,
        "O `06_grafo.py` do curso é *não direcionado*. Não copie o segundo `append` se a "
        "rua for de mão única — você inventaria o caminho de volta.",
    )

    e.h_secao(doc, "Vértices adjacentes e grau")
    e.corpo(
        doc,
        "Dois vértices são *adjacentes* (vizinhos) se existe aresta entre eles. "
        "*Grau* de um vértice = quantas arestas tocam nele. Na lista de adjacência, "
        "`grau(v) = len(self.vizinhos[v])`.",
    )
    e.figura(
        doc,
        "06_grau.png",
        "Bruno é adjacente a Alice e Carlos. Grau(Bruno)=2. Duda não é vizinha de Bruno.",
    )
    e.codigo(doc, LISTA_ADJ, "adjacência e grau na lista")
    e.bullets(
        doc,
        [
            "Não direcionado: um número só (grau).",
            "Direcionado: *grau de saída* (quantas setas saem) e *grau de entrada* (quantas chegam).",
            "Folha da árvore da Aula 5 é o vértice de grau 1 (ou 0, a raiz sozinha) — mesma ideia, outro nome.",
        ],
    )

    e.h_secao(doc, "Caminhos (e ciclo)")
    e.corpo(
        doc,
        "Um *caminho* é uma sequência de vértices em que cada um é adjacente ao próximo. "
        "Neste curso o caminho *não repete* vértice. O *comprimento* é o número de arestas "
        "(Alice–Bruno–Carlos tem comprimento 2).",
    )
    e.figura(
        doc,
        "06_caminho.png",
        "Dois caminhos Alice → Carlos, ambos com 2 arestas. BFS devolve um deles, o de menos arestas.",
    )
    e.bullets(
        doc,
        [
            "*Caminho* — vai de um ponto ao outro, sem repetir vértice.",
            "*Ciclo* — caminho que volta ao começo (Alice–Bruno–Carlos–Duda–Alice). Árvore não tem; grafo pode ter.",
            "*Conexo* (não direcionado) — de qualquer um dá para chegar em qualquer outro.",
        ],
    )
    e.dica(
        doc,
        "BFS (fila) acha o caminho com *menos arestas*. Se as ruas tiverem km diferentes, "
        "menos arestas ≠ menos km — aí o peso entra (mais abaixo).",
    )

    e.h_secao(doc, "Grafos ponderados")
    e.corpo(
        doc,
        "No grafo *não ponderado* da aula, toda aresta vale 1. No *ponderado*, a aresta "
        "carrega um custo: km, minutos, pedágio. Guardamos o par `(vizinho, peso)` na listinha.",
    )
    e.codigo(doc, ARESTA_PESO, "aresta com km")
    e.figura(
        doc,
        "06_ponderado.png",
        "CD–Centro 4 km, Centro–Asa Sul 3 km. BFS ainda conta ruas, não soma km.",
    )
    e.atencao(
        doc,
        "A BFS desta aula *ignora* o peso. Caminho mais curto em km é outro algoritmo "
        "(Dijkstra) — fora do recorte de 2h30. No projeto, BFS no mapa não ponderado já vale.",
    )

    e.h_secao(doc, "Como guardar: lista ou matriz")
    e.corpo(
        doc,
        "O grafo é a ideia. Na RAM você escolhe uma *representação*. As duas guardam o "
        "*mesmo* mapa; mudam custo de memória e de consulta.",
    )
    e.figura(
        doc,
        "06_representacao.png",
        "Lista: para cada vértice, os vizinhos. Matriz: tabela V×V com 0/1 (ou o peso).",
    )
    e.codigo(doc, MATRIZ, "matriz do grafo A–B–C–D")
    e.bullets(
        doc,
        [
            "*Lista de adjacência* — o curso. Boa quando o grafo é *esparso* (poucas ruas). "
            "Olhar os vizinhos de v é percorrer `vizinhos[v]`.",
            "*Matriz de adjacência* — tabela V×V. “Existe aresta A–C?” é `O(1)`. Gasta `O(V²)` "
            "mesmo se quase tudo for zero.",
        ],
    )
    e.dica(
        doc,
        "`self.vizinhos` no código é um `dict` de listinhas — hash (Aula 4) apontando para "
        "listas (Aula 2). O *grafo* é o que isso representa, não o `dict` em si.",
    )

    e.h_secao(doc, "BFS com fila")
    e.corpo(
        doc,
        "Busca em largura visita camada por camada. A estrutura certa é a *fila* da Aula 3 "
        "(quem entra primeiro na visita sai primeiro). O caminho mais curto em *número de "
        "arestas* cai de graça se você guardar `veio_de`.",
    )
    e.passo(doc, 1, "Enfileira o início. Marca `veio_de[inicio] = None`.")
    e.passo(doc, 2, "`popleft` no atual. Se for o destino, para.")
    e.passo(doc, 3, "Para cada *adjacente* ainda não visto: marca `veio_de[vizinho] = atual` e enfileira.")
    e.passo(doc, 4, "No fim, anda `veio_de` de trás para frente e inverte — esse é o caminho.")
    e.codigo(doc, GRAFO, "exemplos/06_grafo.py")
    e.dica(
        doc,
        "Aqui o exemplo usa [[deque]] + [[popleft()]] para a BFS ficar `O(1)` na ponta da fila. "
        "É a mesma regra FIFO que vocês implementaram com nós. No projeto, pode colar a "
        "classe `Fila` da Aula 3 no lugar do deque. Vértices novos usam [[setdefault()]]. "
        "DFS usaria *pilha* — não garante menos arestas.",
    )

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática A — No papel, o vocabulário",
        "Desenhe 5 pessoas e algumas amizades. Marque: um par adjacente, o grau de cada um, "
        "um caminho de 2 arestas, um ciclo se houver. Diga se o desenho é direcionado ou não.",
    )
    e.pratica(
        doc,
        "Prática B — Rede social restrita",
        "Use o grafo da aula (`Karla` … `Juan`) no `06_grafo.py`. Mostre os vizinhos de "
        "Gabriel, amigos em comum (interseção das listas) e o caminho Gabriel → Karla com BFS. "
        "Confira com o desenho.",
    )
    e.pratica(
        doc,
        "Prática C — Mão única (no caderno)",
        "Pegue CD → Centro e *não* desenhe a volta. Escreva a lista de adjacência. "
        "O que muda se alguém pedir o caminho Centro → CD?",
    )

    e.checkpoint(
        doc,
        [
            "Em uma frase: grafo ≠ lista ≠ fila. O que cada um faz nesta aula?",
            "Diferença não direcionado / direcionado no `append`.",
            "O que é vértice adjacente e como lê o grau na lista.",
            "O que é caminho e por que ciclo existe no grafo e não na BST.",
            "Quando a matriz ganha da lista — e por que o curso usa lista.",
            "Por que BFS usa fila (e não pilha) para menos arestas.",
        ],
    )


def main() -> None:
    figuras.grafo()
    figuras_grafo.gerar()
    doc = e.novo_documento()
    e.dica(
        doc,
        "Rascunho isolado da Aula 6. A apostila completa (`gerar_apostila.py`) *não* "
        "muda. Quando este texto estiver pronto, ele entra no gerador principal.",
    )
    e.sumario(doc, SUMARIO)
    escrever_aula6(doc, quebrar=True)
    gerado = e.salvar(doc, SAIDA)
    print(f"Word: {gerado}")
    from gerar_apostila import atualizar_campos_e_pdf

    try:
        pdf = atualizar_campos_e_pdf(gerado)
        if pdf:
            print(f"PDF:  {pdf}")
        else:
            print("Campos do sumário atualizados no Word.")
    except Exception as exc:
        print(f"Não deu para atualizar os números no Word automaticamente: {exc}")
        print("Feche o arquivo no Word e rode de novo, nesta pasta: python aula6.py")


if __name__ == "__main__":
    main()
