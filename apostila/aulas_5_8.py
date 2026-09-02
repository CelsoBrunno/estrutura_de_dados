import estilo as e

BST = '''class NoArvore:
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

    def pre_ordem(self, no):
        if no:
            print(no.valor, end=" ")
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def pos_ordem(self, no):
        if no:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor, end=" ")


arvore = ArvoreBusca()
for codigo in (50, 30, 70, 20, 40):
    arvore.inserir(codigo)
print("Em ordem:")
arvore.em_ordem(arvore.raiz)
print("\\nPré-ordem:")
arvore.pre_ordem(arvore.raiz)
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


rede = Grafo()
rede.adicionar_aresta("Alice", "Bruno")
rede.adicionar_aresta("Bruno", "Carlos")
rede.adicionar_aresta("Alice", "Duda")
print("Amigos de Bruno:", rede.vizinhos["Bruno"])
print("Caminho Alice → Carlos:", rede.bfs("Alice", "Carlos"))
'''

HEAP = '''class MinHeap:
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


heap = MinHeap()
for n in (5, 1, 4, 2):
    heap.inserir(n)
print("Extrai em ordem:", heap.extrair_min(), heap.extrair_min(), heap.extrair_min())
'''

TRIAGEM = '''class Triagem:
    def __init__(self):
        self.heap = MinHeap()
        self.ordem = 0

    def chegar(self, gravidade, nome):
        # tupla: menor gravidade numérica = mais urgente (1 = crítico)
        self.heap.inserir((gravidade, self.ordem, nome))
        self.ordem += 1
        print(f"{nome} entrou com gravidade {gravidade}.")

    def atender(self):
        gravidade, _, nome = self.heap.extrair_min()
        print(f"Atendendo {nome} (gravidade {gravidade})")


hospital = Triagem()
hospital.chegar(5, "Paciente leve")
hospital.chegar(1, "Paciente crítico")
hospital.chegar(3, "Paciente moderado")
hospital.atender()
hospital.atender()
'''

LOGISTICA = '''class SistemaLogistica:
    def __init__(self):
        self.rotas = Grafo()          # Aula 6
        self.pacotes = TabelaHash()   # Aula 4
        self.prioridade = MinHeap()   # Aula 7
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


# Monte um exemplo pequeno: 4 bairros, 3 pacotes, e rode processar_entregas.
'''


def escrever_aulas_5_8(doc):
    _aula5(doc)
    _aula6(doc)
    _aula7(doc)
    _aula8(doc)


def _aula5(doc):
    e.h_aula(doc, 5, "Árvores Binárias e Árvores de Busca (BST)")
    e.objetivo(
        doc,
        "Sair das estruturas lineares: inserir numa BST pela regra esquerda/direita e "
        "percorrer em ordem, pré-ordem e pós-ordem.",
    )
    e.corpo(
        doc,
        "Hash acha pela chave, mas não entrega os dados ordenados. Árvore organiza "
        "hierarquia e, na BST, a busca média cai para `O(log n)` se estiver equilibrada.",
    )

    e.h_secao(doc, "Vocabulário")
    e.bullets(
        doc,
        [
            "Raiz — o primeiro nó. Folhas — nós sem filhos. Altura — níveis até a folha mais fundo.",
            "Árvore binária — cada nó tem no máximo dois filhos.",
            "BST — à esquerda, valores menores; à direita, maiores.",
        ],
    )
    e.figura(
        doc,
        "05_bst.png",
        "Inserção 50, 30, 70, 20, 40. Em-ordem lê de baixo à esquerda até a direita: 20 30 40 50 70.",
    )
    e.atencao(
        doc,
        "Se você inserir 1, 2, 3, 4, 5 nessa ordem, a BST vira uma lista à direita. "
        "Aí a busca volta a ser `O(n)`. Equilíbrio (AVL/vermelho-preto) fica para depois; "
        "hoje o aluno precisa ver o caso ruim.",
    )

    e.h_secao(doc, "Live coding: inserção e travessias")
    e.codigo(doc, BST, "exemplos/05_bst.py")
    e.dica(
        doc,
        "Em-ordem numa BST imprime crescente. Use isso como prova de que a regra "
        "esquerda/direita está certa.",
    )

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática — Catálogo ordenado / categorias",
        "Insira códigos de produto (ou nomes de categoria comparáveis) e liste em ordem. "
        "Opcional: pense no sistema de pastas do computador como analogia de hierarquia — "
        "a BST da prática é a versão com regra de busca.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Inserir cinco valores e desenhar a árvore no papel.",
            "Rodar em-ordem e conferir se saiu crescente.",
            "Explicar a diferença de objetivo entre hash (`O(1)` médio) e BST (ordem + `O(log n)`).",
        ],
    )


