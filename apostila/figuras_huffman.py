"""Diagramas da aula extra — compactação Huffman (BANANA)."""

from __future__ import annotations

from figuras import (
    AZUL,
    BRANCO,
    CINZA,
    FB,
    FS,
    FT,
    F,
    LARANJA,
    LINHA,
    MINT,
    NAVY,
    PRETO,
    ROSA,
    TEAL,
    VERMELHO,
    caixa,
    centro_txt,
    circulo_no,
    nova,
    salvar,
    seta,
)


def _folha(d, x, y, letra, freq, fill=AZUL):
    circulo_no(d, x, y, letra, fill, 34)
    centro_txt(d, (x, y + 52), f"freq {freq}", FS, CINZA)
    return x, y


def _interno(d, x, y, freq, fill=(255, 236, 210)):
    circulo_no(d, x, y, freq, fill, 34)
    return x, y


def ideia():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Mesmo texto, dois jeitos de gastar bits", FT, NAVY)

    caixa(d, (40, 80, 670, 480), (252, 246, 240), LARANJA, 14)
    centro_txt(d, (355, 120), "ASCII: 8 bits para todo mundo", FB, LARANJA)
    letras = [("B", "01000010"), ("A", "01000001"), ("N", "01001110")]
    y = 180
    for letra, bits in letras:
        caixa(d, (80, y, 160, y + 56), AZUL, NAVY, 10)
        centro_txt(d, (120, y + 28), letra, FB, NAVY)
        centro_txt(d, (420, y + 28), bits, F, PRETO)
        y += 80
    centro_txt(d, (355, 440), "BANANA = 48 bits", FB, VERMELHO)

    caixa(d, (730, 80, 1360, 480), MINT, TEAL, 14)
    centro_txt(d, (1045, 120), "Huffman: o frequente paga menos", FB, TEAL)
    huff = [("A", "0", "aparece 3x"), ("N", "11", "aparece 2x"), ("B", "10", "aparece 1x")]
    y = 180
    for letra, bits, nota in huff:
        caixa(d, (770, y, 850, y + 56), AZUL, NAVY, 10)
        centro_txt(d, (810, y + 28), letra, FB, NAVY)
        centro_txt(d, (980, y + 28), bits, FB, TEAL)
        centro_txt(d, (1200, y + 28), nota, FS, CINZA)
        y += 80
    centro_txt(d, (1045, 440), "BANANA = 9 bits", FB, TEAL)
    salvar(im, "huff_ideia.png")


def prefixo():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 32), "Codigo prefixo-livre: nenhum codigo comeca o outro", FT, NAVY)

    caixa(d, (40, 80, 670, 480), MINT, TEAL, 14)
    centro_txt(d, (355, 120), "Pode:  0   10   11", FB, TEAL)
    centro_txt(d, (355, 180), "Lendo 10011...", F, NAVY)
    centro_txt(d, (355, 240), "10  ->  B", F, PRETO)
    centro_txt(d, (355, 290), "0   ->  A", F, PRETO)
    centro_txt(d, (355, 340), "11  ->  N", F, PRETO)
    centro_txt(d, (355, 420), "Nunca fica em duvida onde corta.", FS, TEAL)

    caixa(d, (730, 80, 1360, 480), ROSA, VERMELHO, 14)
    centro_txt(d, (1045, 120), "Nao pode:  0   e   00", FB, VERMELHO)
    centro_txt(d, (1045, 200), "A = 0    B = 00", F, NAVY)
    centro_txt(d, (1045, 270), "Chegou o bit 0...", F, PRETO)
    centro_txt(d, (1045, 330), "Ja e A?  Ou espera o segundo 0 do B?", F, PRETO)
    centro_txt(d, (1045, 420), "O descompressor trava. Por isso a arvore.", FS, VERMELHO)
    salvar(im, "huff_prefixo.png")


