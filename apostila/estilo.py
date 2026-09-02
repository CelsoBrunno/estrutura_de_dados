"""Visual da apostila — mesmo molde de Radar / Algoritmos."""

from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor, Twips

AUTOR = "Celso Brunno Rocha Custódio de Campos"
CURSO = "Estruturas de Dados"
TITULO_INSTALACAO = "Instalação — fazer em casa (não entra na aula)"
TITULO_ERROS = "Se deu erro, faça isto"

LARANJA = RGBColor(0xC4, 0x6B, 0x3A)
COPPER = LARANJA
NAVY = RGBColor(0x0E, 0x24, 0x38)
TEXTO = RGBColor(0x1C, 0x1C, 0x1C)
INK = TEXTO
CINZA = RGBColor(0x5C, 0x5C, 0x5C)
MUTED = CINZA
TEAL = RGBColor(0x1A, 0x6B, 0x64)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)
CAPA_SUB = RGBColor(0xC5, 0xD0, 0xD6)
COD_KW = RGBColor(0xE0, 0x8D, 0x5A)
COD_FN = RGBColor(0xE8, 0xC0, 0x7A)
COD_STR = RGBColor(0x8F, 0xBF, 0x7F)
COD_TXT = RGBColor(0xD6, 0xDE, 0xE4)
COD_CMT = RGBColor(0x7A, 0x8B, 0x99)
COD_NUM = RGBColor(0xD8, 0xC0, 0x72)

HEAD = "Trebuchet MS"
BODY = "Calibri"
MONO = "Consolas"

FILL_CAPA = "0E2438"
FILL_DICA = "F7EFE8"
FILL_ATENCAO = "F8EBE8"
FILL_OBJ = "E8F1F0"
FILL_PRATICA = "F3EEF8"
FILL_CODE = "1E2A32"

BARRA = {
    FILL_DICA: "C46B3A",
    FILL_ATENCAO: "8B1E1E",
    FILL_OBJ: "1A6B64",
    FILL_PRATICA: "6D28D9",
}

LARGURA_CEL = Twips(9638)
PASTA_IMAGENS = Path(__file__).resolve().parent / "imagens"

KEYWORDS = {
    "False", "None", "True", "and", "as", "assert", "break", "class",
    "continue", "def", "del", "elif", "else", "except", "finally", "for",
    "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
    "self",
}
BUILTINS = {
    "print", "len", "range", "list", "dict", "int", "str", "float", "bool",
    "super", "enumerate", "zip", "min", "max", "sum", "abs", "isinstance",
    "hasattr", "open", "input", "type", "sorted", "reversed", "set", "tuple",
}

_TOKEN = re.compile(
    r"(#.*)|"
    r"(f?(?:\"\"\"[\s\S]*?\"\"\"|'''[\s\S]*?'''|\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'))|"
    r"(\b\w+\b)|"
    r"(\s+)|"
    r"(.)",
    re.MULTILINE,
)

_BM_ID = 0
_USED_ANCHORS: set[str] = set()


def toc_anchor(texto: str) -> str:
    """Nome de bookmark válido no Word: letra, número e underscore (sem hífen)."""
    s = unicodedata.normalize("NFKD", texto)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    nome = "s_" + s
    if len(nome) > 40:
        digest = hashlib.md5(texto.encode("utf-8")).hexdigest()[:6]
        nome = nome[:33] + "_" + digest
    return nome


slug = toc_anchor


def novo_documento() -> Document:
    global _BM_ID, _USED_ANCHORS
    _BM_ID = 0
    _USED_ANCHORS = set()
    doc = Document()
    update = OxmlElement("w:updateFields")
    update.set(qn("w:val"), "true")
    doc.settings.element.append(update)
    sec = doc.sections[0]
    sec.page_width = Cm(21)
    sec.page_height = Cm(29.7)
    sec.left_margin = Cm(2)
    sec.right_margin = Cm(2)
    sec.top_margin = Cm(1.9)
    sec.bottom_margin = Cm(2)
    sec.header_distance = Cm(1.27)
    estilo_normal(doc)
    cabecalho(doc)
    rodape(doc)
    return doc