def _aula6(doc):
    e.h_aula(doc, 6, "Grafos e Algoritmos de Travessia")
    e.objetivo(
        doc,
        "Modelar vértices e arestas, escolher lista de adjacência e achar o caminho mais "
        "curto em arestas com BFS — usando fila.",
    )
    e.corpo(
        doc,
        "Árvore é um grafo sem ciclo, com um ancestral comum. Grafo permite ciclo: "
        "Alice é amiga de Bruno, Bruno de Carlos, Carlos de Alice.",
    )
    e.figura(
        doc,
        "06_grafo.png",
        "Rede da prática: amizades são arestas. O caminho mais curto Alice–Carlos tem duas arestas.",
    )

    e.h_secao(doc, "Matriz versus lista de adjacência")
    e.bullets(
        doc,
        [
            "Matriz — tabela V×V. Olhar se existe aresta é `O(1)`, mas gasta `O(V²)` de memória.",
            "Lista — para cada vértice, a lista de vizinhos. Melhor quando o grafo é esparso "
            "(poucas arestas). É o que usamos no curso.",
        ],
    )

    e.h_secao(doc, "BFS com fila")
    e.corpo(
        doc,
        "Busca em largura visita camada por camada. A estrutura certa é a fila da Aula 3 "
        "(quem entra primeiro na visita sai primeiro). O caminho mais curto em número de "
        "arestas cai de graça se você guardar `veio_de`.",
    )
    e.codigo(doc, GRAFO, "exemplos/06_grafo.py")
    e.dica(
        doc,
        "Aqui o exemplo usa `deque.popleft` para a BFS ficar `O(1)` na ponta da fila. "
        "É a mesma regra FIFO que vocês implementaram com nós. No projeto, pode colar a "
        "classe `Fila` da Aula 3 no lugar do deque.",
    )

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática — Rede social restrita",
        "Cadastre 5 pessoas e algumas amizades. Mostre amigos em comum (interseção das "
        "listas) e o caminho mais curto entre dois usuários com BFS.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Desenhar o grafo da prática no papel (círculos e linhas).",
            "Rodar BFS e conferir o caminho com o desenho.",
            "Dizer por que DFS (pilha) não garante o menor número de arestas.",
        ],
    )


def _aula7(doc):
    e.h_aula(doc, 7, "Heaps e preparação para o projeto")
    e.objetivo(
        doc,
        "Manter o menor (ou maior) elemento no topo com um heap em array, usar isso como "
        "fila de prioridade e receber o briefing do projeto final.",
    )
    e.corpo(
        doc,
        "Fila comum atende por ordem de chegada. Hospital, suporte e entrega urgente "
        "atendem por gravidade. Heap é a árvore (quase) completa guardada num array, "
        "em que pai ≤ filhos (min-heap).",
    )
    e.figura(
        doc,
        "07_heap.png",
        "A árvore e o array são a mesma estrutura. Filho esquerdo de i está em 2*i+1.",
    )

    e.h_secao(doc, "Índices no array")
    e.bullets(
        doc,
        [
            "Filho esquerdo de `i`: `2*i + 1`. Filho direito: `2*i + 2`. Pai: `(i - 1) // 2`.",
            "Inserir: coloca no fim e “sobe” trocando com o pai enquanto for menor.",
            "Extrair o topo: pega o índice 0, põe o último no lugar e “desce”.",
        ],
    )
    e.codigo(doc, HEAP, "exemplos/07_heap.py")
    e.dica(
        doc,
        "No Python do dia a dia existe `heapq` (min-heap nativo). Mostre um `heappush` / "
        "`heappop` no quadro depois que o heap próprio funcionar. No projeto, vale a "
        "estrutura que você souber defender — a do zero prova que entendeu o índice.",
    )

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática — Triagem hospitalar",
        "Pacientes entram com um número de gravidade. Quem tem o menor número (mais "
        "crítico) sai primeiro, mesmo tendo chegado depois. Use o heap. O contador `ordem` "
        "desempata quem tem a mesma gravidade (FIFO entre iguais).",
    )
    e.codigo(doc, TRIAGEM, "exemplos/07_triagem.py")

    e.h_secao(doc, "Briefing do Projeto Final")
    e.corpo(
        doc,
        "Na Aula 8 vocês recebem um simulador de logística. Peças obrigatórias:",
    )
    e.bullets(
        doc,
        [
            "Grafo — mapa de bairros / pontos de entrega (BFS para o caminho).",
            "Tabela hash — dados do pacote pela chave `id`.",
            "Heap — ordem de saída pela urgência.",
            "Opcional: fila de veículos, pilha de “desfazer último despacho”, array de baús com capacidade.",
        ],
    )
    e.atencao(
        doc,
        "Quem chegar na Aula 8 sem hash, grafo e heap vai sofrer. Feche as práticas 4, 6 e 7. "
        "Não recomece do zero na apresentação.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Inserir quatro números no min-heap e extrair em ordem crescente.",
            "Atender o paciente crítico antes do leve.",
            "Escrever no caderno qual estrutura vai para cada peça do simulador.",
        ],
    )


