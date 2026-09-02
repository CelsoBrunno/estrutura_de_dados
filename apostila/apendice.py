import estilo as e


def escrever_apendice(doc):
    e.quebra(doc)
    e.h1(doc, "Apêndice — Código de referência")
    e.corpo(
        doc,
        "Os arquivos abaixo estão na pasta `exemplos/`. Rode sempre com o terminal na pasta "
        "do projeto. Este apêndice é o mapa — o código completo está nos arquivos.",
    )
    e.bullets(
        doc,
        [
            "`exemplos/01_array.py` e `01_mochila.py` — array estático e PBL da mochila.",
            "`exemplos/02_lista.py` e `02_reprodutor.py` — lista simples e lista dupla.",
            "`exemplos/03_pilha_fila.py` e `03_callcenter.py` — nós LIFO/FIFO e PBL do Call Center.",
            "`exemplos/04_hash.py` — tabela com encadeamento.",
            "`exemplos/05_bst.py` — inserção e travessias.",
            "`exemplos/06_grafo.py` — lista de adjacência e BFS.",
            "`exemplos/07_heap.py` e `07_triagem.py` — min-heap e prioridade.",
            "`exemplos/08_logistica.py` — simulador integrado (referência da Aula 8).",
        ],
    )
    e.dica(
        doc,
        "Se o seu projeto final divergir desta referência, tudo bem — desde que você "
        "aponte no código hash, grafo e heap e o programa rode do zero.",
    )
    e.corpo(
        doc,
        "Professor: Celso Brunno Rocha Custódio de Campos. Curso de Python — Estruturas de Dados.",
    )
