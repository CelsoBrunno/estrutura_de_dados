"""Apêndice — Glossário de funções usadas no curso."""

import estilo as e

NOMES = [
    "ord()",
    "sum()",
    "str()",
    "len()",
    "append()",
    "pop()",
    "deque",
    "appendleft()",
    "popleft()",
    "setdefault()",
    "%",
]


def escrever_glossario(doc):
    e.quebra(doc)
    e.h1(doc, "Apêndice — Glossário de funções")
    e.corpo(
        doc,
        "Ao longo da apostila, nomes em teal sublinhado (como [[ord()]]) levam até aqui. "
        "Este glossário explica só o que o curso usa — não é manual completo do Python.",
    )
    e.dica(
        doc,
        "No Word/PDF, clique no nome da função no texto da aula para saltar à entrada. "
        "No sumário, abra este apêndice e use a lista abaixo.",
    )

    e.h_secao(doc, "Índice rápido")
    e.indice_glossario(doc, NOMES)

    e.entrada_glossario(
        doc,
        "ord()",
        "Recebe *um* caractere e devolve o número inteiro que o representa na tabela "
        "Unicode/ASCII. No hash didático da Aula 4, somamos esses números para transformar "
        "texto em índice.",
        'print(ord("A"))  # 65\nprint(ord("u"))  # 117\nprint(ord("0"))  # 48',
    )

    e.entrada_glossario(
        doc,
        "sum()",
        "Soma os números de uma sequência. Em `sum(ord(c) for c in chave)`, o Python "
        "percorre cada caractere, chama [[ord()]] e acumula o total.",
        'print(sum([1, 2, 3]))           # 6\nprint(sum(ord(c) for c in "ab"))  # 97+98 = 195',
    )

    e.entrada_glossario(
        doc,
        "str()",
        "Converte o valor para texto (`str`). No hash usamos `str(chave)` para aceitar "
        "chave que não seja string (ex.: um número) sem quebrar o `for c in ...`.",
        'print(str(20))      # "20"\nprint(str("u001"))  # "u001"',
    )

    e.entrada_glossario(
        doc,
        "len()",
        "Devolve quantos itens há na coleção (lista, `deque`, string…). No heap e nas "
        "filas, `len(self.dados)` diz o tamanho atual.",
        'print(len("abc"))     # 3\nprint(len([10, 20]))  # 2',
    )

    e.entrada_glossario(
        doc,
        "append()",
        "Método de lista: coloca um item *no final*. Em hash, cada balde é uma listinha; "
        "`baldes[indice].append([chave, valor])` acrescenta o par naquele balde. Em pilha, "
        "`append` empilha no topo (fim da lista).",
        "lista = [1, 2]\nlista.append(3)\nprint(lista)  # [1, 2, 3]",
    )

    e.entrada_glossario(
        doc,
        "pop()",
        "Remove e devolve um item. Sem argumento, remove o *último* (`O(1)` na `list`) — "
        "é o desempilhar. `lista.pop(0)` remove o primeiro, mas na `list` do Python isso "
        "é `O(n)` (todos andam). Por isso fila usa [[deque]] + [[popleft()]].",
        "pilha = [1, 2, 3]\nprint(pilha.pop())  # 3\nprint(pilha)       # [1, 2]",
    )

    e.entrada_glossario(
        doc,
        "deque",
        "Fila de duas pontas (`collections.deque`). Entra e sai nas duas extremidades em "
        "`O(1)`. No Call Center e no BFS usamos `deque` no lugar de `list.pop(0)`.",
        "from collections import deque\nfila = deque([\"Ana\", \"Bia\"])\nfila.append(\"Caio\")\nprint(fila.popleft())  # Ana",
    )

    e.entrada_glossario(
        doc,
        "appendleft()",
        "Método do [[deque]]: insere no *início* em `O(1)`. No Call Center, o desfazer "
        "usa `appendleft` para a Maria voltar à frente da fila (não ao fim).",
        "from collections import deque\nfila = deque([\"Bia\", \"Caio\"])\nfila.appendleft(\"Maria\")\nprint(fila)  # deque(['Maria', 'Bia', 'Caio'])",
    )

    e.entrada_glossario(
        doc,
        "popleft()",
        "Método do [[deque]]: remove do *início* em `O(1)`. É o “próximo da fila” (FIFO) "
        "e o passo da BFS que tira o vértice da frente.",
        "from collections import deque\nfila = deque([\"Ana\", \"Bia\"])\nprint(fila.popleft())  # Ana",
    )

    e.entrada_glossario(
        doc,
        "setdefault()",
        "Método de `dict`: se a chave *não* existe, cria com o valor padrão e devolve; "
        "se já existe, só devolve o valor atual. No grafo: "
        "`self.vizinhos.setdefault(nome, [])` garante a listinha de vizinhos sem `if` extra.",
        'g = {}\ng.setdefault("CD", []).append("Centro")\nprint(g)  # {"CD": ["Centro"]}',
    )

    e.entrada_glossario(
        doc,
        "%",
        "Operador *resto da divisão* (módulo). `262 % 5` vale `2`: 5 cabe 52 vezes em 262 "
        "e sobram 2. No hash, `soma % tamanho` força o índice a ficar entre `0` e "
        "`tamanho - 1`.",
        "print(10 % 3)   # 1\nprint(262 % 5)  # 2\nprint(7 % 7)    # 0",
    )

    e.corpo(
        doc,
        "Professor: Celso Brunno Rocha Custódio de Campos. Curso de Python — Estruturas de Dados.",
    )