def estilo_normal(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = BODY
    style.font.size = Pt(12)
    style.font.color.rgb = TEXTO
    style.paragraph_format.space_after = Pt(8)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.line_spacing = 1.15


def _rpr(run, nome, tamanho=None, bold=None, cor=None, italic=None):
    run.font.name = nome
    r = run._element.get_or_add_rPr()
    rFonts = r.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        r.append(rFonts)
    rFonts.set(qn("w:ascii"), nome)
    rFonts.set(qn("w:hAnsi"), nome)
    rFonts.set(qn("w:eastAsia"), nome)
    if tamanho is not None:
        run.font.size = Pt(tamanho)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if cor is not None:
        run.font.color.rgb = cor


def _preserve(run):
    t = run._r.find(qn("w:t"))
    if t is not None:
        t.set(qn("xml:space"), "preserve")


def esvaziar(p) -> None:
    for child in list(p._p):
        if child.tag != qn("w:pPr"):
            p._p.remove(child)


def run_txt(p, texto, nome=BODY, tamanho=12, bold=False, cor=TEXTO, italic=False):
    r = p.add_run(texto)
    _rpr(r, nome, tamanho, bold, cor, italic)
    if texto[:1] == " " or texto[-1:] == " " or "\t" in texto:
        _preserve(r)
    return r


def _tight(paragraph, after=6, before=0, line=1.18):
    pf = paragraph.paragraph_format
    pf.space_after = Pt(after)
    pf.space_before = Pt(before)
    pf.line_spacing = line


def _p_border_bottom(paragraph, color="C46B3A", sz="12", space="4"):
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), sz)
    bottom.set(qn("w:space"), space)
    bottom.set(qn("w:color"), color)
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


def _outline(paragraph, level: int):
    p_pr = paragraph._p.get_or_add_pPr()
    node = OxmlElement("w:outlineLvl")
    node.set(qn("w:val"), str(level))
    p_pr.append(node)


def bookmark(paragraph, nome: str) -> None:
    global _BM_ID
    original = nome
    n = 2
    while nome in _USED_ANCHORS:
        nome = f"{original}_{n}"
        n += 1
    _USED_ANCHORS.add(nome)
    _BM_ID += 1
    bid = str(_BM_ID)
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), bid)
    start.set(qn("w:name"), nome)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), bid)
    p_el = paragraph._p
    p_pr = p_el.find(qn("w:pPr"))
    if p_pr is not None:
        p_pr.addnext(start)
    else:
        p_el.insert(0, start)
    p_el.append(end)


def _shade_tc(cell, fill: str) -> None:
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def _set_cell_border(cell, **kwargs) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        if edge not in kwargs:
            continue
        spec = kwargs[edge]
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), spec.get("val", "single"))
        if spec.get("val") != "nil":
            el.set(qn("w:sz"), str(spec.get("sz", 8)))
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), spec.get("color", "000000"))
        borders.append(el)
    tc_pr.append(borders)


def _cell_margins(cell, top=80, bottom=80, left=140, right=140) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for edge, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tc_pr.append(mar)


def _tabela_unica(doc: Document, fill: str, barra: str | None = None):
    tabela = doc.add_table(rows=1, cols=1)
    tabela.alignment = WD_TABLE_ALIGNMENT.CENTER
    tabela.autofit = True
    cell = tabela.cell(0, 0)
    cell.width = LARGURA_CEL
    _shade_tc(cell, fill)
    _cell_margins(cell)
    if barra:
        _set_cell_border(
            cell,
            left={"val": "single", "sz": "28", "color": barra},
            top={"val": "single", "sz": "4", "color": fill},
            bottom={"val": "single", "sz": "4", "color": fill},
            right={"val": "single", "sz": "4", "color": fill},
        )
    else:
        _set_cell_border(
            cell,
            top={"val": "nil"},
            left={"val": "nil"},
            bottom={"val": "nil"},
            right={"val": "nil"},
        )
    esvaziar(cell.paragraphs[0])
    return tabela, cell


