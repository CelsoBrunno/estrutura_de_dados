"""Gera a apostila em Word (e PDF, se o Word estiver disponível)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import apendice  # noqa: E402
import aulas_1_4  # noqa: E402
import aulas_5_8  # noqa: E402
import estilo as e  # noqa: E402
import figuras  # noqa: E402
import glossario  # noqa: E402
import preambulo  # noqa: E402

SAIDA = HERE / "Apostila-Estruturas-de-Dados.docx"

SUMARIO = [
    (
        "Antes de começar",
        [
            "O que você vai construir",
            "Ferramentas",
            "Calendário (igual ao site)",
        ],
    ),
    (
        e.TITULO_INSTALACAO,
        ["Python 3", "VS Code", "Conferir se está pronto"],
    ),
    (
        e.TITULO_ERROS,
        [
            "Python não encontrado",
            "IndentationError",
            "Arquivo na pasta errada",
            "NoneType e ponteiro",
        ],
    ),
    (
        "Boas práticas de programação",
        [
            "Nomes que explicam",
            "Indentação e uma ideia por vez",
            "Funções curtas",
            "Não se repita",
            "Comente o porquê, não o óbvio",
            "Não copie sem entender",
            "Checklist rápido (todas as aulas)",
        ],
    ),
    (
        "Aula 1 — Fundamentos de Memória, Big-O e Arrays",
        [
            "Como a RAM guarda um array",
            "Big-O em uma frase",
            "Live coding: array estático",
        ],
    ),
    (
        "Aula 2 — Listas Encadeadas (Linked Lists)",
        [
            "Nós e ponteiros",
            "Trade-off de Big-O",
            "Live coding: lista simples",
        ],
    ),
    (
        "Aula 3 — Pilhas (Stacks) e Filas (Queues)",
        ["Pilha — LIFO", "Fila — FIFO", "Live coding: pilha e fila sobre nós"],
    ),
    (
        "Aula 4 — Tabelas Hash (Dicionários/Mapas)",
        [
            "O problema (antes da técnica)",
            "Resposta em uma frase",
            "O dict do Python já é isso",
            "Peças da tabela hash",
            "Inserir e buscar (fluxo mental)",
            "Colisão — o ponto que mais confunde",
            "Exercício na mão (antes do código)",
            "Live coding: tabela com chaining",
        ],
    ),
    (
        "Aula 5 — Árvores Binárias e Árvores de Busca (BST)",
        ["Vocabulário", "Live coding: inserção e travessias"],
    ),
    (
        "Aula 6 — Grafos e Algoritmos de Travessia",
        ["Matriz versus lista de adjacência", "BFS com fila"],
    ),
    (
        "Aula 7 — Heaps e preparação para o projeto",
        ["Índices no array", "Briefing do Projeto Final"],
    ),
    (
        "Aula 8 — Projeto Final (PBL Integrado)",
        [
            "O desafio",
            "O que a avaliação cobra",
            "Roteiro da apresentação (5 a 8 minutos)",
            "Checklist antes de apresentar",
        ],
    ),
    (
        "Apêndice — Código de referência",
        ["Gabarito — Aula 4 (hash)"],
    ),
    (
        "Apêndice — Glossário de funções",
        ["Índice rápido"],
    ),
]


def atualizar_campos_e_pdf(docx_path: Path) -> Path | None:
    """Abre o Word, atualiza PAGEREF/PAGE (números do sumário) e tenta o PDF."""
    docx_path = docx_path.resolve()
    pdf_path = docx_path.with_suffix(".pdf")
    ps = rf"""
$ErrorActionPreference = 'Stop'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$docx = '{docx_path}'
$pdf = '{pdf_path}'
try {{
    $doc = $word.Documents.Open($docx)
    $word.ActiveWindow.View.Type = 3
    $doc.Repaginate()
    foreach ($story in $doc.StoryRanges) {{
        $story.Fields.Update() | Out-Null
        $next = $story.NextStoryRange
        while ($next -ne $null) {{
            $next.Fields.Update() | Out-Null
            $next = $next.NextStoryRange
        }}
    }}
    foreach ($section in $doc.Sections) {{
        foreach ($header in $section.Headers) {{ $header.Range.Fields.Update() | Out-Null }}
        foreach ($footer in $section.Footers) {{ $footer.Range.Fields.Update() | Out-Null }}
    }}
    $doc.Fields.Update() | Out-Null
    $doc.Repaginate()
    $doc.Save()
    try {{
        $doc.SaveAs2($pdf, 17)
        Write-Output "PDF $pdf"
    }} catch {{
        Write-Output "DOCX ok (PDF falhou)"
    }}
    $doc.Close(0)
}} finally {{
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}}
"""
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True)
    return pdf_path if pdf_path.exists() else None


def main() -> None:
    figuras.gerar_todas()
    doc = e.novo_documento()
    preambulo.escrever_capa(doc)
    e.sumario(doc, SUMARIO)
    preambulo.escrever_preambulo(doc)
    aulas_1_4.escrever_aulas_1_4(doc)
    aulas_5_8.escrever_aulas_5_8(doc)
    apendice.escrever_apendice(doc)
    glossario.escrever_glossario(doc)
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
        print("Feche o arquivo no Word e rode de novo, nesta pasta: python gerar_apostila.py")


if __name__ == "__main__":
    main()