def frequencia():
    im, d = nova(1400, 480)
    centro_txt(d, (700, 36), "Passo 1  contar  BANANA", FT, NAVY)
    centro_txt(d, (700, 84), "B A N A N A", FB, LARANJA)

    cab = ["Letra", "Quantas vezes", "Vira no da arvore"]
    linhas = [
        ["A", "3", "folha A, peso 3"],
        ["N", "2", "folha N, peso 2"],
        ["B", "1", "folha B, peso 1"],
    ]
    xs = [80, 360, 740, 1320]
    y0 = 130
    h = 70
    for c, (x0, x1) in enumerate(zip(xs, xs[1:])):
        caixa(d, (x0, y0, x1 - 12, y0 + h), NAVY, NAVY, 8)
        centro_txt(d, ((x0 + x1 - 12) / 2, y0 + h / 2), cab[c], FS, BRANCO)
    for r, linha in enumerate(linhas):
        y = y0 + (r + 1) * h
        fill = MINT if r == 0 else AZUL
        for c, (x0, x1) in enumerate(zip(xs, xs[1:])):
            caixa(d, (x0, y, x1 - 12, y + h - 8), fill, LINHA, 6)
            centro_txt(d, ((x0 + x1 - 12) / 2, y + (h - 8) / 2), linha[c], FB if c == 0 else F, NAVY)
    salvar(im, "huff_freq.png")


def juntar():
    im, d = nova(1400, 820)
    centro_txt(d, (700, 28), "Passos 2 e 3  sempre junte os dois menores", FT, NAVY)

    caixa(d, (30, 64, 1370, 380), (252, 246, 240), LARANJA, 12)
    centro_txt(d, (700, 96), "Juncao 1 — B(1) e N(2) saem. A(3) espera.", FB, LARANJA)
    _folha(d, 140, 200, "B", 1, ROSA)
    _folha(d, 320, 200, "N", 2, ROSA)
    _folha(d, 500, 200, "A", 3, AZUL)
    centro_txt(d, (230, 290), "menores", FS, VERMELHO)
    centro_txt(d, (500, 290), "espera", FS, CINZA)
    d.line([(140, 330), (140, 350), (860, 350)], fill=VERMELHO, width=3)
    d.line([(320, 330), (320, 350)], fill=VERMELHO, width=3)
    seta(d, (860, 350), (860, 200), VERMELHO, 3)
    _interno(d, 1000, 170, 3)
    _folha(d, 900, 300, "B", 1, ROSA)
    _folha(d, 1100, 300, "N", 2, ROSA)
    seta(d, (980, 200), (920, 270), TEAL, 3)
    seta(d, (1020, 200), (1080, 270), TEAL, 3)
    centro_txt(d, (1000, 112), "pai peso 1+2 = 3", FS, TEAL)

    caixa(d, (30, 400, 1370, 800), MINT, TEAL, 12)
    centro_txt(d, (700, 432), "Juncao 2 — empate 3 e 3. A entrou primeiro: filho esquerdo.", FB, TEAL)
    _folha(d, 160, 560, "A", 3, AZUL)
    _interno(d, 480, 540, 3)
    _folha(d, 400, 660, "B", 1, ROSA)
    _folha(d, 560, 660, "N", 2, ROSA)
    seta(d, (460, 570), (420, 630), TEAL, 3)
    seta(d, (500, 570), (540, 630), TEAL, 3)
    centro_txt(d, (320, 500), "os dois que restam", FS, CINZA)
    seta(d, (220, 520), (820, 500), VERMELHO, 3)
    seta(d, (540, 510), (900, 500), VERMELHO, 3)
    _interno(d, 1000, 530, 6)
    a2 = _folha(d, 840, 640, "A", 3, MINT)
    p2 = _interno(d, 1160, 640, 3)
    _folha(d, 1080, 750, "B", 1, ROSA)
    _folha(d, 1240, 750, "N", 2, ROSA)
    seta(d, (970, 560), (a2[0] + 10, 600), TEAL, 3)
    seta(d, (1030, 560), (p2[0] - 10, 610), TEAL, 3)
    seta(d, (1140, 670), (1100, 720), TEAL, 2)
    seta(d, (1180, 670), (1220, 720), TEAL, 2)
    centro_txt(d, (1000, 478), "raiz peso 6  (uma arvore so)", FS, TEAL)
    salvar(im, "huff_juntar.png")