def caixa(doc: Document, titulo: str, corpo: str, fill: str) -> None:
    _, cell = _tabela_unica(doc, fill, BARRA.get(fill, "C46B3A"))
    p0 = cell.paragraphs[0]
    p0.paragraph_format.space_after = Pt(2)
    run_txt(p0, titulo, HEAD, 11, True, NAVY)
    if corpo:
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        _texto_misto(p2, corpo, 11)
    _espaco(doc, 8)


def dica(doc, texto):
    caixa(doc, "Dica", texto, FILL_DICA)


def atencao(doc, texto):
    caixa(doc, "Atenção", texto, FILL_ATENCAO)


def boa_pratica(doc, texto):
    caixa(doc, "Boa prática", texto, FILL_DICA)


def objetivo(doc, texto):
    caixa(doc, "Objetivo desta aula (2h30)", texto, FILL_OBJ)


def pratica(doc, titulo, texto):
    caixa(doc, titulo, texto, FILL_PRATICA)


def _texto_misto(p, texto: str, tamanho=12) -> None:
    partes = re.split(r"(`[^`]+`|\*[^*]+\*)", texto)
    for parte in partes:
        if not parte:
            continue
        if parte.startswith("`") and parte.endswith("`") and len(parte) >= 2:
            run_txt(p, parte[1:-1], MONO, tamanho - 1, False, TEAL)
        elif parte.startswith("*") and parte.endswith("*") and len(parte) >= 2:
            run_txt(p, parte[1:-1], BODY, tamanho, False, TEXTO, True)
        else:
            run_txt(p, parte, BODY, tamanho, False, TEXTO)


def corpo(doc: Document, texto: str) -> None:
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(8)
    par.paragraph_format.line_spacing = 1.15
    _texto_misto(par, texto)
    return par


p = corpo


def bullets(doc: Document, itens: list[str]) -> None:
    for item in itens:
        par = doc.add_paragraph()
        _tight(par, after=5)
        par.paragraph_format.left_indent = Cm(0.7)
        par.paragraph_format.first_line_indent = Cm(-0.35)
        run_txt(par, "▸  ", BODY, 10, True, LARANJA)
        _texto_misto(par, item)


def passo(doc: Document, numero: int, texto: str) -> None:
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(6)
    run_txt(par, f"Passo {numero}. ", HEAD, 12, True, LARANJA)
    _texto_misto(par, texto)


def h1(doc: Document, texto: str):
    if " — " in texto:
        kicker, title = texto.split(" — ", 1)
        p1 = doc.add_paragraph()
        _tight(p1, after=2, before=20)
        run_txt(p1, kicker.upper(), HEAD, 9, True, LARANJA)
        p2 = doc.add_paragraph()
        _tight(p2, after=12, before=0)
        run_txt(p2, title, HEAD, 22, True, NAVY)
        _p_border_bottom(p2)
        _outline(p2, 0)
        bookmark(p2, toc_anchor(texto))
        return p2
    par = doc.add_paragraph()
    _tight(par, after=12, before=18)
    run_txt(par, texto, HEAD, 22, True, NAVY)
    _p_border_bottom(par)
    if texto != "Sumário":
        _outline(par, 0)
        bookmark(par, toc_anchor(texto))
    return par


def h2(doc: Document, texto: str):
    par = doc.add_paragraph()
    _tight(par, after=8, before=16)
    run_txt(par, texto, HEAD, 15, True, TEAL)
    _outline(par, 1)
    bookmark(par, toc_anchor(texto))
    return par


def h3(doc: Document, texto: str):
    par = doc.add_paragraph()
    _tight(par, after=6, before=12)
    run_txt(par, texto, HEAD, 12, True, NAVY)
    return par


def h_rotulo(doc: Document, texto: str, bookmark_nome: str | None = None) -> None:
    p1 = doc.add_paragraph()
    p1.paragraph_format.space_before = Pt(12)
    p1.paragraph_format.space_after = Pt(0)
    run_txt(p1, texto, HEAD, 9, True, LARANJA)
    if bookmark_nome:
        bookmark(p1, bookmark_nome)


