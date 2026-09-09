"""Aula 5 — passo a passo calmo do balanceamento AVL."""

from __future__ import annotations

import estilo as e

FORMULAS = '''def altura(no):
    if no is None:
        return -1
    return 1 + max(altura(no.esquerda), altura(no.direita))


def balance(no):
    if no is None:
        return 0
    return altura(no.esquerda) - altura(no.direita)
'''

ROTACOES = '''def rotacionar_direita(x):
    y = x.esquerda
    x.esquerda = y.direita   # x recebe o que estava a direita de y
    y.direita = x
    return y


def rotacionar_esquerda(x):
    y = x.direita
    x.direita = y.esquerda   # x recebe o que estava a esquerda de y
    y.esquerda = x
    return y
'''

DETECTAR = '''# z = no recem-inserido, y = pai, x = avo
# ANTES de z, x ja pendia (+1 ou -1). DEPOIS, |balance(x)| == 2.
y = z.pai
x = y.pai

# Caso 1 (LL): caminho esquerda-esquerda
if x.esquerda is y and y.esquerda is z:
    rotacionar_direita(x)

# Caso 2 (RR): caminho direita-direita
if x.direita is y and y.direita is z:
    rotacionar_esquerda(x)

# Caso 3 (RL): y a direita de x, z a esquerda de y  ->  gira y a direita, depois x a esquerda
# Caso 4 (LR): y a esquerda de x, z a direita de y  ->  gira y a esquerda, depois x a direita
'''