def _aula8(doc):
    e.h_aula(doc, 8, "Projeto Final (PBL Integrado)")
    e.objetivo(
        doc,
        "Juntar as estruturas num simulador de logística, defender as escolhas em 5 a 8 "
        "minutos e entregar um README que outra pessoa consiga rodar.",
    )
    e.atencao(
        doc,
        "Esta aula não é para inventar heap na hora. É para integrar, quebrar, consertar e apresentar.",
    )

    e.h_secao(doc, "O desafio")
    e.corpo(
        doc,
        "Há um centro de distribuição e bairros ligados por ruas (grafo). Pacotes têm id, "
        "destino e urgência. O sistema registra rotas, aceita pacotes e processa entregas "
        "do mais urgente para o menos urgente, mostrando o caminho no mapa.",
    )
    e.figura(
        doc,
        "08_logistica.png",
        "Mapa (grafo) + ficha do pacote (hash) + ordem de saída (heap). P2 (urgência 1) sai primeiro.",
    )
    e.codigo(doc, LOGISTICA, "exemplos/08_logistica.py")

    e.h_secao(doc, "O que a avaliação cobra")
    e.bullets(
        doc,
        [
            "Por que hash para o pacote e não uma BST (ou o contrário, se fizer sentido).",
            "Por que grafo no mapa — e não uma lista de endereços soltos.",
            "Por que heap na urgência — e não a fila FIFO da Aula 3.",
            "Um limite que você conhece: BST degenerada, colisão de hash, heap só no array.",
        ],
    )

    e.h_secao(doc, "Roteiro da apresentação (5 a 8 minutos)")
    e.bullets(
        doc,
        [
            "1. Qual o problema? (pacotes com urgência + mapa da cidade).",
            "2. Rodar o cadastro de rotas e de pacotes.",
            "3. Processar entregas: o crítico sai primeiro; o caminho aparece.",
            "4. No código: apontar hash, grafo/BFS e heap.",
            "5. Uma frase do que você não fez de propósito (GPS real, banco, interface web).",
        ],
    )

    e.h_secao(doc, "README (entregue junto)")
    e.codigo(
        doc,
        "# Simulador de logística\n"
        "O que é: entregas com urgência sobre um mapa em grafo.\n\n"
        "Como o dado anda:\n"
        "1. rotas (Grafo) — bairros e ruas\n"
        "2. pacotes (TabelaHash) — id → destino e urgência\n"
        "3. prioridade (MinHeap) — quem sai primeiro\n"
        "4. BFS — caminho depósito → destino\n\n"
        "Como rodar:\n"
        "python exemplos/08_logistica.py\n",
        "README.md",
    )

    e.h_secao(doc, "Checklist antes de apresentar")
    e.pratica(
        doc,
        "Prática",
        "Marque só o que o programa já faz de verdade (não o que você pretende fazer).",
    )
    e.bullets(
        doc,
        [
            "[ ] Três ou mais pacotes; o de menor urgência numérica sai primeiro.",
            "[ ] BFS devolve um caminho que existe no grafo (teste com o desenho).",
            "[ ] Dá para apontar no código: hash, heap, grafo.",
            "[ ] README diz o que é, como rodar e o que não faz.",
            "[ ] Nomes de classe e arquivo fazem sentido para outra pessoa.",
        ],
    )
    e.corpo(doc, "O que não precisa: banco de dados, site Django, API, login, mapa real de GPS.")