def h_titulo(doc: Document, texto: str, bookmark_nome: str | None = None) -> None:
    if bookmark_nome is None:
        h1(doc, texto)
        return
    par = doc.add_paragraph()
    _tight(par, after=12, before=0)
    run_txt(par, texto, HEAD, 22, True, NAVY)
    _p_border_bottom(par)
    _outline(par, 0)
    bookmark(par, bookmark_nome)


def h_aula(doc: Document, numero: int, titulo: str) -> None:
    quebra(doc)
    h1(doc, f"Aula {numero} — {titulo}")


def h_secao(doc: Document, texto: str) -> None:
    h2(doc, texto)


def h_antes(doc: Document) -> None:
    h3(doc, "Antes da próxima aula, você precisa conseguir")


def checkpoint(doc: Document, itens: list[str]) -> None:
    h_antes(doc)
    bullets(doc, itens)


def figura(doc: Document, arquivo: str, legenda: str, largura_cm: float = 15.2) -> None:
    caminho = PASTA_IMAGENS / arquivo
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _tight(par, after=4, before=8)
    if caminho.exists():
        par.add_run().add_picture(str(caminho), width=Cm(largura_cm))
    else:
        run_txt(par, f"(Imagem não encontrada: {arquivo}.)", BODY, 11, False, CINZA)
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _tight(cap, after=10, before=0)
    run_txt(cap, legenda, BODY, 9, False, CINZA, True)


def caption(doc: Document, nome_arquivo: str) -> None:
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(8)
    par.paragraph_format.space_after = Pt(0)
    run_txt(par, nome_arquivo, HEAD, 9, True, CINZA)


def _cor_token(tipo: str, texto: str, depois_de_def: bool) -> RGBColor:
    if tipo == "cmt":
        return COD_CMT
    if tipo == "str":
        return COD_STR
    if tipo == "id":
        if texto in KEYWORDS:
            return COD_KW
        if depois_de_def or texto in BUILTINS:
            return COD_FN
        return COD_TXT
    return COD_TXT


def destacar(par, codigo: str) -> None:
    depois_de_def = False
    for m in _TOKEN.finditer(codigo):
        cmt, string, ident, espaco, outro = m.groups()
        if cmt:
            run_txt(par, cmt, MONO, 10, False, COD_CMT)
            depois_de_def = False
        elif string:
            run_txt(par, string, MONO, 10, False, COD_STR)
            depois_de_def = False
        elif ident:
            if ident.isdigit() or re.fullmatch(r"\d+\.\d+", ident):
                run_txt(par, ident, MONO, 10, False, COD_NUM)
            else:
                cor = _cor_token("id", ident, depois_de_def)
                run_txt(par, ident, MONO, 10, False, cor)
            depois_de_def = ident in ("def", "class")
        elif espaco:
            run_txt(par, espaco, MONO, 10, False, COD_TXT)
        else:
            run_txt(par, outro or "", MONO, 10, False, COD_TXT)
            if outro not in (" ",):
                depois_de_def = False


def codigo(doc: Document, fonte: str, arquivo: str | None = None) -> None:
    if arquivo:
        caption(doc, arquivo)
    _, cell = _tabela_unica(doc, FILL_CODE)
    linhas = fonte.replace("\t", "    ").splitlines() or [""]
    first = True
    for linha in linhas:
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.space_before = Pt(0)
        par.paragraph_format.line_spacing = 1.08
        destacar(par, linha if linha else " ")
    _espaco(doc, 8)


def _espaco(doc: Document, pts: int) -> None:
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(pts)
    par.paragraph_format.space_before = Pt(0)


def quebra(doc: Document) -> None:
    doc.add_page_break()


def _hex(color: RGBColor) -> str:
    return f"{int(color[0]):02X}{int(color[1]):02X}{int(color[2]):02X}"


def _toc_tab(paragraph, pos="9600"):
    p_pr = paragraph._p.get_or_add_pPr()
    tabs = OxmlElement("w:tabs")
    tab = OxmlElement("w:tab")
    tab.set(qn("w:val"), "right")
    tab.set(qn("w:leader"), "dot")
    tab.set(qn("w:pos"), pos)
    tabs.append(tab)
    p_pr.append(tabs)


