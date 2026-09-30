"""Aula extra — compactação Huffman (apostila de um encontro)."""

from __future__ import annotations

from pathlib import Path

import estilo as e

EXEMPLO = (Path(__file__).resolve().parent.parent / "exemplos" / "huffman.py").read_text(
    encoding="utf-8"
)

CONTAR = '''def contar(texto):
    freq = {}
    for letra in texto:
        freq[letra] = freq.get(letra, 0) + 1
    return freq
'''

JUNTAR = '''floresta.sort(key=lambda no: (no.freq, no.ordem))
a = floresta.pop(0)          # o menor
b = floresta.pop(0)          # o segundo menor
pai = No(a.freq + b.freq, esquerda=a, direita=b)
floresta.append(pai)
'''

BITS = '''codigos = {"A": "0", "B": "10", "N": "11"}
bits = "".join(codigos[letra] for letra in "BANANA")
# 10 + 0 + 11 + 0 + 11 + 0  ->  100110110
'''

LER = '''no = raiz
for bit in bits:
    no = no.esquerda if bit == "0" else no.direita
    if no.eh_folha():
        print(no.simbolo, end="")
        no = raiz
'''


def escrever_preambulo(doc):
    e.h1(doc, "Antes de começar")
    e.corpo(
        doc,
        "Esta apostila é de *um* encontro (2h30). O alvo não é o ZIP completo: é a ideia "
        "que faz o ZIP funcionar — gastar poucos bits no que aparece muito.",
    )
    e.objetivo(
        doc,
        "Sair da aula sabendo compactar e descompactar `BANANA` na mão, explicar por que "
        "o código precisa ser prefixo-livre, e rodar `exemplos/huffman.py`.",
    )

    e.h_secao(doc, "O que você vai construir hoje")
    e.bullets(
        doc,
        [
            "Uma tabela de frequência (o mesmo espírito da Aula 4 — contar por chave).",
            "Uma floresta de árvores que vai juntando os dois menores até sobrar uma.",
            "Uma árvore de Huffman: folha = letra, ramo esquerdo = `0`, direito = `1`.",
            "Um arquivo `.huff` com a tabela e os bits, e a volta ao texto original.",
        ],
    )

    e.h_secao(doc, "O que precisa já saber")
    e.corpo(
        doc,
        "Não é a primeira aula do curso. Você já viu nó com `esquerda`/`direita` (Aula 5) "
        "e a ideia de “sempre o menor na frente” (Aula 7). Hoje a árvore *não* é BST: "
        "não comparamos letra com letra para decidir o lado. O lado é só o bit.",
    )
    e.bullets(
        doc,
        [
            "Classe com atributos, `if` e `for`.",
            "Dicionário: `freq[letra] = freq.get(letra, 0) + 1`.",
            "Árvore: um nó, dois filhos, folha é o nó sem (ou com) dado útil.",
        ],
    )
    e.dica(
        doc,
        "Na lousa usamos uma *lista* ordenada para achar os dois menores. Na Aula 7 isso "
        "vira heap — mesmo serviço, mais barato. Não invente heap hoje se ainda não fechou "
        "a Aula 7: a lógica é a que importa.",
    )

    e.h_secao(doc, "Roteiro das 2h30")
    e.bullets(
        doc,
        [
            "0:00–0:20 — o problema dos 8 bits e o prefixo-livre (figuras na apostila).",
            "0:20–0:55 — `BANANA` na mão: contar, juntar, árvore, bits.",
            "0:55–1:10 — descompactar bit a bit, sem pular.",
            "1:10–2:00 — live coding (`exemplos/huffman.py`) e o arquivo `.huff`.",
            "2:00–2:20 — o que o ZIP acrescenta (DEFLATE, uma ideia).",
            "2:20–2:30 — prática: compactar `ABRA` na mão e conferir no código.",
        ],
    )
    e.atencao(
        doc,
        "Não pule o exemplo na mão. Quem só copia o `.py` não sabe dizer *por que* o `A` "
        "ganhou o bit `0`. Na prova e na apresentação, isso pesa mais que a sintaxe.",
    )


