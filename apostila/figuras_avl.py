"""Diagramas AVL — fórmulas e os quatro casos de rotação."""

from __future__ import annotations

from figuras import (
    AZUL,
    CINZA,
    FB,
    FS,
    FT,
    F,
    LARANJA,
    MINT,
    NAVY,
    ROSA,
    TEAL,
    VERMELHO,
    circulo_no,
    caixa,
    centro_txt,
    nova,
    salvar,
    seta,
)


def _no(d, x, y, v, fill=AZUL, r=30, tag=""):
    circulo_no(d, x, y, v, fill, r)
    if tag:
        centro_txt(d, (x, y - r - 16), tag, FS, LARANJA)
    return x, y


def avl_formulas():
    im, d = nova(1400, 560)
    centro_txt(d, (700, 32), "AVL: altura e balance de cada no", FT, NAVY)
    caixa(d, (40, 70, 680, 520), (252, 246, 240), LARANJA, 14)
    centro_txt(d, (360, 110), "Formulas", FB, LARANJA)
    linhas = [
        "h(None)  =  -1",
        "h(no)    =  1 + max( h(esq), h(dir) )",
        "balance  =  h(esq) - h(dir)",
        "AVL:  |h(E) - h(D)|  <=  1",
        "      em TODOS os nos",
    ]
    y = 170
    for txt in linhas:
        centro_txt(d, (360, y), txt, F, NAVY)
        y += 54

    caixa(d, (720, 70, 1360, 520), MINT, TEAL, 14)
    centro_txt(d, (1040, 110), "O que o numero diz", FB, TEAL)
    regras = [
        ("+1", "pende a esquerda  (ainda AVL)"),
        (" 0", "nivelado"),
        ("-1", "pende a direita   (ainda AVL)"),
        ("|b|=2", "desbalanceado  ->  rotacionar"),
    ]
    y = 180
    for sig, frase in regras:
        caixa(d, (760, y - 28, 900, y + 28), (255, 236, 210), LARANJA, 10)
        centro_txt(d, (830, y), sig, FB, NAVY)
        centro_txt(d, (1120, y), frase, FS, NAVY)
        y += 80
    salvar(im, "05_avl_formulas.png")


def avl_ll_rr():
    im, d = nova(1400, 640)
    centro_txt(d, (700, 28), "Casos 1 e 2: uma rotacao so  (reta, nao Z)", FT, NAVY)

    caixa(d, (30, 64, 680, 610), (252, 246, 240), LARANJA, 12)
    centro_txt(d, (355, 96), "Caso 1  rotacao a direita  (LL)", FB, LARANJA)
    centro_txt(d, (355, 132), "z a esquerda de y; y a esquerda de x", FS, CINZA)
    _no(d, 200, 220, 30, (255, 236, 210), 32, "x")
    _no(d, 140, 340, 20, ROSA, 32, "y")
    _no(d, 90, 460, 10, ROSA, 32, "z")
    seta(d, (180, 248), (150, 312), VERMELHO, 3)
    seta(d, (120, 368), (100, 432), VERMELHO, 3)
    centro_txt(d, (355, 250), "ANTES", FS, VERMELHO)
    _no(d, 500, 300, 20, MINT, 32, "y")
    _no(d, 430, 440, 10, AZUL, 32, "z")
    _no(d, 570, 440, 30, AZUL, 32, "x")
    seta(d, (480, 328), (440, 412), TEAL, 3)
    seta(d, (520, 328), (560, 412), TEAL, 3)
    centro_txt(d, (500, 230), "DEPOIS  rotateRight(x)", FS, TEAL)
    centro_txt(d, (355, 560), "x.esquerda recebe y.direita", FS, NAVY)
    centro_txt(d, (355, 590), "inserir 10 em 30-20", FS, CINZA)

    caixa(d, (720, 64, 1370, 610), MINT, TEAL, 12)
    centro_txt(d, (1045, 96), "Caso 2  rotacao a esquerda  (RR)", FB, TEAL)
    centro_txt(d, (1045, 132), "z a direita de y; y a direita de x", FS, CINZA)
    _no(d, 880, 220, 10, (255, 236, 210), 32, "x")
    _no(d, 960, 340, 20, ROSA, 32, "y")
    _no(d, 1030, 460, 30, ROSA, 32, "z")
    seta(d, (900, 248), (940, 312), VERMELHO, 3)
    seta(d, (980, 368), (1012, 432), VERMELHO, 3)
    centro_txt(d, (880, 250), "ANTES", FS, VERMELHO)
    _no(d, 1200, 300, 20, MINT, 32, "y")
    _no(d, 1130, 440, 10, AZUL, 32, "x")
    _no(d, 1270, 440, 30, AZUL, 32, "z")
    seta(d, (1180, 328), (1140, 412), TEAL, 3)
    seta(d, (1220, 328), (1260, 412), TEAL, 3)
    centro_txt(d, (1200, 230), "DEPOIS  rotateLeft(x)", FS, TEAL)
    centro_txt(d, (1045, 560), "x.direita recebe y.esquerda", FS, NAVY)
    centro_txt(d, (1045, 590), "inserir 30 em 10-20", FS, CINZA)
    salvar(im, "05_avl_ll_rr.png")


