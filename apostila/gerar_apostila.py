"""Gera Apostila-Estruturas-de-Dados.docx no molde Radar / Algoritmos."""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import estilo as e  # noqa: E402
import figuras  # noqa: E402
import preambulo  # noqa: E402
import aulas_1_4  # noqa: E402
import aulas_5_8  # noqa: E402
import apendice  # noqa: E402

SAIDA = HERE / "Apostila-Estruturas-de-Dados.docx"


def atualizar_campos_word(caminho: Path) -> bool:
    try:
        import win32com.client  # type: ignore
    except ImportError:
        return False
    word = None
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(str(caminho))
        doc.Fields.Update()
        for secao in doc.Sections:
            secao.Headers(1).Range.Fields.Update()
            secao.Footers(1).Range.Fields.Update()
        doc.Save()
        doc.Close()
        return True
    except Exception as exc:
        print("Word não atualizou o sumário:", exc)
        return False
    finally:
        if word is not None:
            try:
                word.Quit()
            except Exception:
                pass


def main() -> None:
    figuras.gerar_todas()
    doc = e.novo_documento()
    preambulo.escrever_capa(doc)
    preambulo.escrever_sumario(doc)
    preambulo.escrever_preambulo(doc)
    aulas_1_4.escrever_aulas_1_4(doc)
    aulas_5_8.escrever_aulas_5_8(doc)
    apendice.escrever_apendice(doc)
    try:
        doc.save(SAIDA)
        destino = SAIDA
    except PermissionError:
        destino = HERE / "Apostila-Estruturas-de-Dados-nova.docx"
        doc.save(destino)
        print("Arquivo original aberto no Word. Salvei em:", destino)
    print("Salvo:", destino)
    if atualizar_campos_word(destino):
        print("Sumário e números de página atualizados no Word.")
    else:
        print(
            "Abra o Word e pressione Ctrl+A, depois F9, para atualizar o sumário "
            "(se o Word estiver instalado)."
        )


if __name__ == "__main__":
    main()
