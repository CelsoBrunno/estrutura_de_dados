"""Rascunho isolado da Aula 4 — não altera a apostila completa.

Gera Word/PDF só desta aula:

    cd apostila
    python aula4.py

Quando o texto estiver pronto, este arquivo entra no gerar_apostila.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import estilo as e  # noqa: E402
import figuras  # noqa: E402

SAIDA = HERE / "Apostila-Aula-4.docx"

SUMARIO = [
    (
        "Aula 4 — Tabelas Hash (Dicionários/Mapas)",
        [
            "O problema (antes da técnica)",
            "Resposta em uma frase",
            "O dict do Python já é isso",
            "Peças da tabela hash",
            "A classe TabelaHash — por que criar",
            "Inserir e buscar (fluxo mental)",
            "Colisão — o ponto que mais confunde",
            "Exercício na mão (antes do código)",
            "Live coding: tabela com chaining",
            "Quando o prédio fica pequeno — crescer a tabela",
        ],
    ),
]

DICT_NATIVO = '''pessoa = {"nome": "Bruna", "idade": "20"}
print(pessoa["nome"])  # rápido — o dict já é hash
'''

CLASSE_ESQUELETO = '''class TabelaHash:
    def __init__(self, tamanho=8):
        self.tamanho = tamanho
        self.baldes = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return sum(ord(c) for c in str(chave)) % self.tamanho


catalogo = TabelaHash(5)
'''

ESQUEMA_BALDES = '''tamanho = 5

baldes:
  [0] []
  [1] []
  [2] [ ["u001", "João"], ["outra", "..."] ]   ← colisão
  [3] [ ["u002", "Maria"] ]
  [4] []
'''

HASH = '''class TabelaHash:
    def __init__(self, tamanho=8):
        self.tamanho = tamanho
        self.baldes = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return sum(ord(c) for c in str(chave)) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.baldes[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                return par[1]
        return None


catalogo = TabelaHash(5)
catalogo.inserir("u001", "João Silva")
catalogo.inserir("u002", "Maria Souza")
print("Busca u001:", catalogo.buscar("u001"))
print("Busca u999:", catalogo.buscar("u999"))
'''

HASH_DINAMICO = '''class TabelaHash:
    def __init__(self, tamanho=8, limite=0.75):
        self.tamanho = tamanho      # tamanho *inicial* — pode dobrar
        self.limite = limite        # critério: fator de carga
        self.quantidade = 0
        self.baldes = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return sum(ord(c) for c in str(chave)) % self.tamanho

    def fator_carga(self):
        return self.quantidade / self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for par in self.baldes[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.baldes[indice].append([chave, valor])
        self.quantidade += 1
        if self.fator_carga() > self.limite:
            self._crescer()

    def _crescer(self):
        antigos = []
        for balde in self.baldes:
            antigos.extend(balde)
        self.tamanho *= 2
        self.baldes = [[] for _ in range(self.tamanho)]
        for chave, valor in antigos:
            indice = self._hash(chave)
            self.baldes[indice].append([chave, valor])
'''

INSERIR_1 = '''def inserir(self, chave, valor):
    indice = self._hash(chave)
'''

INSERIR_2 = '''def inserir(self, chave, valor):
    indice = self._hash(chave)
    for par in self.baldes[indice]:
        ...
'''

INSERIR_3 = '''def inserir(self, chave, valor):
    indice = self._hash(chave)
    for par in self.baldes[indice]:
        if par[0] == chave:
            par[1] = valor
            return
'''

INSERIR_4 = '''def inserir(self, chave, valor):
    indice = self._hash(chave)
    for par in self.baldes[indice]:
        if par[0] == chave:
            par[1] = valor
            return
    self.baldes[indice].append([chave, valor])
'''

BUSCAR_1 = '''def buscar(self, chave):
    indice = self._hash(chave)
'''

BUSCAR_2 = '''def buscar(self, chave):
    indice = self._hash(chave)
    for par in self.baldes[indice]:
        ...
'''

BUSCAR_3 = '''def buscar(self, chave):
    indice = self._hash(chave)
    for par in self.baldes[indice]:
        if par[0] == chave:
            return par[1]
    return None
'''


def escrever_aula4(doc, quebrar=True):
    if quebrar:
        e.quebra(doc)
    e.h1(doc, "Aula 4 — Tabelas Hash (Dicionários/Mapas)")
    e.objetivo(
        doc,
        "Entender o porquê do hash, mapear chave → índice, tratar colisão por encadeamento "
        "e buscar em tempo médio `O(1)` — sem usar o `dict` nativo no catálogo da aula.",
    )
    e.aviso_ferramenta(doc, "VS Code")
    e.corpo(
        doc,
        "Gancho da Aula 3: o gerente quer o cliente “Carlos” sem percorrer a fila inteira. "
        "Array é `O(1)` por índice, mas o índice não é o CPF. Hash transforma a chave em índice.",
    )

    e.h_secao(doc, "O problema (antes da técnica)")
    e.corpo(
        doc,
        "Com array, achar `dados[3]` é instantâneo (`O(1)`): você já sabe o endereço. "
        "Na vida real a pergunta costuma ser outra: “qual o nome do usuário `u001`?” ou "
        "“qual o preço do produto `SKU-9981`?”. Aqui a chave *não* é o índice. Se você só "
        "tiver uma lista, precisa percorrer até achar → `O(n)`.",
    )
    e.corpo(
        doc,
        "*Pergunta da aula:* como transformar uma chave qualquer (texto, id, CPF) em um índice rápido?",
    )

    e.h_secao(doc, "Resposta em uma frase")
    e.corpo(
        doc,
        "*Hash* = função que transforma a chave em um número; esse número vira o índice de "
        "um “balde” na tabela. Depois disso, você só procura *dentro daquele balde*, não na "
        "tabela inteira.",
    )
    e.corpo(
        doc,
        "Analogia do prédio: imagine 5 andares (baldes 0 a 4). Chega a moradora com a chave "
        "`\"u001\"`. O porteiro (função de hash) calcula: “ela mora no andar 2”. Você sobe "
        "*só* o andar 2 e procura o nome na listinha daquele andar. Se duas pessoas caírem "
        "no mesmo andar, as duas ficam na listinha — isso é *colisão*. Ainda assim você não "
        "vasculha o prédio inteiro.",
    )

    e.h_secao(doc, "O dict do Python já é isso")
    e.codigo(doc, DICT_NATIVO)
    e.corpo(
        doc,
        "O `dict` nativo *é* uma tabela hash (bem otimizada). Nesta aula você *não* usa o "
        "`dict` para guardar o catálogo: recria a ideia na mão, para entender o que o Python "
        "faz por baixo.",
    )
    e.bullets(
        doc,
        [
            "`dict` do Python — hash pronto, uso diário.",
            "`TabelaHash` da aula — hash didático, para estudar o mecanismo.",
        ],
    )

    e.h_secao(doc, "Peças da tabela hash")
    e.bullets(
        doc,
        [
            "*Tabela* — array de tamanho fixo (ex.: 5 ou 8 posições).",
            "*Balde* — cada posição é uma listinha (vazia no início).",
            "*Função de hash* — transforma a chave em inteiro.",
            "*Índice* — `hash(chave) % tamanho` (fica entre `0` e `tamanho - 1`).",
            "*Par* — dentro do balde guardamos `[chave, valor]`.",
        ],
    )
    e.dica(
        doc,
        "*Balde* é o nome padrão (em inglês: *bucket*). Não chamamos só de “posição” "
        "porque cada índice é um *recipiente*: pode estar vazio, ter um par ou vários "
        "(quando há colisão). Na analogia, “andar” ajuda a imaginar; na estrutura, o "
        "nome técnico é balde. Outros textos usam *slot* (endereçamento aberto) ou *bin*.",
    )
    e.codigo(doc, ESQUEMA_BALDES)

    e.h_secao(doc, "A classe TabelaHash — por que criar")
    e.corpo(
        doc,
        "As peças (tamanho, baldes, porteiro) *andam juntas*. Se fossem variáveis soltas, "
        "cada função precisaria receber `baldes` e `tamanho` na mão. A *classe* é o "
        "molde do prédio: um só lugar guarda os andares e o porteiro que calcula o andar.",
    )
    e.corpo(
        doc,
        "Por isso criamos `class TabelaHash` *antes* de `inserir` e `buscar`. Sem a classe "
        "não existe `self` — e sem `self` o porteiro não sabe quantos andares *este* "
        "prédio tem.",
    )
    e.bullets(
        doc,
        [
            "`class TabelaHash` — o projeto do prédio (molde).",
            "`__init__` — roda quando o prédio é construído: define quantos andares e "
            "abre as listinhas vazias.",
            "`_hash` — o porteiro *deste* prédio. O `_` na frente = método interno "
            "(a classe usa; o aluno de fora chama `inserir` / `buscar`).",
            "`self` — “este objeto”. Quando você faz `catalogo.inserir(...)`, o Python "
            "coloca o `catalogo` no `self`.",
            "`catalogo = TabelaHash(5)` — um prédio de verdade, com 5 andares. Dá para "
            "ter outro: `produtos = TabelaHash(8)` — outro prédio, outros baldes.",
        ],
    )
    e.codigo(doc, CLASSE_ESQUELETO, "esqueleto — ainda sem inserir/buscar")
    e.corpo(
        doc,
        "Fórmula didática do curso, agora *dentro* da classe: "
        "`indice = (soma dos códigos dos caracteres) % self.tamanho`.",
    )
    e.dica(
        doc,
        "`self._hash(chave)` (que vem no próximo bloco) é o `catalogo` chamando o "
        "*próprio* porteiro. [[ord()]] devolve o código do caractere; [[sum()]] soma; "
        "[[%]] cabe o índice na tabela. Essa função é *só para aprender* — a do `dict` "
        "real é mais sofisticada.",
    )
    e.figura(
        doc,
        "04_hash.png",
        "Cada balde é uma listinha. Duas chaves no mesmo índice = colisão; as duas ficam no encadeamento.",
    )

    _fluxo_mental(doc)

    e.h_secao(doc, "Colisão — o ponto que mais confunde")
    e.corpo(
        doc,
        "*Colisão* = duas chaves *diferentes* geram o *mesmo* índice. Isso *não é erro*: "
        "é esperado. Tratamento desta aula: *encadeamento (chaining)* — cada balde é uma "
        "listinha; as chaves colidentes ficam juntas no mesmo balde (lista da Aula 2 em miniatura).",
    )
    e.bullets(
        doc,
        [
            "Chaves bem espalhadas, tabela folgada → busca média ≈ `O(1)`.",
            "Quase tudo no mesmo balde → piora para `O(n)`.",
        ],
    )
    e.atencao(
        doc,
        "Por isso o tamanho da tabela importa. Tabela pequena demais → mais colisões → "
        "mais lento. Tempo médio `O(1)` *assume* tabela folgada e hash espalhada.",
    )

    e.h_secao(doc, "Comparação rápida (não misture com as outras aulas)")
    e.bullets(
        doc,
        [
            "Lista encadeada — inserir no início fácil; busca `O(n)`.",
            "Array por índice — `O(1)` se souber o índice; índice ≠ CPF / id.",
            "Hash — busca por chave ≈ `O(1)` médio; não mantém ordem; há colisões.",
            "BST (Aula 5) — mantém ordem + busca `O(log n)`; mais complexa.",
        ],
    )
    e.corpo(
        doc,
        "No projeto final (logística): hash guarda `id_pacote → dados`; heap decide "
        "prioridade; grafo acha a rota. Hash acha a *ficha* do pacote — não decide quem "
        "sai primeiro (isso é heap).",
    )

    e.h_secao(doc, "Exercício na mão (antes do código)")
    e.corpo(
        doc,
        "Use tabela de tamanho `5` e a função do curso: "
        "`indice = sum(ord(c) for c in chave) % 5` "
        "(veja [[ord()]], [[sum()]] e [[%]] no glossário). "
        "Códigos úteis: `u`=117, `0`=48, `1`=49, `2`=50, `a`=97, `b`=98.",
    )
    e.pratica(
        doc,
        "Parte A — Calcular índices",
        "Calcule o índice de `\"u001\"`, `\"u002\"`, `\"ab\"` e `\"ba\"`. "
        "Anote: chave | soma dos ord | soma % 5 | balde.",
    )
    e.pratica(
        doc,
        "Parte B — Desenhar a tabela",
        "Insira `\"u001\" → \"João\"` e `\"u002\" → \"Maria\"`. Desenhe os 5 baldes e o "
        "conteúdo de cada um.",
    )
    e.pratica(
        doc,
        "Parte C — Forçar colisão",
        "Ache duas chaves diferentes no mesmo balde. Sugestão: `\"ab\"` e `\"ba\"` têm os "
        "mesmos caracteres → mesma soma → colidem de propósito com esta função didática. "
        "Desenhe de novo o balde com dois pares.",
    )
    e.pratica(
        doc,
        "Parte D — Busca mental",
        "1) Para buscar `\"u001\"`, quantos baldes você abre? "
        "2) Se o balde tiver 2 pares, o que você compara? "
        "3) Se o tamanho da tabela for `1`, o que acontece com todas as inserções?",
    )
    e.dica(
        doc,
        "Gabarito no Apêndice — olhe *só depois* de tentar no papel.",
    )

    e.h_secao(doc, "Live coding: tabela com chaining")
    e.codigo(doc, HASH, "exemplos/04_hash.py")
    e.boa_pratica(
        doc,
        "Ao inserir, primeiro percorra o balde: se a chave já existe, atualize o valor. "
        "Senão a mesma chave aparece duas vezes e a busca pega a antiga.",
    )

    e.h_secao(doc, "Quando o prédio fica pequeno — crescer a tabela")
    e.corpo(
        doc,
        "`tamanho=8` no `__init__` é o tamanho *inicial*, não um teto. Encadeamento "
        "aguenta gente demais no mesmo andar, mas a listinha incha e a busca deixa de "
        "ser `O(1)`. O critério clássico é o *fator de carga*:",
    )
    e.codigo(doc, "fator = quantidade_de_itens / tamanho_da_tabela")
    e.corpo(
        doc,
        "Quando o fator passa de um limite (nesta aula: `0.75`), dobramos os andares e "
        "o porteiro *recoloca todo mundo*. Isso se chama *rehash*: o resto muda, então "
        "o andar de `\"ab\"` em 5 andares (`195 % 5 = 0`) não é o mesmo em 10 "
        "(`195 % 10 = 5`). Sem recolocar, a busca iria ao andar errado.",
    )
    e.passo(doc, 1, "Contar os itens: `self.quantidade` sobe só em inserção *nova* (atualizar não conta).")
    e.passo(doc, 2, "Depois do `append`, se `quantidade / tamanho > 0.75` → crescer.")
    e.passo(doc, 3, "`_crescer`: guardar os pares, `tamanho *= 2`, baldes novos, recolocar com `_hash`.")
    e.atencao(
        doc,
        "Não chame `inserir` de dentro de `_crescer`. `inserir` pode disparar outro "
        "crescimento. Recoloque os pares direto no balde novo.",
    )
    e.codigo(doc, HASH_DINAMICO, "exemplos/04_hash_dinamico.py")
    e.dica(
        doc,
        "O `dict` do Python também cresce por fator de carga (bem mais sofisticado). "
        "Na Aula 4 o `04_hash.py` continua *fixo* de propósito: primeiro o fluxo, "
        "depois o extra de crescer.",
    )

    e.h_secao(doc, "Práticas no computador")
    e.pratica(
        doc,
        "Prática — Catálogo de usuários / cache",
        "Rode `python exemplos/04_hash.py`. Guarde id → nome (ou url → conteúdo). Busque "
        "por chave. Mude o tamanho para `5`, imprima `catalogo.baldes` após cada inserção, "
        "force uma colisão e mostre os dois pares no mesmo balde. Explique em voz alta o "
        "que `_hash`, `inserir` e `buscar` fazem — sem olhar o código. Depois rode "
        "`python exemplos/04_hash_dinamico.py`: comece com tamanho `4` e veja o "
        "`tamanho` dobrar quando o fator passar de `0.75`.",
    )

    e.checkpoint(
        doc,
        [
            "Por que hash existe, se já temos lista?",
            "O que significa `hash(chave) % tamanho`?",
            "O que é colisão e como o encadeamento resolve?",
            "Por que o tempo médio é `O(1)`, e quando isso falha?",
            "Em uma frase: diferença entre `dict` nativo e a `TabelaHash` da aula.",
            "O que é fator de carga e por que, ao crescer, é preciso recolocar as chaves?",
        ],
    )


def _fluxo_mental(doc):
    e.h_secao(doc, "Inserir e buscar (fluxo mental)")
    e.corpo(
        doc,
        "A classe já existe: `__init__` abriu os baldes e `_hash` é o porteiro. "
        "`inserir` e `buscar` usam `self._hash` porque estão *dentro do mesmo prédio*. "
        "Agora montamos esses dois métodos um passo de cada vez — o código cresce até "
        "ficar igual ao `exemplos/04_hash.py`.",
    )

    e.corpo(doc, "Inserir `\"u001\" → \"João\"`:")
    e.passo(doc, 1, "Calcular `indice = self._hash(\"u001\")`.")
    e.corpo(
        doc,
        "O porteiro transforma a chave em andar. Com a função da aula, `\"u001\"` "
        "soma 262 e `262 % 5 = 2` — balde 2.",
    )
    e.codigo(doc, INSERIR_1, "inserir — passo 1")

    e.passo(doc, 2, "Ir ao `baldes[indice]`.")
    e.corpo(
        doc,
        "Você sobe *só* aquele andar. O `for` percorre a listinha do balde 2 — os "
        "outros nem são abertos.",
    )
    e.codigo(doc, INSERIR_2, "inserir — passo 2")

    e.passo(
        doc,
        3,
        "Se a chave *já existe* nesse balde → atualiza o valor (não duplica).",
    )
    e.corpo(
        doc,
        "`par[0]` é a chave; `par[1]` é o valor. Se achar `\"u001\"` de novo, "
        "só troca o nome e dá `return` — não cria outro par.",
    )
    e.codigo(doc, INSERIR_3, "inserir — passo 3")

    e.passo(doc, 4, "Se não existe → [[append()]] `[chave, valor]` na listinha.")
    e.corpo(
        doc,
        "O `for` acabou sem achar a chave: o andar estava vazio (ou tinha outras "
        "pessoas, mas não o `u001`). Aí entra o par novo.",
    )
    e.codigo(doc, INSERIR_4, "inserir — passo 4 (método completo)")
    e.codigo(
        doc,
        'catalogo.inserir("u001", "João")\n# baldes[2] agora: [["u001", "João"]]',
        "depois do passo 4",
    )

    e.corpo(doc, "Buscar `\"u001\"`:")
    e.passo(doc, 1, "Calcular o *mesmo* índice.")
    e.corpo(
        doc,
        "A mesma chave *tem* que cair no mesmo andar. Por isso inserir e buscar "
        "usam a *mesma* `_hash`.",
    )
    e.codigo(doc, BUSCAR_1, "buscar — passo 1")

    e.passo(doc, 2, "Percorrer *só* aquele balde.")
    e.codigo(doc, BUSCAR_2, "buscar — passo 2")

    e.passo(doc, 3, "Se achar a chave → devolve o valor; senão → `None`.")
    e.codigo(doc, BUSCAR_3, "buscar — passo 3 (método completo)")
    e.corpo(
        doc,
        "Por que é rápido no caso médio? Porque a maioria dos baldes tem poucos itens — "
        "você quase não percorre a tabela toda.",
    )


def main() -> None:
    figuras.hash_baldes()
    doc = e.novo_documento()
    e.dica(
        doc,
        "Rascunho isolado da Aula 4. A apostila completa (`gerar_apostila.py`) *não* "
        "muda. Quando este texto estiver pronto, ele entra no gerador principal.",
    )
    e.sumario(doc, SUMARIO)
    escrever_aula4(doc, quebrar=True)
    gerado = e.salvar(doc, SAIDA)
    print(f"Word: {gerado}")
    from gerar_apostila import atualizar_campos_e_pdf

    try:
        pdf = atualizar_campos_e_pdf(gerado)
        if pdf:
            print(f"PDF:  {pdf}")
        else:
            print("Campos do sumário atualizados no Word.")
    except Exception as exc:
        print(f"Não deu para atualizar os números no Word automaticamente: {exc}")
        print("Feche o arquivo no Word e rode de novo, nesta pasta: python aula4.py")


if __name__ == "__main__":
    main()