def _toc_link(paragraph, anchor, text, *, size, color, bold=False, font=BODY):
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), anchor)
    hyperlink.set(qn("w:history"), "1")
    run = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    r_fonts = OxmlElement("w:rFonts")
    r_fonts.set(qn("w:ascii"), font)
    r_fonts.set(qn("w:hAnsi"), font)
    r_pr.append(r_fonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    r_pr.append(sz)
    col = OxmlElement("w:color")
    col.set(qn("w:val"), _hex(color))
    r_pr.append(col)
    if bold:
        r_pr.append(OxmlElement("w:b"))
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "none")
    r_pr.append(u)
    run.append(r_pr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def _pageref(paragraph, anchor):
    def fld_char(kind):
        r = OxmlElement("w:r")
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), kind)
        r.append(fc)
        return r

    paragraph._p.append(fld_char("begin"))
    r = OxmlElement("w:r")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = f" PAGEREF {anchor} \\h "
    r.append(instr)
    paragraph._p.append(r)
    paragraph._p.append(fld_char("separate"))
    ph = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    col = OxmlElement("w:color")
    col.set(qn("w:val"), "C46B3A")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "18")
    r_pr.append(col)
    r_pr.append(sz)
    ph.append(r_pr)
    t = OxmlElement("w:t")
    t.text = "·"
    ph.append(t)
    paragraph._p.append(ph)
    paragraph._p.append(fld_char("end"))


def _add_page_field(paragraph):
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    rr = OxmlElement("w:r")
    r_pr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "16")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "C46B3A")
    r_pr.append(sz)
    r_pr.append(color)
    rr.append(r_pr)
    t = OxmlElement("w:t")
    t.text = "1"
    rr.append(t)
    fld.append(rr)
    paragraph._p.append(fld)


def cabecalho(doc: Document) -> None:
    par = doc.sections[0].header.paragraphs[0]
    esvaziar(par)
    par.alignment = WD_ALIGN_PARAGRAPH.LEFT
    _tight(par, after=2, before=0)
    run_txt(par, "PYTHON", HEAD, 8, True, LARANJA)
    run_txt(par, f"    Apostila passo a passo  ·  {CURSO}", BODY, 8, False, CINZA)
    _p_border_bottom(par, color="C46B3A", sz="8", space="4")


def rodape(doc: Document) -> None:
    par = doc.sections[0].footer.paragraphs[0]
    esvaziar(par)
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _tight(par, after=0, before=4)
    run_txt(par, f"{AUTOR}  ·  {CURSO}  ·  ", BODY, 8, False, CINZA)
    _add_page_field(par)


def capa(doc: Document) -> None:
    tabela = doc.add_table(rows=1, cols=1)
    tabela.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tabela.cell(0, 0)
    _shade_tc(cell, FILL_CAPA)
    _cell_margins(cell, top=360, bottom=320, left=280, right=280)
    _set_cell_border(
        cell,
        top={"val": "nil"},
        left={"val": "single", "sz": 48, "color": "C46B3A"},
        bottom={"val": "nil"},
        right={"val": "nil"},
    )
    esvaziar(cell.paragraphs[0])
    p0 = cell.paragraphs[0]
    _tight(p0, after=6, before=0)
    run_txt(p0, "CURSO DE PYTHON", HEAD, 11, True, LARANJA)

    p2 = cell.add_paragraph()
    _tight(p2, after=8, before=4)
    run_txt(p2, CURSO, HEAD, 32, True, BRANCO)

    p3 = cell.add_paragraph()
    _tight(p3, after=10, before=0)
    run_txt(
        p3,
        "Apostila passo a passo: da memória RAM ao projeto final",
        BODY,
        13,
        False,
        CAPA_SUB,
        True,
    )

    p4 = cell.add_paragraph()
    _tight(p4, after=4, before=8)
    run_txt(p4, "Python 3   ·   VS Code   ·   estruturas do zero", HEAD, 10, False, LARANJA)

    p5 = cell.add_paragraph()
    _tight(p5, after=2, before=16)
    run_txt(p5, "APOSTILA ELABORADA POR", HEAD, 8, True, LARANJA)

    p6 = cell.add_paragraph()
    _tight(p6, after=4, before=0)
    run_txt(p6, f"Professor {AUTOR}", HEAD, 14, True, BRANCO)

    doc.add_paragraph()
    caixa(
        doc,
        "Como esta apostila funciona",
        "Você não pula para o simulador pronto. Em cada aula faz uma estrutura "
        "simples, lê o que aquilo significa e só então volta e edita. O projeto "
        "final nasce assim: array, lista, pilha, fila, hash, árvore, grafo e heap.",
        FILL_DICA,
    )
    caixa(
        doc,
        "Uso desta apostila",
        f"© 2026 {AUTOR}. Material de uso didático.\n"
        "É vedada a reprodução, distribuição ou comercialização sem autorização do autor.\n"
        "O aluno pode usar o conteúdo para estudar e montar o projeto do curso.",
        FILL_ATENCAO,
    )
    quebra(doc)