def avl_rl_lr():
    im, d = nova(1400, 700)
    centro_txt(d, (700, 26), "Casos 3 e 4: duas rotacoes  (cenario em Z / joelho)", FT, NAVY)

    caixa(d, (20, 56, 690, 670), (252, 246, 240), LARANJA, 12)
    centro_txt(d, (355, 88), "Caso 3  direita no y, depois esquerda no x  (RL)", FB, LARANJA)
    centro_txt(d, (355, 122), "z a esquerda de y; y a direita de x", FS, CINZA)
    _no(d, 120, 200, 10, (255, 236, 210), 28, "x")
    _no(d, 200, 320, 30, ROSA, 28, "y")
    _no(d, 140, 440, 20, ROSA, 28, "z")
    seta(d, (136, 224), (182, 296), VERMELHO, 3)
    seta(d, (180, 344), (150, 416), VERMELHO, 3)
    centro_txt(d, (160, 520), "1. ANTES", FS, VERMELHO)

    _no(d, 360, 200, 10, (255, 236, 210), 28, "x")
    _no(d, 360, 340, 20, MINT, 28, "z")
    _no(d, 430, 460, 30, ROSA, 28, "y")
    seta(d, (360, 228), (360, 312), TEAL, 3)
    seta(d, (376, 364), (416, 436), TEAL, 3)
    centro_txt(d, (430, 200), "2. gira y", FS, TEAL)

    _no(d, 560, 280, 20, MINT, 28, "z")
    _no(d, 490, 420, 10, AZUL, 28, "x")
    _no(d, 630, 420, 30, AZUL, 28, "y")
    seta(d, (540, 304), (500, 396), TEAL, 3)
    seta(d, (580, 304), (620, 396), TEAL, 3)
    centro_txt(d, (560, 540), "3. gira x", FS, TEAL)
    centro_txt(d, (355, 620), "Exemplo: inserir 20 em 10-30", FS, NAVY)

    caixa(d, (710, 56, 1380, 670), MINT, TEAL, 12)
    centro_txt(d, (1045, 88), "Caso 4  esquerda no y, depois direita no x  (LR)", FB, TEAL)
    centro_txt(d, (1045, 122), "z a direita de y; y a esquerda de x", FS, CINZA)
    _no(d, 860, 200, 30, (255, 236, 210), 28, "x")
    _no(d, 780, 320, 10, ROSA, 28, "y")
    _no(d, 840, 440, 20, ROSA, 28, "z")
    seta(d, (840, 224), (794, 296), VERMELHO, 3)
    seta(d, (800, 344), (830, 416), VERMELHO, 3)
    centro_txt(d, (780, 520), "1. ANTES", FS, VERMELHO)

    _no(d, 1040, 200, 30, (255, 236, 210), 28, "x")
    _no(d, 1040, 340, 20, MINT, 28, "z")
    _no(d, 970, 460, 10, ROSA, 28, "y")
    seta(d, (1040, 228), (1040, 312), TEAL, 3)
    seta(d, (1024, 364), (984, 436), TEAL, 3)
    centro_txt(d, (1120, 200), "2. gira y", FS, TEAL)

    _no(d, 1240, 280, 20, MINT, 28, "z")
    _no(d, 1170, 420, 10, AZUL, 28, "y")
    _no(d, 1310, 420, 30, AZUL, 28, "x")
    seta(d, (1220, 304), (1180, 396), TEAL, 3)
    seta(d, (1260, 304), (1300, 396), TEAL, 3)
    centro_txt(d, (1240, 540), "3. gira x", FS, TEAL)
    centro_txt(d, (1045, 620), "Exemplo: inserir 20 em 30-10", FS, NAVY)
    salvar(im, "05_avl_rl_lr.png")


def gerar_avl() -> None:
    avl_formulas()
    avl_ll_rr()
    avl_rl_lr()
