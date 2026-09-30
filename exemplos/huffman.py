"""Compactação Huffman — aula extra (hoje).

Texto de teste: BANANA
  A aparece 3 vezes, N 2, B 1.
  Códigos: A=0, B=10, N=11
  Bits: 100110110  (9 bits em vez de 48 do ASCII)
"""

from pathlib import Path


class No:
    def __init__(self, freq, simbolo=None, esquerda=None, direita=None, ordem=0):
        self.freq = freq
        self.simbolo = simbolo
        self.esquerda = esquerda
        self.direita = direita
        self.ordem = ordem

    def eh_folha(self):
        return self.simbolo is not None


def contar(texto):
    freq = {}
    for letra in texto:
        freq[letra] = freq.get(letra, 0) + 1
    return freq


def construir_arvore(freq):
    floresta = []
    ordem = 0
    for simbolo in sorted(freq):
        floresta.append(No(freq[simbolo], simbolo, ordem=ordem))
        ordem += 1

    if len(floresta) == 1:
        unico = floresta[0]
        return No(unico.freq, esquerda=unico, ordem=ordem)

    while len(floresta) > 1:
        floresta.sort(key=lambda no: (no.freq, no.ordem))
        a = floresta.pop(0)
        b = floresta.pop(0)
        pai = No(a.freq + b.freq, esquerda=a, direita=b, ordem=ordem)
        ordem += 1
        floresta.append(pai)
    return floresta[0]


def tabela_codigos(raiz):
    codigos = {}

    def caminhar(no, prefixo):
        if no.eh_folha():
            codigos[no.simbolo] = prefixo or "0"
            return
        caminhar(no.esquerda, prefixo + "0")
        caminhar(no.direita, prefixo + "1")

    caminhar(raiz, "")
    return codigos


def compactar(texto):
    freq = contar(texto)
    raiz = construir_arvore(freq)
    codigos = tabela_codigos(raiz)
    bits = "".join(codigos[letra] for letra in texto)
    return raiz, codigos, bits


def descompactar(raiz, bits):
    letras = []
    no = raiz
    for bit in bits:
        no = no.esquerda if bit == "0" else no.direita
        if no.eh_folha():
            letras.append(no.simbolo)
            no = raiz
    return "".join(letras)


def salvar_huff(caminho, codigos, bits):
    with open(caminho, "w", encoding="utf-8") as arq:
        arq.write("HUFFMAN\n")
        for simbolo in sorted(codigos):
            arq.write(f"{simbolo} {codigos[simbolo]}\n")
        arq.write("---\n")
        arq.write(bits)
        arq.write("\n")


def abrir_huff(caminho):
    with open(caminho, "r", encoding="utf-8") as arq:
        linhas = [linha.rstrip("\n") for linha in arq]
    if not linhas or linhas[0] != "HUFFMAN":
        raise ValueError("Arquivo .huff inválido.")
    codigos = {}
    i = 1
    while i < len(linhas) and linhas[i] != "---":
        simbolo, codigo = linhas[i].split(" ", 1)
        codigos[simbolo] = codigo
        i += 1
    bits = "".join(linhas[i + 1 :])
    return codigos, bits


def descompactar_tabela(codigos, bits):
    inverso = {codigo: simbolo for simbolo, codigo in codigos.items()}
    letras = []
    atual = ""
    for bit in bits:
        atual += bit
        if atual in inverso:
            letras.append(inverso[atual])
            atual = ""
    if atual:
        raise ValueError("Sobrou bit sem código. A tabela ou os bits estão errados.")
    return "".join(letras)


if __name__ == "__main__":
    texto = "BANANA"
    raiz, codigos, bits = compactar(texto)
    print("Frequência:", contar(texto))
    print("Códigos:", codigos)
    print("Bits:", bits)
    print("Tamanho ASCII:", len(texto) * 8, "bits")
    print("Tamanho Huffman:", len(bits), "bits")
    volta = descompactar(raiz, bits)
    print("Volta pela árvore:", volta)
    saida = Path(__file__).resolve().parent / "banana.huff"
    salvar_huff(saida, codigos, bits)
    tab, bits_arquivo = abrir_huff(saida)
    print("Volta pelo arquivo:", descompactar_tabela(tab, bits_arquivo))