def arvore():
    im, d = nova(1400, 640)
    centro_txt(d, (700, 28), "Passo 4  esquerda = 0    direita = 1", FT, NAVY)
    r = _interno(d, 700, 120, 6)
    a = _folha(d, 380, 320, "A", 3, MINT)
    p = _interno(d, 1020, 320, 3)
    b = _folha(d, 860, 520, "B", 1, ROSA)
    n = _folha(d, 1180, 520, "N", 2, ROSA)
    seta(d, (r[0] - 24, r[1] + 34), (a[0] + 20, a[1] - 50), TEAL, 3)
    seta(d, (r[0] + 24, r[1] + 34), (p[0] - 16, p[1] - 50), TEAL, 3)
    seta(d, (p[0] - 20, p[1] + 34), (b[0] + 12, b[1] - 50), TEAL, 3)
    seta(d, (p[0] + 20, p[1] + 34), (n[0] - 12, n[1] - 50), TEAL, 3)
    centro_txt(d, (500, 200), "0", FB, LARANJA)
    centro_txt(d, (900, 200), "1", FB, LARANJA)
    centro_txt(d, (900, 400), "0", FB, LARANJA)
    centro_txt(d, (1140, 400), "1", FB, LARANJA)
    caixa(d, (40, 430, 320, 600), (252, 246, 240), LARANJA, 12)
    centro_txt(d, (180, 470), "Tabela", FB, LARANJA)
    centro_txt(d, (180, 520), "A = 0", F, NAVY)
    centro_txt(d, (180, 555), "B = 10", F, NAVY)
    centro_txt(d, (180, 590), "N = 11", F, NAVY)
    salvar(im, "huff_arvore.png")


def encode():
    im, d = nova(1400, 480)
    centro_txt(d, (700, 32), "Compactar BANANA  letra a letra", FT, NAVY)
    colunas = [
        ("B", "10"),
        ("A", "0"),
        ("N", "11"),
        ("A", "0"),
        ("N", "11"),
        ("A", "0"),
    ]
    x = 80
    for letra, bits in colunas:
        caixa(d, (x, 90, x + 180, 220), AZUL, NAVY, 12)
        centro_txt(d, (x + 90, 130), letra, FT, NAVY)
        centro_txt(d, (x + 90, 185), bits, FB, TEAL)
        x += 220
    caixa(d, (80, 280, 1320, 440), MINT, TEAL, 12)
    centro_txt(d, (700, 330), "100110110", FT, NAVY)
    centro_txt(d, (700, 390), "9 bits   (ASCII gastaria 6 x 8 = 48)", FB, TEAL)
    salvar(im, "huff_encode.png")


def decode():
    im, d = nova(1400, 640)
    centro_txt(d, (700, 28), "Descompactar: um bit, um passo na arvore. Folha? Emita e volte a raiz.", FT, NAVY)
    passos = [
        ("1", "desce direita", "ainda interno"),
        ("0", "desce esquerda", "folha B  ->  emite B"),
        ("0", "desce esquerda", "folha A  ->  emite A"),
        ("1", "desce direita", "ainda interno"),
        ("1", "desce direita", "folha N  ->  emite N"),
    ]
    y = 80
    for i, (bit, acao, resultado) in enumerate(passos, start=1):
        caixa(d, (60, y, 160, y + 88), (255, 236, 210), LARANJA, 10)
        centro_txt(d, (110, y + 44), bit, FT, NAVY)
        centro_txt(d, (420, y + 44), f"{i}. {acao}", F, NAVY)
        centro_txt(d, (1000, y + 44), resultado, F, TEAL if "emite" in resultado else CINZA)
        y += 100
    centro_txt(d, (700, 600), "Depois: 0 -> A,  11 -> N,  0 -> A.   Texto: BANANA", FB, NAVY)
    salvar(im, "huff_decode.png")


def deflate():
    im, d = nova(1400, 420)
    centro_txt(d, (700, 32), "ZIP / gzip (DEFLATE): duas ideias na fila", FT, NAVY)
    etapas = [
        ("Texto", "abcabcabc"),
        ("1. Copiar trechos", '"3 bytes de 3 atras"'),
        ("2. Huffman", "codigos curtos"),
        (".zip / .gz", "arquivo menor"),
    ]
    x = 40
    for i, (titulo, corpo) in enumerate(etapas):
        caixa(d, (x, 100, x + 300, 340), MINT if i % 2 == 0 else AZUL, TEAL if i else NAVY, 14)
        centro_txt(d, (x + 150, 160), titulo, FB, NAVY)
        centro_txt(d, (x + 150, 240), corpo, FS, CINZA)
        if i < 3:
            seta(d, (x + 310, 220), (x + 350, 220), LARANJA, 4)
        x += 350
    salvar(im, "huff_deflate.png")


def gerar_todas():
    ideia()
    prefixo()
    frequencia()
    juntar()
    arvore()
    encode()
    decode()
    deflate()
