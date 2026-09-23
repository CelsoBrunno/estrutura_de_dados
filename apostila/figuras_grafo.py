"""Figuras extras da Aula 6 — tipos, grau, caminho, peso e representação."""

from __future__ import annotations

from figuras import (
    AZUL,
    BRANCO,
    CINZA,
    F,
    FB,
    FS,
    FT,
    LARANJA,
    MINT,
    NAVY,
    PRETO,
    TEAL,
    VERMELHO,
    caixa,
    centro_txt,
    nova,
    salvar,
    seta,
)


def _vertice(d, x, y, nome, fill=AZUL, rx=64, ry=40):
    d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=fill, outline=NAVY, width=3)
    centro_txt(d, (x, y), nome, FB, NAVY)
    return x, y


def tipos():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Nao direcionado (mao dupla)  vs  direcionado (seta)", FT, NAVY)

    caixa(d, (40, 80, 680, 480), (247, 247, 247), TEAL, 12)
    centro_txt(d, (360, 118), "Nao direcionado — amizade", FB, TEAL)
    a = _vertice(d, 200, 280, "Alice")
    b = _vertice(d, 520, 280, "Bruno")
    d.line([(a[0] + 64, a[1]), (b[0] - 64, b[1])], fill=TEAL, width=5)
    centro_txt(d, (360, 220), "aresta {Alice, Bruno}", FS, CINZA)
    centro_txt(d, (360, 430), "Se A liga B, B liga A. Grau(Alice)=1.", F, PRETO)

    caixa(d, (720, 80, 1360, 480), (247, 247, 247), LARANJA, 12)
    centro_txt(d, (1040, 118), "Direcionado — rua de mao unica", FB, LARANJA)
    c = _vertice(d, 880, 280, "CD", fill=MINT)
    e = _vertice(d, 1200, 280, "Centro", fill=MINT)
    seta(d, (c[0] + 64, c[1]), (e[0] - 64, e[1]), LARANJA, 5)
    centro_txt(d, (1040, 220), "arco CD -> Centro", FS, CINZA)
    centro_txt(d, (1040, 430), "CD chega em Centro; o inverso pode nao existir.", F, PRETO)
    salvar(im, "06_tipos.png")


def adjacencia_grau():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Adjacentes = vizinhos. Grau = quantas arestas tocam o vertice.", FT, NAVY)
    pos = {
        "Alice": (280, 220),
        "Bruno": (700, 160),
        "Carlos": (1120, 220),
        "Duda": (700, 380),
    }
    for a, b in [("Alice", "Bruno"), ("Bruno", "Carlos"), ("Alice", "Duda")]:
        d.line([pos[a], pos[b]], fill=TEAL, width=4)
    for nome, (x, y) in pos.items():
        fill = (255, 214, 150) if nome == "Bruno" else AZUL
        _vertice(d, x, y, nome, fill=fill)
    centro_txt(d, (700, 470), "Bruno e adjacente a Alice e Carlos. Grau(Bruno)=2. Duda nao e adjacente a Bruno.", F, PRETO)
    salvar(im, "06_grau.png")


def caminho():
    im, d = nova(1400, 520)
    centro_txt(d, (700, 36), "Caminho = sequencia de vertices adjacentes (sem repetir, no curso)", FT, NAVY)
    pos = {
        "Alice": (220, 200),
        "Bruno": (560, 140),
        "Carlos": (980, 200),
        "Duda": (560, 360),
    }
    d.line([pos["Alice"], pos["Bruno"]], fill=LARANJA, width=6)
    d.line([pos["Bruno"], pos["Carlos"]], fill=LARANJA, width=6)
    d.line([pos["Alice"], pos["Duda"]], fill=TEAL, width=3)
    d.line([pos["Duda"], pos["Carlos"]], fill=TEAL, width=3)
    for nome, (x, y) in pos.items():
        _vertice(d, x, y, nome)
    centro_txt(d, (700, 455), "Laranja: Alice-Bruno-Carlos (2 arestas). Teal: Alice-Duda-Carlos (tambem 2).", F, PRETO)
    centro_txt(d, (700, 492), "Ciclo: Alice-Bruno-Carlos-Duda-Alice. Arvore nao tem ciclo; grafo pode ter.", FS, CINZA)
    salvar(im, "06_caminho.png")


