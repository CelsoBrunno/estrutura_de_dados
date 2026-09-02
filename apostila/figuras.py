"""Diagramas da apostila — visual limpo, no espírito dos slides da aula."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PASTA = Path(__file__).resolve().parent / "imagens"

NAVY = (14, 36, 56)
LARANJA = (196, 107, 58)
TEAL = (26, 107, 100)
VERDE = (46, 125, 80)
VERMELHO = (176, 64, 64)
ROSA = (244, 196, 196)
MINT = (196, 226, 196)
AZUL = (210, 226, 236)
CINZA = (92, 92, 92)
PRETO = (28, 28, 28)
BRANCO = (255, 255, 255)
LINHA = (40, 40, 40)


def _font(tam: int, bold: bool = False):
    nome = "arialbd.ttf" if bold else "arial.ttf"
    caminho = Path(r"C:\Windows\Fonts") / nome
    if caminho.exists():
        return ImageFont.truetype(str(caminho), tam)
    return ImageFont.load_default()


F = _font(18)
FB = _font(22, True)
FS = _font(15)
FT = _font(28, True)


def nova(w=1400, h=520):
    im = Image.new("RGB", (w, h), BRANCO)
    return im, ImageDraw.Draw(im)


def salvar(im: Image.Image, nome: str) -> Path:
    PASTA.mkdir(exist_ok=True)
    dest = PASTA / nome
    im.save(dest, "PNG")
    return dest


def caixa(d, xy, fill, outline=LINHA, r=16, width=3):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def seta(d, a, b, cor=LINHA, w=3):
    d.line([a, b], fill=cor, width=w)
    x0, y0 = a
    x1, y1 = b
    dx, dy = x1 - x0, y1 - y0
    dist = max((dx * dx + dy * dy) ** 0.5, 1)
    ux, uy = dx / dist, dy / dist
    px, py = -uy, ux
    p1 = (x1, y1)
    p2 = (x1 - 16 * ux + 8 * px, y1 - 16 * uy + 8 * py)
    p3 = (x1 - 16 * ux - 8 * px, y1 - 16 * uy - 8 * py)
    d.polygon([p1, p2, p3], fill=cor)


def centro_txt(d, xy, texto, font=F, cor=PRETO):
    d.text(xy, texto, font=font, fill=cor, anchor="mm")


def lampada(d, cx, cy, ligada: bool):
    r = 28
    fill = (255, 214, 70) if ligada else (245, 245, 245)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fill, outline=LINHA, width=3)
    d.rectangle((cx - 10, cy + r - 4, cx + 10, cy + r + 14), fill=CINZA, outline=LINHA, width=2)


def bits():
    im, d = nova(1400, 480)
    centro_txt(d, (700, 40), "2 bits = 4 combinacoes = valores 0 a 3", FT, NAVY)
    pares = [("0 0", False, False, "0"), ("0 1", False, True, "1"), ("1 0", True, False, "2"), ("1 1", True, True, "3")]
    for i, (bits_txt, a, b, val) in enumerate(pares):
        x = 160 + i * 310
        caixa(d, (x, 110, x + 260, 400), AZUL)
        lampada(d, x + 80, 210, a)
        lampada(d, x + 180, 210, b)
        centro_txt(d, (x + 130, 310), bits_txt, FB, NAVY)
        centro_txt(d, (x + 130, 360), f"valor {val}", F, LARANJA)
    salvar(im, "01_bits.png")


def faixas():
    im, d = nova(1400, 420)
    centro_txt(d, (700, 36), "Quantos valores cabem em N bits?", FT, NAVY)
    cab = ["Bits", "Quantidade (2^N)", "Sem sinal", "Com sinal (aprox.)"]
    linhas = [
        ["2", "4", "0 a 3", "-2 a 1"],
        ["4", "16", "0 a 15", "-8 a 7"],
        ["8", "256", "0 a 255", "-128 a 127"],
        ["16", "65 536", "0 a 65 535", "-32 768 a 32 767"],
        ["32", "4 294 967 296", "0 a 4 294 967 295", "-2 147 483 648 a 2 147 483 647"],
    ]
    xs = [40, 220, 520, 860, 1360]
    y0 = 80
    h = 54
    for c, (x0, x1) in enumerate(zip(xs, xs[1:])):
        caixa(d, (x0, y0, x1 - 8, y0 + h), NAVY, NAVY, 8)
        centro_txt(d, ((x0 + x1 - 8) / 2, y0 + h / 2), cab[c], FS, BRANCO)
    for r, linha in enumerate(linhas):
        y = y0 + (r + 1) * h
        fill = MINT if r % 2 == 0 else AZUL
        for c, (x0, x1) in enumerate(zip(xs, xs[1:])):
            caixa(d, (x0, y, x1 - 8, y + h - 4), fill, LINHA, 6)
            centro_txt(d, ((x0 + x1 - 8) / 2, y + (h - 4) / 2), linha[c], FS if c else FB, NAVY)
    salvar(im, "01_faixas.png")


def array_ram():
    im, d = nova(1400, 460)
    centro_txt(d, (700, 36), "Array precisa de gavetas vizinhas (memoria continua)", FT, NAVY)
    centro_txt(d, (700, 80), "lista = [1, 2, 3, 4, 5]     vizinho ocupado impede crescer no lugar", F, CINZA)
    y = 180
    for i, n in enumerate(["1", "2", "3", "4", "5"]):
        x = 80 + i * 110
        caixa(d, (x, y, x + 100, y + 90), MINT, TEAL, 10)
        centro_txt(d, (x + 50, y + 45), n, FT, NAVY)
        centro_txt(d, (x + 50, y + 115), f"[{i}]", FS, CINZA)
    caixa(d, (80 + 5 * 110, y, 80 + 8 * 110 - 10, y + 90), ROSA, VERMELHO, 10)
    centro_txt(d, (80 + 6.5 * 110, y + 45), "ocupado", F, VERMELHO)
    centro_txt(d, (700, 360), "Para caber o 6, o computador copia tudo para um bloco novo. Custo O(n).", F, PRETO)
    salvar(im, "01_array_ram.png")


def array_copia():
    im, d = nova(1400, 500)
    centro_txt(d, (700, 36), "append quando nao ha vizinho livre: copiar o bloco", FT, NAVY)
    centro_txt(d, (350, 100), "antes  (5 slots)", FB, CINZA)
    for i, n in enumerate(["1", "2", "3", "4", "5"]):
        x = 80 + i * 90
        caixa(d, (x, 140, x + 80, 220), MINT, TEAL, 10)
        centro_txt(d, (x + 40, 180), n, FB, NAVY)
    seta(d, (700, 180), (700, 300), LARANJA)
    centro_txt(d, (820, 250), "copia + 6", F, LARANJA)
    centro_txt(d, (350, 330), "depois (6 slots, outro endereco)", FB, CINZA)
    for i, n in enumerate(["1", "2", "3", "4", "5", "6"]):
        x = 80 + i * 90
        caixa(d, (x, 370, x + 80, 450), AZUL, TEAL, 10)
        centro_txt(d, (x + 40, 410), n, FB, NAVY)
    salvar(im, "01_array_copia.png")


def big_o():
    im, d = nova(1400, 560)
    centro_txt(d, (700, 36), "Big-O: como o tempo cresce quando o input cresce", FT, NAVY)
    ox, oy, W, H = 140, 480, 700, 360
    d.line((ox, oy, ox, oy - H), fill=LINHA, width=3)
    d.line((ox, oy, ox + W, oy), fill=LINHA, width=3)
    centro_txt(d, (ox - 50, oy - H / 2), "tempo", FS, CINZA)
    centro_txt(d, (ox + W / 2, oy + 36), "input", FS, CINZA)

    def pt(n, t, max_n=8, max_t=80):
        x = ox + n / max_n * W
        y = oy - t / max_t * H
        return x, y

    pts1 = [pt(n, 6) for n in range(0, 9)]
    ptsn = [pt(n, n * 6) for n in range(0, 9)]
    pts2 = [pt(n, (n * n) * 1.1) for n in range(0, 9)]
    d.line(pts1, fill=TEAL, width=4)
    d.line(ptsn, fill=LARANJA, width=4)
    d.line(pts2, fill=VERMELHO, width=4)
    caixa(d, (920, 140, 1340, 420), (248, 248, 248), CINZA, 10)
    centro_txt(d, (1130, 180), "O(1)  constante", F, TEAL)
    centro_txt(d, (1130, 240), "O(n)   linear", F, LARANJA)
    centro_txt(d, (1130, 300), "O(n^2) quadratico", F, VERMELHO)
    centro_txt(d, (1130, 360), "acesso por indice = O(1)", FS, NAVY)
    salvar(im, "01_big_o.png")


def no_caixa(d, x, y, titulo, extra="", fill=AZUL, w=180, h=90):
    caixa(d, (x, y, x + w, y + h), fill, NAVY, 18)
    centro_txt(d, (x + w / 2, y + 32), titulo, FB, NAVY)
    if extra:
        centro_txt(d, (x + w / 2, y + 64), extra, FS, CINZA)
    return x + w / 2, y + h / 2, x + w, y + h / 2


def lista_simples():
    im, d = nova(1400, 380)
    centro_txt(d, (700, 36), "Lista simplesmente encadeada  (prox so para a frente)", FT, NAVY)
    nos = [("4", "HEAD"), ("2", ""), ("5", ""), ("1", ""), ("3", "TAIL")]
    xs = [70, 330, 590, 850, 1110]
    y = 150
    centros = []
    for x, (val, tag) in zip(xs, nos):
        cx, cy, dirx, diry = no_caixa(d, x, y, "NODE", val)
        centros.append((dirx, diry, x, val, tag))
        if tag:
            centro_txt(d, (x + 90, y - 36), tag, FB, LARANJA)
    for i in range(len(centros) - 1):
        seta(d, (centros[i][0] + 4, centros[i][1]), (xs[i + 1] - 6, y + 45), VERDE)
        centro_txt(d, ((centros[i][0] + xs[i + 1]) / 2, y + 20), "prox", FS, VERDE)
    seta(d, (centros[-1][0] + 4, centros[-1][1]), (centros[-1][0] + 90, centros[-1][1]), CINZA)
    centro_txt(d, (centros[-1][0] + 110, centros[-1][1] - 28), "None", FS, CINZA)
    salvar(im, "02_lista_simples.png")


def lista_dupla():
    im, d = nova(1400, 420)
    centro_txt(d, (700, 36), "Lista dupla: prox (verde) e anterior (vermelho)", FT, NAVY)
    xs = [90, 380, 670, 960]
    y = 170
    vals = ["A", "B", "C", "D"]
    for x, v in zip(xs, vals):
        no_caixa(d, x, y, "NODE", v, MINT)
    for i in range(len(xs) - 1):
        seta(d, (xs[i] + 184, y + 32), (xs[i + 1] - 6, y + 32), VERDE)
        seta(d, (xs[i + 1] - 4, y + 62), (xs[i] + 186, y + 62), VERMELHO)
        centro_txt(d, ((xs[i] + xs[i + 1] + 180) / 2, y + 14), "prox", FS, VERDE)
        centro_txt(d, ((xs[i] + xs[i + 1] + 180) / 2, y + 88), "anterior", FS, VERMELHO)
    centro_txt(d, (180, 140), "HEAD", FB, LARANJA)
    centro_txt(d, (1050, 140), "TAIL", FB, LARANJA)
    salvar(im, "02_lista_dupla.png")


def reprodutor():
    im, d = nova(1400, 400)
    centro_txt(d, (700, 36), "ReprodutorStreaming  —  faixa atual no meio da playlist", FT, NAVY)
    faixas = ["Queen", "Led Zeppelin", "Eagles"]
    xs = [80, 500, 920]
    y = 150
    for i, (x, nome) in enumerate(zip(xs, faixas)):
        fill = (255, 236, 210) if i == 1 else AZUL
        no_caixa(d, x, y, "faixa", nome, fill, 360, 100)
    for i in range(2):
        seta(d, (xs[i] + 364, y + 35), (xs[i + 1] - 6, y + 35), VERDE)
        seta(d, (xs[i + 1] - 4, y + 70), (xs[i] + 366, y + 70), VERMELHO)
    centro_txt(d, (680, 300), "faixa_atual", FB, LARANJA)
    seta(d, (680, 280), (680, 255), LARANJA)
    salvar(im, "02_reprodutor.png")


def pilha():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Pilha (LIFO)  —  so mexe no topo   O(1)", FT, NAVY)
    # plates
    for i, w in enumerate((220, 240, 260, 280)):
        y = 430 - i * 42
        x = 180
        caixa(d, (x + (280 - w) / 2, y, x + (280 - w) / 2 + w, y + 34), MINT, TEAL, 12)
    centro_txt(d, (320, 250), "topo", FB, LARANJA)
    seta(d, (320, 270), (320, 300), LARANJA)
    centro_txt(d, (320, 480), "pratos: o ultimo a entrar sai primeiro", FS, CINZA)
    # nodes
    nos = ["Pagina 3  (topo)", "Pagina 2", "Pagina 1"]
    for i, t in enumerate(nos):
        y = 120 + i * 110
        no_caixa(d, 820, y, t, "prox para baixo" if i < 2 else "prox = None", AZUL, 460, 90)
        if i < 2:
            seta(d, (1050, y + 92), (1050, y + 108), VERDE)
    salvar(im, "03_pilha.png")


def fila():
    im, d = nova(1400, 380)
    centro_txt(d, (700, 36), "Fila (FIFO)  —  entra no fim, sai no inicio   O(1)", FT, NAVY)
    nomes = ["Ana", "Bia", "Caio", "Duda"]
    xs = [80, 400, 720, 1040]
    y = 160
    for x, n in zip(xs, nomes):
        no_caixa(d, x, y, n, "", AZUL, 260, 90)
    for i in range(3):
        seta(d, (xs[i] + 264, y + 45), (xs[i + 1] - 6, y + 45), VERDE)
    centro_txt(d, (210, 130), "inicio / Head  (sai)", FB, LARANJA)
    centro_txt(d, (1170, 130), "fim  (entra)", FB, TEAL)
    centro_txt(d, (700, 320), "Matchmaking: quem chegou primeiro joga primeiro.", F, PRETO)
    salvar(im, "03_fila.png")


def callcenter():
    im, d = nova(1400, 480)
    centro_txt(d, (700, 36), "Call Center: fila de espera + pilha de historico", FT, NAVY)
    centro_txt(d, (350, 90), "FILA  (FIFO)  deque", FB, TEAL)
    nomes = ["Maria", "Carlos"]
    xs = [80, 300]
    y = 140
    for x, n in zip(xs, nomes):
        no_caixa(d, x, y, n, "", AZUL, 180, 80)
    seta(d, (264, y + 40), (296, y + 40), VERDE)
    centro_txt(d, (170, 250), "inicio  (sai)", FS, LARANJA)
    centro_txt(d, (390, 250), "fim  (entra)", FS, TEAL)
    centro_txt(d, (1050, 90), "PILHA  (LIFO)  list", FB, LARANJA)
    caixa(d, (880, 130, 1320, 210), (255, 236, 210), LARANJA, 12)
    centro_txt(d, (1100, 170), "topo: Joao  (ultimo atendido)", F, NAVY)
    caixa(d, (880, 230, 1320, 290), AZUL, NAVY, 12)
    centro_txt(d, (1100, 260), "abaixo: ...", FS, CINZA)
    seta(d, (880, 170), (520, 180), VERMELHO)
    centro_txt(d, (700, 170), "desfazer", FS, VERMELHO)
    centro_txt(d, (700, 400), "appendleft: Maria volta para o INICIO da fila, nao para o fim.", F, PRETO)
    salvar(im, "03_callcenter.png")


def hash_baldes():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Tabela hash: indice = hash(chave) % tamanho   +  colisao por encadeamento", FT, NAVY)
    for i in range(5):
        x = 80 + i * 260
        caixa(d, (x, 100, x + 220, 160), NAVY, NAVY, 8)
        centro_txt(d, (x + 110, 130), f"balde {i}", F, BRANCO)
        caixa(d, (x, 170, x + 220, 470), (248, 248, 248), CINZA, 8)
    # example pairs in buckets 2 and 3 (from 04_hash demo)
    caixa(d, (80 + 2 * 260 + 20, 200, 80 + 2 * 260 + 200, 270), MINT, TEAL, 8)
    centro_txt(d, (80 + 2 * 260 + 110, 235), "u001 -> Joao", FS, NAVY)
    caixa(d, (80 + 3 * 260 + 20, 200, 80 + 3 * 260 + 200, 270), MINT, TEAL, 8)
    centro_txt(d, (80 + 3 * 260 + 110, 235), "u002 -> Maria", FS, NAVY)
    caixa(d, (80 + 2 * 260 + 20, 290, 80 + 2 * 260 + 200, 360), ROSA, VERMELHO, 8)
    centro_txt(d, (80 + 2 * 260 + 110, 325), "outra chave", FS, VERMELHO)
    centro_txt(d, (80 + 2 * 260 + 110, 400), "colisao", F, VERMELHO)
    salvar(im, "04_hash.png")


def bst():
    im, d = nova(1400, 560)
    centro_txt(d, (700, 36), "BST: esquerda < no < direita     insercao 50, 30, 70, 20, 40", FT, NAVY)

    def no(x, y, v, fill=AZUL):
        d.ellipse((x - 42, y - 42, x + 42, y + 42), fill=fill, outline=NAVY, width=3)
        centro_txt(d, (x, y), str(v), FT, NAVY)
        return x, y

    r = no(700, 130, 50, (255, 236, 210))
    e = no(420, 280, 30)
    dir_ = no(980, 280, 70)
    no(280, 430, 20)
    no(560, 430, 40)
    seta(d, (r[0] - 30, r[1] + 36), (e[0] + 20, e[1] - 40), TEAL)
    seta(d, (r[0] + 30, r[1] + 36), (dir_[0] - 20, dir_[1] - 40), TEAL)
    seta(d, (e[0] - 24, e[1] + 36), (280, 390), TEAL)
    seta(d, (e[0] + 24, e[1] + 36), (560, 390), TEAL)
    centro_txt(d, (520, 200), "menor", FS, TEAL)
    centro_txt(d, (900, 200), "maior", FS, TEAL)
    centro_txt(d, (700, 520), "em-ordem visita esquerda, raiz, direita  ->  20 30 40 50 70", F, PRETO)
    salvar(im, "05_bst.png")


def grafo():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Grafo: vertices (pessoas) e arestas (amizades)", FT, NAVY)
    pos = {
        "Alice": (280, 180),
        "Bruno": (700, 140),
        "Carlos": (1120, 220),
        "Duda": (700, 380),
    }
    edges = [("Alice", "Bruno"), ("Bruno", "Carlos"), ("Alice", "Duda"), ("Duda", "Carlos")]
    for a, b in edges:
        d.line([pos[a], pos[b]], fill=TEAL, width=4)
    for nome, (x, y) in pos.items():
        d.ellipse((x - 70, y - 46, x + 70, y + 46), fill=AZUL, outline=NAVY, width=3)
        centro_txt(d, (x, y), nome, FB, NAVY)
    centro_txt(d, (700, 480), "BFS (fila): caminho mais curto em numero de arestas. Alice -> Carlos = Alice-Bruno-Carlos", F, PRETO)
    salvar(im, "06_grafo.png")


def heap():
    im, d = nova(1400, 620)
    centro_txt(d, (700, 36), "Min-heap: pai <= filhos, guardado num array", FT, NAVY)

    def no(x, y, v, idx):
        d.ellipse((x - 40, y - 40, x + 40, y + 40), fill=MINT, outline=NAVY, width=3)
        centro_txt(d, (x, y - 6), str(v), FT, NAVY)
        centro_txt(d, (x, y + 22), f"i={idx}", FS, CINZA)
        return x, y

    n0 = no(700, 130, 1, 0)
    n1 = no(420, 300, 2, 1)
    n2 = no(980, 300, 4, 2)
    n3 = no(280, 450, 5, 3)
    seta(d, (n0[0] - 24, n0[1] + 36), (n1[0] + 16, n1[1] - 36), TEAL)
    seta(d, (n0[0] + 24, n0[1] + 36), (n2[0] - 16, n2[1] - 36), TEAL)
    seta(d, (n1[0] - 20, n1[1] + 36), (n3[0] + 10, n3[1] - 36), TEAL)
    centro_txt(d, (200, 200), "esq  2*i+1", FS, TEAL)
    centro_txt(d, (1200, 200), "dir  2*i+2", FS, TEAL)
    for i, v in enumerate(["1", "2", "4", "5"]):
        x = 860 + i * 90
        caixa(d, (x, 480, x + 80, 540), AZUL, NAVY, 8)
        centro_txt(d, (x + 40, 510), v, FB, NAVY)
        centro_txt(d, (x + 40, 555), str(i), FS, CINZA)
    centro_txt(d, (780, 510), "array:", F, NAVY)
    salvar(im, "07_heap.png")


def logistica():
    im, d = nova(1400, 560)
    centro_txt(d, (700, 36), "Projeto final: tres pecas no mesmo sistema", FT, NAVY)
    pos = {"CD": (200, 280), "Centro": (520, 180), "Asa Norte": (900, 140), "Asa Sul": (900, 340), "Lago Norte": (1220, 140)}
    edges = [("CD", "Centro"), ("Centro", "Asa Norte"), ("Centro", "Asa Sul"), ("Asa Norte", "Lago Norte")]
    for a, b in edges:
        d.line([pos[a], pos[b]], fill=TEAL, width=4)
    for nome, (x, y) in pos.items():
        caixa(d, (x - 80, y - 28, x + 80, y + 28), AZUL, NAVY, 14)
        centro_txt(d, (x, y), nome, FS, NAVY)
    caixa(d, (40, 430, 450, 530), MINT, TEAL, 10)
    centro_txt(d, (245, 460), "Hash  id -> pacote", FB, NAVY)
    centro_txt(d, (245, 500), "P2 urgente primeiro", FS, PRETO)
    caixa(d, (490, 430, 900, 530), (255, 236, 210), LARANJA, 10)
    centro_txt(d, (695, 460), "Heap  urgencia", FB, NAVY)
    centro_txt(d, (695, 500), "1, depois 2, depois 3", FS, PRETO)
    caixa(d, (940, 430, 1360, 530), AZUL, TEAL, 10)
    centro_txt(d, (1150, 460), "Grafo + BFS", FB, NAVY)
    centro_txt(d, (1150, 500), "CD -> destino", FS, PRETO)
    salvar(im, "08_logistica.png")


def gerar_todas() -> None:
    bits()
    faixas()
    array_ram()
    array_copia()
    big_o()
    lista_simples()
    lista_dupla()
    reprodutor()
    pilha()
    fila()
    callcenter()
    hash_baldes()
    bst()
    grafo()
    heap()
    logistica()
    print("Figuras em", PASTA)


if __name__ == "__main__":
    gerar_todas()
