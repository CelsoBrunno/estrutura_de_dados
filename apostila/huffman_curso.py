"""Huffman na apostila principal — exemplo que junta aulas do curso."""

from __future__ import annotations

import aula_huffman as h
import estilo as e


def escrever_huffman_curso(doc):
    e.quebra(doc)
    e.h1(doc, "Exemplo prático — Huffman junta o curso")
    e.objetivo(
        doc,
        "Ver um único problema (encolher `BANANA`) usando hash, árvore e a ideia do heap. "
        "Não substitui o projeto da Aula 8 e não é BST.",
    )
    e.aviso_ferramenta(doc, "VS Code")
    e.corpo(
        doc,
        "O simulador de logística junta hash + grafo + heap. Huffman é o *outro* exemplo "
        "de união: mesma caixa de ferramentas, outro recorte. Compactar texto. O código "
        "está em `exemplos/huffman.py`. A apostila extra (2h30) aprofunda o mesmo modelo.",
    )

    e.h_secao(doc, "O que cada aula faz aqui")
    e.corpo(
        doc,
        "Uma estrutura por papel. Se na apresentação alguém perguntar “isso é a BST?”, "
        "a resposta é não — e a tabela abaixo diz o porquê.",
    )
    e.bullets(
        doc,
        [
            "*Aula 4 (hash / `dict`)* — `contar`: cada letra é chave, o valor é quantas vezes "
            "aparece. No fim, outra tabela: letra → bits (`A` → `0`). O `00` *não* vira o "
            "ASCII do A; a tabela é que diz o que cada código significa.",
            "*Aula 2 (lista)* — a floresta é uma listinha de árvores. Tira duas, põe o pai de volta.",
            "*Aula 7 (heap / prioridade)* — sempre saem os *dois menores*. Na aula usamos "
            "`sort` + `pop(0)`. No projeto, isso é o min-heap. A árvore *final* de códigos "
            "*não* é heap.",
            "*Aula 5 (nó esquerda/direita)* — o mesmo desenho de ponteiros. Só que o lado "
            "não compara `valor < no.valor`. Esquerda = bit `0`, direita = bit `1`. "
            "A letra mora na *folha*.",
            "*Aula 3 (fila, de longe)* — descompactar lê os bits *na ordem*, um de cada vez. "
            "Não é BFS; é descer e voltar à raiz.",
        ],
    )
    e.dica(
        doc,
        "Grafo (Aula 6) *não* entra neste modelo. Huffman não é mapa de ruas. Se quiser "
        "ligar os dois, é outro problema (caminho + compactar o log da entrega).",
    )

    e.h_secao(doc, "O problema (8 bits para tudo)")
    e.corpo(
        doc,
        "`BANANA` tem 6 letras. Em ASCII cada uma paga 8 bits: `6 × 8 = 48`. O `A` aparece "
        "3 vezes, o `N` duas, o `B` uma. Huffman gasta *pouco bit no que aparece muito*.",
    )
    e.figura(
        doc,
        "huff_ideia.png",
        "À esquerda, cada letra paga 8 bits. À direita, o A (o mais comum) paga 1 bit.",
    )

    e.h_secao(doc, "Na mão: contar, juntar, ler")
    e.corpo(
        doc,
        "Escreva `B A N A N A` e conte *antes* do código. Cada letra vira uma árvore de "
        "um nó (peso = frequência). Isso é a *floresta* — ainda não há uma raiz única.",
    )
    e.figura(
        doc,
        "huff_freq.png",
        "A=3, N=2, B=1. Três árvores soltas. Huffman não insere letra numa BST.",
    )
    e.codigo(doc, h.CONTAR, "Aula 4 — contar por chave")
    e.passo(doc, 1, "Floresta: `A(3)`, `N(2)`, `B(1)`.")
    e.passo(
        doc,
        2,
        "Menores: `B(1)` e `N(2)`. Pai peso 3, esquerda B, direita N. Sobram `A(3)` e o pai `(3)`.",
    )
    e.passo(
        doc,
        3,
        "Empate 3 e 3. `A` tem `ordem` menor, sai primeiro, vira filho *esquerdo*. "
        "O pai `BN` vai à direita. Sobra *uma* árvore, peso 6.",
    )
    e.codigo(doc, h.JUNTAR, "Aula 7 — os dois menores (sort no lugar do heap)")
    e.figura(
        doc,
        "huff_juntar.png",
        "Duas junções. No empate, A entra à esquerda porque a ordem é menor — não porque A < B.",
    )
    e.figura(
        doc,
        "huff_arvore.png",
        "A = 0, B = 10, N = 11. Folha = letra. Nó interno = só peso.",
    )
    e.atencao(
        doc,
        "Huffman *não* é BST. Também *não* traduz `0` para o ASCII do A (`01000001`). "
        "A folha guarda o símbolo `A`; a tabela guarda `A → 0`. Sem a tabela (ou a árvore), "
        "`0` é só um bit.",
    )

    e.h_secao(doc, "Compactar e descompactar")
    e.corpo(
        doc,
        "Compactar: para cada letra, olhe a tabela e emende os bits. Descompactar: comece "
        "na raiz, um bit de cada vez; na folha emita a letra e *volte à raiz*.",
    )
    e.codigo(doc, h.BITS, "letra → bits (a tabela, não o ASCII)")
    e.figura(
        doc,
        "huff_encode.png",
        "B=10, A=0, N=11, A=0, N=11, A=0 → 100110110. De 48 bits para 9.",
    )
    e.codigo(doc, h.LER, "bits → letra (desce até a folha)")
    e.figura(
        doc,
        "huff_decode.png",
        "Os dois primeiros bits 10 não são “dez”: um passo (1) e outro (0) até a folha B.",
    )
    e.dica(
        doc,
        "O arquivo `.huff` da aula é texto de propósito: cabeçalho `HUFFMAN`, linhas "
        "`letra código`, um `---`, depois a bitstring. Compactar e descompactar usam a "
        "*mesma* tabela. Por isso ela viaja junto com os bits.",
    )

    e.h_secao(doc, "Prática")
    e.pratica(
        doc,
        "Na mão — ABRA",
        "Conte A, B, R. Monte a floresta, faça as junções, escreva a tabela e os bits. "
        "Rode `exemplos/huffman.py` com `texto = \"ABRA\"` e compare. Os bits podem "
        "diferir se o empate sair outro; o tamanho e a volta do texto é que precisam bater.",
    )
    e.pratica(
        doc,
        "No código",
        "Troque o texto por uma palavra da turma. Confira se `descompactar` devolve a "
        "mesma string. Abra o `.huff` e aponte: tabela (Aula 4) e árvore (Aula 5) são o "
        "mesmo mapa; o `sort` dos dois menores é o papel do heap (Aula 7).",
    )
    e.checkpoint(
        doc,
        [
            "Dizer, numa frase, o papel de hash, árvore e heap neste exemplo.",
            "Por que Huffman não é a BST da Aula 5.",
            "Por que `0` não é o ASCII do A.",
            "Descompactar `100110110` na árvore do BANANA, bit a bit.",
            "Rodar `python exemplos/huffman.py` e ver o texto voltar.",
        ],
    )