def escrever(doc):
    e.h_secao(doc, "Fórmulas do balanceamento (AVL)")
    e.corpo(
        doc,
        "Antes de girar, respire. AVL não é mágica: cada nó guarda (ou calcula) uma *altura*, "
        "e o *balance* diz se aquele nó ainda é AVL. Uma árvore `<E, raiz, D>` é AVL se "
        "`|h(E) - h(D)| ≤ 1` *e* E e D também são AVL — em todos os nós, não só na raiz.",
    )
    e.figura(
        doc,
        "05_avl_formulas.png",
        "h(None) = −1. Balance positivo pende à esquerda; negativo, à direita. |b| = 2 pede rotação.",
    )
    e.bullets(
        doc,
        [
            "`altura(None) = -1`. Folha: `1 + max(-1, -1) = 0`.",
            "`altura(no) = 1 + max(altura(esquerda), altura(direita))`.",
            "`balance(no) = altura(esquerda) - altura(direita)`.",
            "`+1` pende à esquerda, `0` nivelado, `-1` pende à direita — *ainda* AVL (`|b| ≤ 1`).",
            "`|balance| == 2` está desbalanceado. Aí sim rotaciona.",
        ],
    )
    e.codigo(doc, FORMULAS, "altura e balance")
    e.dica(
        doc,
        "Pendente (`+1` ou `-1`) não é o mesmo que desbalanceado. Pendente é a iminência. "
        "Desbalanceado (`+2` ou `-2`) é o alarme.",
    )

    e.h_secao(doc, "Passo a passo depois de inserir")
    e.corpo(
        doc,
        "A inserção é a mesma da BST. O extra da AVL começa *depois* do novo nó existir. "
        "Nomes fixos (de baixo para cima):",
    )
    e.bullets(
        doc,
        [
            "`z` — o nó que acabou de entrar.",
            "`y` — o pai de `z`.",
            "`x` — o avô de `z` (pai de `y`).",
        ],
    )
    e.corpo(doc, "Agora, devagar:")
    e.passo(doc, 1, "Insira como na BST. `z` é o novo nó.")
    e.passo(doc, 2, "Suba: `y = z.pai`, `x = y.pai`. (Se não houver avô, não gira ainda.)")
    e.passo(doc, 3, "Calcule `balance(x)`, `balance(y)`.")
    e.passo(doc, 4, "Pergunte: `z` nasceu à esquerda ou à direita de `y`? E `y` é filho esquerdo ou direito de `x`?")
    e.passo(doc, 5, "Se `|balance(x)| == 2`, escolha o caso 1, 2, 3 ou 4 e gire.")
    e.passo(doc, 6, "Confira em-ordem (continua crescente) e `|balance| ≤ 1` nos nós que girou.")
    e.codigo(doc, ROTACOES, "as duas rotações")
    e.corpo(
        doc,
        "Na rotação à *direita* de `x`, a esquerda de `x` passa a receber o que estava à *direita* de `y`. "
        "Na rotação à *esquerda* de `x`, a direita de `x` passa a receber o que estava à *esquerda* de `y`. "
        "É o filho interno — ele não some, muda de pai.",
    )

    e.h_secao(doc, "Caso 1 — rotação à direita (LL)")
    e.corpo(
        doc,
        "O `z` entrou à *esquerda* do pai. O pai `y` é filho *esquerdo* de um `x` que *já pendia* "
        "à esquerda (`balance == +1`). Com o `z`, `balance(x)` vira `+2`. É uma reta: "
        "esquerda-esquerda. Gira só o avô, à direita.",
    )
    e.codigo(
        doc,
        "y = z.pai\nx = y.pai\nif x.esquerda is y and y.esquerda is z:\n    rotacionar_direita(x)",
        "detectar caso 1",
    )
    e.figura(
        doc,
        "05_avl_ll_rr.png",
        "Esquerda: caso 1 (10 entra em 30–20). Direita: caso 2 (30 entra em 10–20).",
    )

    e.h_secao(doc, "Caso 2 — rotação à esquerda (RR)")
    e.corpo(
        doc,
        "Espelho do caso 1. O `z` entrou à *direita* do pai. O pai `y` é filho *direito* de um `x` "
        "que *já pendia* à direita (`balance == -1`). Com o `z`, `balance(x)` vira `-2`. "
        "Reta direita-direita. Gira só o avô, à esquerda. É a vareta 10 → 20 → 30 da aula.",
    )
    e.codigo(
        doc,
        "y = z.pai\nx = y.pai\nif x.direita is y and y.direita is z:\n    rotacionar_esquerda(x)",
        "detectar caso 2",
    )

    e.h_secao(doc, "Caso 3 — direita no pai, depois esquerda no avô (RL)")
    e.corpo(
        doc,
        "O `z` entrou à *esquerda* do pai, mas o pai `y` é filho *direito* de `x`. "
        "O desenho faz um Z (joelho). Uma rotação só no avô *não* basta: primeiro endereita o joelho "
        "girando `y` à direita; depois gira `x` à esquerda.",
    )
    e.bullets(
        doc,
        [
            "Exemplo: 10, depois 30, depois 20. `z=20`, `y=30`, `x=10`.",
            "Passo A — `rotacionar_direita(y)`: o 20 sobe para debaixo do 10.",
            "Passo B — `rotacionar_esquerda(x)`: o 20 vira raiz local; 10 e 30 são filhos.",
        ],
    )

    e.h_secao(doc, "Caso 4 — esquerda no pai, depois direita no avô (LR)")
    e.corpo(
        doc,
        "Espelho do caso 3. O `z` entrou à *direita* do pai, e o pai `y` é filho *esquerdo* de `x`. "
        "Outro Z. Primeiro gira `y` à esquerda; depois gira `x` à direita.",
    )
    e.figura(
        doc,
        "05_avl_rl_lr.png",
        "Caso 3 (inserir 20 em 10–30) e caso 4 (inserir 20 em 30–10). Dois giros cada.",
    )
    e.bullets(
        doc,
        [
            "Exemplo: 30, depois 10, depois 20. `z=20`, `y=10`, `x=30`.",
            "Passo A — `rotacionar_esquerda(y)`.",
            "Passo B — `rotacionar_direita(x)`.",
        ],
    )
    e.codigo(doc, DETECTAR, "exemplos/05_bst_avl.py")
    e.dica(
        doc,
        "Para lembrar: reta (LL/RR) = um giro no avô. Joelho (LR/RL) = um giro no pai para "
        "endereitar, depois o mesmo giro do caso 1 ou 2 no avô.",
    )
    e.corpo(
        doc,
        "Leitura extra (mesmos quatro casos e as fórmulas de altura): "
        "João Arthur BM, *Árvores Balanceadas (AVL)* — "
        "`https://joaoarthurbm.github.io/eda/posts/avl/`.",
    )

    e.h_secao(doc, "Rotação quando o pai já tem filhos")
    e.corpo(
        doc,
        "A vareta 10-20-30 esconde o filho interno. Na árvore da aula o 30 *já tem* 20 e 40, "
        "e o 40 já tem o ramo 35-36-37. Quando você faz o caso 2 no 30, a linha "
        "`x.direita = y.esquerda` é o 35 mudando de pai.",
    )
    e.corpo(
        doc,
        "Valores 20, 30, 40, 35, 36, 37, 50, 70 (inserção: 50, 30, 70, 20, 40, 35, 36, 37). "
        "Gira o 30 à esquerda: o 40 sobe; o 35, que era esquerdo do 40, vira direito do 30.",
    )
    e.figura(
        doc,
        "05_bst_rotacao_filhos.png",
        "O 30 desce e fica pai de 20 e 35. Em-ordem continua 20 30 35 36 37 40 50 70.",
    )
    e.bullets(
        doc,
        [
            "Antes: 30 tem 20 e 40; 40 tem 35.",
            "Depois: 40 no lugar do 30; 30 tem 20 e 35.",
            "Um giro não deixa tudo perfeito — o ramo 35-36-37 ainda pende. AVL olharia o próximo `x`.",
        ],
    )

    e.h_secao(doc, "Reconstruir pelo meio e inserir o 32")
    e.corpo(
        doc,
        "Atalho de sala (não é o algoritmo AVL): pegue a em-ordem e use o do meio como raiz; "
        "repita nas metades. Com oito valores o meio é o 37. Depois o 32 entra à direita do 30.",
    )
    e.figura(
        doc,
        "05_bst_meio_32.png",
        "Painel 2: 37 no topo. Painel 3: o 32 cai à direita do 30 — o 30 fica com 20 e 32.",
    )
    e.codigo(
        doc,
        "arvore.raiz = construir_equilibrada([20, 30, 35, 36, 37, 40, 50, 70])\n"
        "arvore.inserir(32)  # 32 < 37, > 30, < 35  ->  direita do 30",
        "exemplos/05_bst_rebalance.py",
    )
    e.atencao(
        doc,
        "O reset pelo meio equilibra agora. Se depois chegarem 33, 34, 38… em sequência, "
        "aquele ramo pende de novo — aí voltam os quatro casos (ou uma AVL de verdade).",
    )
    e.corpo(
        doc,
        "Na Aula 8: *usei BST porque preciso de ordem; sei que ids em sequência degeneram; "
        "AVL gira com as fórmulas de balance; hash não degenera assim, mas não lista em ordem.*",
    )