def sumario(doc: Document, entries) -> None:
    h1(doc, "Sumário")
    corpo(doc, "Clique no título para ir à seção.")
    for title, children in entries:
        if " — " in title:
            kicker, rest = title.split(" — ", 1)
            k = doc.add_paragraph()
            _tight(k, after=0, before=12)
            run_txt(k, kicker.upper(), HEAD, 8, True, LARANJA)
            label = rest
            title_before = 0
        else:
            label = title
            title_before = 12
        par = doc.add_paragraph()
        _tight(par, after=3, before=title_before, line=1.15)
        _toc_tab(par)
        _toc_link(par, toc_anchor(title), label, size=13, color=NAVY, bold=True, font=HEAD)
        par.add_run("\t")
        _pageref(par, toc_anchor(title))
        for child in children:
            c = doc.add_paragraph()
            _tight(c, after=1, before=0, line=1.12)
            c.paragraph_format.left_indent = Cm(0.55)
            _toc_tab(c, "9600")
            _toc_link(c, toc_anchor(child), child, size=10.5, color=TEAL, font=BODY)
            c.add_run("\t")
            _pageref(c, toc_anchor(child))
    quebra(doc)


def frase_com_pagina(par, titulo_h1, rotulo):
    _toc_link(par, toc_anchor(titulo_h1), rotulo, size=11, color=LARANJA, bold=True, font=HEAD)
    t = par.add_run("  (pág. ")
    _rpr(t, BODY, 11, False, CINZA)
    _pageref(par, toc_anchor(titulo_h1))
    f = par.add_run(")")
    _rpr(f, BODY, 11, False, CINZA)


_frase_com_pagina = frase_com_pagina


def aviso_ferramenta(doc: Document, programa: str) -> None:
    """Aviso de aula: instalação já deveria estar feita; aponta o capítulo com o passo a passo."""
    _, cell = _tabela_unica(doc, FILL_DICA, "C46B3A")
    t = cell.paragraphs[0]
    t.paragraph_format.space_after = Pt(2)
    run_txt(t, f"Para seguir, use o {programa}", HEAD, 11, True, NAVY)
    q = cell.add_paragraph()
    q.paragraph_format.space_after = Pt(2)
    a = q.add_run("A instalação não entra no tempo de aula. Se ainda não tiver o programa, faça o passo a passo em ")
    _rpr(a, BODY, 11, False, TEXTO)
    frase_com_pagina(q, TITULO_INSTALACAO, "Instalação")
    err = cell.add_paragraph()
    err.paragraph_format.space_after = Pt(0)
    b = err.add_run("Se a tela falhar (Python não encontrado, pasta errada, NoneType), vá para ")
    _rpr(b, BODY, 11, False, TEXTO)
    frase_com_pagina(err, TITULO_ERROS, "Se deu erro, faça isto")
    _espaco(doc, 8)


def salvar(doc: Document, caminho: Path) -> Path:
    try:
        doc.save(caminho)
        return caminho
    except PermissionError:
        alt = caminho.with_name(caminho.stem + "-atualizado.docx")
        doc.save(alt)
        return alt