def ponderado():
    im, d = nova(1400, 480)
    centro_txt(d, (700, 36), "Grafo ponderado: a aresta carrega um custo (km, minutos, pedagio)", FT, NAVY)
    pos = {"CD": (220, 240), "Centro": (700, 160), "Asa Norte": (1180, 240), "Asa Sul": (700, 380)}
    rotulos = [
        ("CD", "Centro", "4 km"),
        ("Centro", "Asa Norte", "6 km"),
        ("Centro", "Asa Sul", "3 km"),
    ]
    for a, b, txt in rotulos:
        d.line([pos[a], pos[b]], fill=TEAL, width=4)
        mx = (pos[a][0] + pos[b][0]) // 2
        my = (pos[a][1] + pos[b][1]) // 2
        caixa(d, (mx - 44, my - 18, mx + 44, my + 18), BRANCO, LARANJA, 8, 2)
        centro_txt(d, (mx, my), txt, FS, LARANJA)
    for nome, (x, y) in pos.items():
        _vertice(d, x, y, nome, fill=MINT, rx=78, ry=36)
    centro_txt(d, (700, 450), "BFS ignora o km: conta arestas. Caminho mais curto em km pede outro algoritmo (depois do curso).", F, PRETO)
    salvar(im, "06_ponderado.png")


def representacao():
    im, d = nova(1400, 620)
    centro_txt(d, (700, 32), "Mesmo grafo, duas representacoes", FT, NAVY)

    pos = {"A": (160, 160), "B": (400, 120), "C": (400, 280), "D": (160, 280)}
    for a, b in [("A", "B"), ("B", "C"), ("A", "D")]:
        d.line([pos[a], pos[b]], fill=TEAL, width=4)
    for nome, (x, y) in pos.items():
        d.ellipse((x - 36, y - 36, x + 36, y + 36), fill=AZUL, outline=NAVY, width=3)
        centro_txt(d, (x, y), nome, FB, NAVY)

    caixa(d, (520, 80, 880, 560), (247, 247, 247), TEAL, 10)
    centro_txt(d, (700, 112), "Lista de adjacencia", FB, TEAL)
    linhas = [
        "A: [B, D]",
        "B: [A, C]",
        "C: [B]",
        "D: [A]",
    ]
    for i, linha in enumerate(linhas):
        centro_txt(d, (700, 190 + i * 70), linha, FB, NAVY)
    centro_txt(d, (700, 500), "Curso usa esta.", FS, TEAL)
    centro_txt(d, (700, 532), "Grafo esparso: poucas arestas.", FS, CINZA)

    caixa(d, (920, 80, 1360, 560), (247, 247, 247), LARANJA, 10)
    centro_txt(d, (1140, 112), "Matriz V x V", FB, LARANJA)
    cab = ["", "A", "B", "C", "D"]
    grid = [
        ["A", "0", "1", "0", "1"],
        ["B", "1", "0", "1", "0"],
        ["C", "0", "1", "0", "0"],
        ["D", "1", "0", "0", "0"],
    ]
    ox, oy = 980, 170
    for j, h in enumerate(cab):
        centro_txt(d, (ox + j * 72, oy), h, FS, CINZA)
    for i, row in enumerate(grid):
        for j, cel in enumerate(row):
            x, y = ox + j * 72, oy + 70 + i * 70
            if j == 0:
                centro_txt(d, (x, y), cel, FS, CINZA)
            else:
                fill = MINT if cel == "1" else BRANCO
                caixa(d, (x - 24, y - 24, x + 24, y + 24), fill, NAVY, 6, 2)
                centro_txt(d, (x, y), cel, FB, NAVY)
    centro_txt(d, (1140, 532), "Olhar aresta e O(1). Gasta O(V^2).", FS, CINZA)
    salvar(im, "06_representacao.png")


def gerar() -> None:
    tipos()
    adjacencia_grau()
    caminho()
    ponderado()
    representacao()


if __name__ == "__main__":
    gerar()
    print("Figuras da Aula 6 em imagens/")
