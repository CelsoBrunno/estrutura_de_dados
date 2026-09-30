"""Gera a apostila da aula extra de Huffman (Word e PDF)."""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import aula_huffman  # noqa: E402
import estilo as e  # noqa: E402
import figuras_huffman  # noqa: E402
from gerar_apostila import atualizar_campos_e_pdf  # noqa: E402

SAIDA = HERE / "Apostila-Huffman-Compactacao.docx"

SUMARIO = [
    (
        "Antes de começar",
        [
            "O que você vai construir hoje",
            "O que precisa já saber",
            "Roteiro das 2h30",
        ],
    ),
    (
        "Aula extra — Compactação com Huffman",
        [
            "O problema (8 bits para tudo)",
            "Resposta em uma frase",
            "Código prefixo-livre",
            "Exemplo na mão: BANANA",
            "Juntar sempre os dois menores",
            "Ler os bits na árvore",
            "Compactar letra a letra",
            "Descompactar bit a bit",
            "Live coding",
            "O arquivo .huff",
            "O que o ZIP faz a mais",
            "Prática de hoje",
        ],
    ),
]


def main() -> None:
    figuras_huffman.gerar_todas()
    doc = e.novo_documento()
    e.capa(
        doc,
        titulo="Compactação com Huffman",
        subtitulo="Aula extra: da frequência à árvore, do bit ao arquivo .huff",
        linha_tech="Python 3   ·   VS Code   ·   hash + árvore + prioridade",
        como_funciona=(
            "Um encontro de 2h30. Primeiro a mensagem BANANA no quadro (contar, juntar, "
            "árvore, bits). Depois o código em exemplos/huffman.py e um recado honesto "
            "sobre o que o ZIP faz a mais. Não substitui as 8 aulas do curso: usa o que "
            "elas já ensinaram."
        ),
    )
    e.sumario(doc, SUMARIO)
    aula_huffman.escrever_preambulo(doc)
    aula_huffman.escrever_aula(doc)
    gerado = e.salvar(doc, SAIDA)
    print(f"Word: {gerado}")
    try:
        pdf = atualizar_campos_e_pdf(gerado)
        if pdf:
            print(f"PDF:  {pdf}")
        else:
            print("Campos do sumário atualizados no Word.")
    except Exception as exc:
        print(f"Não deu para atualizar os números no Word automaticamente: {exc}")
        print("Feche o arquivo no Word e rode de novo, nesta pasta: python gerar_apostila_huffman.py")


if __name__ == "__main__":
    main()
