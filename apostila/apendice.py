import estilo as e


GABARITO_HASH_A = '''"u001": ord('u')+ord('0')+ord('0')+ord('1') = 117+48+48+49 = 262
262 % 5 = 2  → balde 2

"u002": 117+48+48+50 = 263
263 % 5 = 3  → balde 3

"ab": 97+98 = 195
195 % 5 = 0  → balde 0

"ba": 98+97 = 195
195 % 5 = 0  → balde 0  (colide com "ab")
'''

GABARITO_HASH_B = '''[0] []
[1] []
[2] [["u001", "João"]]
[3] [["u002", "Maria"]]
[4] []
'''

GABARITO_HASH_C = '''[0] [["ab", "..."], ["ba", "..."]]   ← colisão
[1] []
[2] [["u001", "João"]]
[3] [["u002", "Maria"]]
[4] []
'''


def escrever_apendice(doc):
    e.quebra(doc)
    e.h1(doc, "Apêndice — Código de referência")
    e.corpo(
        doc,
        "Os arquivos abaixo estão na pasta `exemplos/`. Rode sempre com o terminal na pasta "
        "do projeto. Este apêndice é o mapa — o código completo está nos arquivos. "
        "Funções do Python (`ord`, `deque`, etc.) estão no *Apêndice — Glossário de funções*.",
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

    e.h_secao(doc, "Gabarito — Aula 4 (hash)")
    e.atencao(
        doc,
        "Só confira depois de tentar o exercício na mão da Aula 4.",
    )
    e.corpo(doc, "Parte A — índices (tamanho `5`):")
    e.codigo(doc, GABARITO_HASH_A)
    e.corpo(doc, "Parte B — depois de inserir `u001` e `u002`:")
    e.codigo(doc, GABARITO_HASH_B)
    e.corpo(doc, "Parte C — exemplo com `ab` / `ba` (colisão no balde 0):")
    e.codigo(doc, GABARITO_HASH_C)
    e.corpo(doc, "Parte D — busca mental:")
    e.bullets(
        doc,
        [
            "Abre *um* balde (o do índice calculado).",
            "Compara a *chave* de cada par (`par[0]`), não o valor.",
            "Tabela de tamanho `1`: tudo cai no balde `0` → vira uma lista só → busca `O(n)`.",
        ],
    )

    e.corpo(
        doc,
        "Professor: Celso Brunno Rocha Custódio de Campos. Curso de Python — Estruturas de Dados.",
    )