def escrever_aula(doc):
    e.quebra(doc)
    e.h1(doc, "Aula extra — Compactação com Huffman")

    e.h_secao(doc, "O problema (8 bits para tudo)")
    e.corpo(
        doc,
        "Um arquivo de texto em ASCII (e o `str` “cru” que você imagina na RAM) trata "
        "cada caractere como um bloco de 8 bits. A letra `A` e a letra `Z` custam *igual*, "
        "mesmo se o `A` aparecer mil vezes e o `Z` uma.",
    )
    e.corpo(
        doc,
        "`BANANA` tem 6 letras. Em ASCII: `6 × 8 = 48` bits. Só que o `A` aparece 3 vezes, "
        "o `N` duas, o `B` uma. Se o frequente puder ser um bit só, o arquivo encolhe.",
    )
    e.figura(
        doc,
        "huff_ideia.png",
        "À esquerda, cada letra paga 8 bits. À direita, o A (o mais comum) paga 1 bit.",
    )

    e.h_secao(doc, "Resposta em uma frase")
    e.corpo(
        doc,
        "Huffman monta uma árvore em que letra frequente fica *perto da raiz* (código curto) "
        "e letra rara fica *longe* (código longo). Compactar é descer a árvore e anotar 0/1. "
        "Descompactar é ler os bits, descer, emitir a folha e voltar à raiz.",
    )
    e.dica(
        doc,
        "David Huffman inventou isso em 1952, ainda aluno. A pergunta do professor era: "
        "qual o melhor código se eu já conheço as frequências? A resposta é esta árvore.",
    )

    e.h_secao(doc, "Código prefixo-livre")
    e.corpo(
        doc,
        "Código curto só funciona se o descompressor souber *onde* um código acaba e o "
        "próximo começa. A regra: *nenhum código é prefixo de outro*. Isso se chama "
        "código prefixo-livre.",
    )
    e.bullets(
        doc,
        [
            "Pode: `A=0`, `B=10`, `N=11`. O bit `0` sozinho já é A. `10` não começa com um A isolado no meio do caminho — você só emite quando chega na *folha*.",
            "Não pode: `A=0` e `B=00`. O primeiro `0` já seria A. O `B` nunca nasce.",
            "A árvore *garante* a regra: só emite na folha. Caminho interno nunca é letra.",
        ],
    )
    e.figura(
        doc,
        "huff_prefixo.png",
        "Se um código começa o outro, o leitor não sabe quando cortar. A árvore impede isso.",
    )
    e.atencao(
        doc,
        "Huffman *não* é BST. Na BST, esquerda/direita dependem de `valor < no.valor`. "
        "Aqui esquerda/direita são só os bits `0` e `1`. A letra mora na folha.",
    )

    e.h_secao(doc, "Exemplo na mão: BANANA")
    e.corpo(
        doc,
        "Escreva `B A N A N A` no quadro. Peça para a turma contar *antes* de abrir o código. "
        "Se o número não bater, o resto da aula desanda.",
    )
    e.figura(
        doc,
        "huff_freq.png",
        "A=3, N=2, B=1. Cada letra vira uma árvore de um nó só, com peso = frequência.",
    )
    e.codigo(doc, CONTAR, "contar frequências")
    e.passo(
        doc,
        1,
        "Três folhas: `A(3)`, `N(2)`, `B(1)`. Isso é a *floresta*. Ainda não há pai.",
    )

    e.h_secao(doc, "Juntar sempre os dois menores")
    e.corpo(
        doc,
        "Enquanto houver mais de uma árvore na floresta: tire as duas de *menor peso*, "
        "crie um pai cujo peso é a soma, e devolva o pai. Empate de peso: ganha quem "
        "entrou primeiro (`ordem` menor). No código, `A` entra antes de `B` e `N` "
        "(ordem alfabética na montagem).",
    )
    e.codigo(doc, JUNTAR, "uma junção")
    e.passo(
        doc,
        2,
        "Menores: `B(1)` e `N(2)`. Pai peso `3`, esquerda `B`, direita `N`. Floresta: `A(3)` e pai `(3)`.",
    )
    e.passo(
        doc,
        3,
        "Empate 3 e 3. `A` tem `ordem` menor, sai primeiro, vira filho *esquerdo*. "
        "O pai `BN` vira filho direito. Sobra *uma* árvore, peso 6 — fim.",
    )
    e.figura(
        doc,
        "huff_juntar.png",
        "Duas junções. Na segunda, A e o pai BN têm o mesmo peso; A entra à esquerda.",
    )
    e.dica(
        doc,
        "Se a turma juntar em outra ordem de empate, os *bits* mudam (`A=1` em vez de `A=0`), "
        "mas o tamanho continua 9 bits e o texto volta igual — desde que compactar e "
        "descompactar usem a *mesma* árvore. Por isso o arquivo `.huff` guarda a tabela.",
    )

    e.h_secao(doc, "Ler os bits na árvore")
    e.corpo(
        doc,
        "Raiz até a folha: cada passo à esquerda anota `0`, à direita anota `1`. "
        "O código da letra é o caminho.",
    )
    e.figura(
        doc,
        "huff_arvore.png",
        "A está logo à esquerda da raiz (código 0). B = 10, N = 11.",
    )
    e.bullets(
        doc,
        [
            "`A`: esquerda → `0`.",
            "`B`: direita, esquerda → `10`.",
            "`N`: direita, direita → `11`.",
        ],
    )

    e.h_secao(doc, "Compactar letra a letra")
    e.corpo(
        doc,
        "Troque cada letra pelo código e concatene. Não coloque espaço no arquivo real; "
        "no quadro o espaço só ajuda a enxergar.",
    )
    e.codigo(doc, BITS, "montar a bitstring")
    e.figura(
        doc,
        "huff_encode.png",
        "B=10, A=0, N=11, A=0, N=11, A=0 → 100110110. De 48 bits para 9.",
    )
    e.corpo(
        doc,
        "Contas para o quadro: `3×1 + 2×2 + 1×2 = 3 + 4 + 2 = 9` bits. "
        "Isso é a soma `frequência × comprimento do código`. Huffman escolhe os "
        "comprimentos para essa soma ficar pequena (ótimo entre os códigos prefixo-livres, "
        "quando as frequências são as da mensagem).",
    )

    e.h_secao(doc, "Descompactar bit a bit")
    e.corpo(
        doc,
        "Comece na raiz. Leia *um* bit. `0` desce à esquerda, `1` à direita. "
        "Chegou em folha? Escreva a letra e *volte à raiz*. Não pule bits.",
    )
    e.figura(
        doc,
        "huff_decode.png",
        "Os dois primeiros bits 10 não são “dez”: são um passo (1) e outro (0) até a folha B.",
    )
    e.codigo(doc, LER, "descer até a folha")
    e.passo(doc, 1, "`1` → direita (nó interno). `0` → esquerda → folha `B`. Volta à raiz.")
    e.passo(doc, 2, "`0` → esquerda → folha `A`.")
    e.passo(doc, 3, "`1` → direita (interno). `1` → direita → folha `N`.")
    e.passo(doc, 4, "`0` → `A`.  `1``1` → `N`.  `0` → `A`. Texto: `BANANA`.")
    e.atencao(
        doc,
        "Se no fim dos bits você *não* estiver de novo na raiz, a bitstring está quebrada "
        "ou a tabela não é a mesma da compactação. Não “chute” a última letra.",
    )

    e.h_secao(doc, "Live coding")
    e.corpo(
        doc,
        "Abra `exemplos/huffman.py`. Digite com a turma nesta ordem: `No` → `contar` → "
        "`construir_arvore` (o `while` das junções) → `tabela_codigos` → `compactar` / "
        "`descompactar`. Só então o arquivo `.huff`.",
    )
    e.codigo(doc, EXEMPLO, "exemplos/huffman.py")
    e.boa_pratica(
        doc,
        "O `ordem` no nó é o desempate. Sem ele, dois pais com o mesmo peso deixam o "
        "`sort` instável entre máquinas — e a tabela muda. Frequência primeiro, ordem depois.",
    )

    e.h_secao(doc, "O arquivo .huff")
    e.corpo(
        doc,
        "Na aula o arquivo é *texto*, de propósito. Você abre no VS Code e vê a tabela. "
        "Um compactador “de verdade” empacota os bits em bytes (`int(bits, 2)` de 8 em 8) "
        "e guarda um cabeçalho binário. Isso é o dever de casa, não o quadro das 19h.",
    )
    e.bullets(
        doc,
        [
            "Primeira linha: `HUFFMAN` (assinatura).",
            "Depois: `letra código`, uma por linha.",
            "Uma linha `---` separa a tabela dos bits.",
            "Por último: a bitstring (`100110110`).",
        ],
    )
    e.dica(
        doc,
        "Tem dois jeitos de voltar o texto: descer a árvore (`descompactar`) ou ir "
        "acumulando bits até achar um código na tabela invertida (`descompactar_tabela`). "
        "Os dois precisam da *mesma* tabela que foi salva.",
    )

    e.h_secao(doc, "O que o ZIP faz a mais")
    e.corpo(
        doc,
        "Huffman trata *símbolo por símbolo*. Ele não percebe que `abcabcabc` é o mesmo "
        "bloco três vezes. O DEFLATE (o motor do gzip e de muitos `.zip`) faz duas etapas:",
    )
    e.figura(
        doc,
        "huff_deflate.png",
        "Primeiro copia trechos que já apareceram (LZ77). Depois aplica Huffman nesses códigos.",
    )
    e.bullets(
        doc,
        [
            "LZ77: “copie 3 bytes de 3 posições atrás” em vez de repetir `abc`.",
            "Huffman: os códigos de “cópia” e de “literal” que mais aparecem ficam curtos.",
            "JPEG e MP3 *já* vieram comprimidos. Jogar no ZIP quase não encolhe — às vezes até cresce, por causa do cabeçalho.",
        ],
    )
    e.corpo(
        doc,
        "Hoje vocês implementam só a segunda ideia (Huffman). A primeira (janela de cópia) "
        "é um projeto de extensão: uma fila/buffer do texto recente, no espírito da Aula 3.",
    )

    e.h_secao(doc, "Prática de hoje")
    e.pratica(
        doc,
        "Na mão (10 min) — ABRA",
        "Conte A, B, R. Monte a floresta, faça as junções, escreva a tabela e a bitstring. "
        "Depois rode o script trocando `texto = \"ABRA\"` e compare. Os bits podem diferir "
        "se o empate for outro; o tamanho e a volta do texto é que precisam bater.",
    )
    e.pratica(
        doc,
        "No código (10 min)",
        "Compacte uma frase com o nome da turma. Confira se `descompactar` devolve a frase. "
        "Abra o `.huff` no editor: a tabela tem de fazer sentido com o que está no quadro.",
    )
    e.checkpoint(
        doc,
        [
            "Explicar, sem olhar o código, por que `A` em `BANANA` fica com 1 bit.",
            "Descompactar `100110110` na árvore da apostila, bit a bit.",
            "Dizer o que é prefixo-livre — e dar um contraexemplo (`0` e `00`).",
            "Rodar `python exemplos/huffman.py` e ver `BANANA` voltar.",
            "Uma frase: Huffman não é BST; ZIP não é só Huffman.",
        ],
    )
