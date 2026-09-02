"""Capa, sumário e capítulos de apoio."""

import estilo as e


def escrever_capa(doc):
    e.capa(doc)
    e.caixa(
        doc,
        "Como esta apostila funciona",
        "Você não pula para o simulador pronto. Em cada aula faz uma estrutura "
        "simples, lê o que aquilo significa e só então volta e edita. O projeto "
        "final nasce assim: array, lista, pilha, fila, hash, árvore, grafo e heap.",
        e.FILL_DICA,
    )
    e.caixa(
        doc,
        "Uso desta apostila",
        "© 2026 Celso Brunno Rocha Custódio de Campos. Material de uso didático. "
        "É vedada a reprodução, distribuição ou comercialização sem autorização do autor. "
        "O aluno pode usar o conteúdo para estudar e montar o projeto do curso.",
        e.FILL_ATENCAO,
    )


def escrever_sumario(doc):
    e.quebra(doc)
    p = doc.add_paragraph()
    e.run_txt(p, "Sumário", "Trebuchet MS", 22, True, e.NAVY)
    p2 = doc.add_paragraph()
    e.run_txt(p2, "Clique no título para ir à seção.", "Calibri", 12, False, e.CINZA)

    entradas = [
        (None, "Antes de começar", e.slug("Antes de começar"), 0),
        (None, "O que você vai construir", e.slug("O que você vai construir"), 1),
        (None, "Ferramentas", e.slug("Ferramentas"), 1),
        (None, "Calendário (igual ao site)", e.slug("Calendário (igual ao site)"), 1),
        ("INSTALAÇÃO", "fazer em casa (não entra na aula)", e.slug("fazer em casa (não entra na aula)"), 0),
        (None, "Python 3", e.slug("Python 3"), 1),
        (None, "VS Code", e.slug("VS Code"), 1),
        (None, "Conferir se está pronto", e.slug("Conferir se está pronto"), 1),
        (None, "Se deu erro, faça isto", e.slug("Se deu erro, faça isto"), 0),
        (None, "Boas práticas de programação", e.slug("Boas práticas de programação"), 0),
        ("AULA 1", "Fundamentos de Memória, Big-O e Arrays", e.slug("AULA 1"), 0),
        ("AULA 2", "Listas Encadeadas (Linked Lists)", e.slug("AULA 2"), 0),
        ("AULA 3", "Pilhas (Stacks) e Filas (Queues)", e.slug("AULA 3"), 0),
        ("AULA 4", "Tabelas Hash (Dicionários/Mapas)", e.slug("AULA 4"), 0),
        ("AULA 5", "Árvores Binárias e Árvores de Busca (BST)", e.slug("AULA 5"), 0),
        ("AULA 6", "Grafos e Algoritmos de Travessia", e.slug("AULA 6"), 0),
        ("AULA 7", "Heaps e preparação para o projeto", e.slug("AULA 7"), 0),
        ("AULA 8", "Projeto Final (PBL Integrado)", e.slug("AULA 8"), 0),
        ("APÊNDICE", "Código de referência", e.slug("Código de referência"), 0),
    ]
    for rotulo, titulo, ancora, nivel in entradas:
        e.linha_sumario(doc, rotulo, titulo, ancora, nivel)


def escrever_preambulo(doc):
    e.quebra(doc)
    e.h_titulo(doc, "Antes de começar", e.slug("Antes de começar"))
    e.corpo(
        doc,
        "Esta apostila acompanha o curso Estruturas de Dados. Cada aula tem 2h30. "
        "Você lê a explicação, copia o código com o professor e faz a prática no fim.",
    )
    e.corpo(
        doc,
        "Usamos o VS Code do primeiro ao último encontro. A instalação é em casa — "
        "não consome tempo de aula. O projeto do curso é um simulador de logística: "
        "cada estrutura vira uma peça, e a Aula 8 junta o sistema.",
    )

    e.h_secao(doc, "O que você vai construir")
    e.corpo(
        doc,
        "Não é um script copiado da internet: você constrói em camadas. Uma peça por vez, "
        "conferida no checkpoint do fim da aula.",
    )
    e.bullets(
        doc,
        [
            "Aulas 1 e 2 — memória contígua (array) e memória ligada (lista encadeada).",
            "Aulas 3 a 5 — regras de acesso (pilha/fila), busca por chave (hash) e ordem (BST).",
            "Aulas 6 e 7 — relações (grafo + BFS) e prioridade (heap).",
            "Aula 8 — simulador de logística, README e apresentação.",
        ],
    )
    e.dica(
        doc,
        "Não tente decorar. Digite o código. Se der erro, leia a mensagem em vermelho — "
        "ela quase sempre aponta a linha.",
    )
    e.atencao(
        doc,
        "Neste curso a `list` e o `dict` nativos do Python existem, mas não são o ponto. "
        "Você implementa a estrutura do zero para entender o custo. Usar `lista.append` "
        "sem saber o que acontece na memória é nota baixa.",
    )

    e.h_secao(doc, "Ferramentas")
    e.corpo(
        doc,
        "Python 3 e VS Code. O passo a passo está no capítulo Instalação — fazer em casa. "
        "Se a tela falhar, use Se deu erro, faça isto.",
    )
    e.corpo(
        doc,
        "Não é um curso de algoritmo do zero. Antes da Aula 1 você precisa conseguir: "
        "criar um arquivo `.py`, usar `print`, `if` e `for`, e escrever uma classe simples. "
        "Lista e dicionário nativos aparecem só como contraste com a estrutura real.",
    )

    e.h_secao(doc, "Calendário (igual ao site)")
    e.bullets(
        doc,
        [
            "Aula 1 — Fundamentos de Memória, Big-O e Arrays",
            "Aula 2 — Listas Encadeadas (Linked Lists)",
            "Aula 3 — Pilhas (Stacks) e Filas (Queues)",
            "Aula 4 — Tabelas Hash (Dicionários/Mapas)",
            "Aula 5 — Árvores Binárias e Árvores de Busca (BST)",
            "Aula 6 — Grafos e Algoritmos de Travessia",
            "Aula 7 — Estruturas avançadas (Heaps) e preparação para o projeto",
            "Aula 8 — Projeto Final (PBL Integrado)",
        ],
    )

    e.quebra(doc)
    e.h_rotulo(doc, "INSTALAÇÃO")
    e.h_titulo(doc, "fazer em casa (não entra na aula)", e.slug("fazer em casa (não entra na aula)"))
    e.atencao(
        doc,
        "Este capítulo não é aula. Nas 8 aulas o professor considera Python e VS Code "
        "já instalados. Use estas páginas em casa, antes do curso ou se o computador for novo.",
    )

    e.h_secao(doc, "Python 3")
    e.corpo(doc, "Passo 1. Abra python.org e baixe o instalador do Python 3.")
    e.corpo(doc, "Passo 2. No Windows, marque Add python.exe to PATH antes de clicar em Install Now.")
    e.corpo(doc, "Passo 3. Termine a instalação. Depois abra o Prompt e digite `python --version`. Deve aparecer 3.x.")

    e.h_secao(doc, "VS Code")
    e.corpo(doc, "Passo 1. Baixe em code.visualstudio.com e instale.")
    e.corpo(doc, "Passo 2. Abra o VS Code → ícone de extensões → instale a extensão Python (Microsoft).")
    e.corpo(
        doc,
        "Passo 3. File → Open Folder na pasta do projeto (a pasta que contém `exemplos/`). "
        "Abra um `.py` e rode no terminal: `python exemplos/01_array.py`.",
    )
    e.dica(
        doc,
        "O terminal precisa estar na pasta do projeto. Se aparecer `FileNotFoundError`, "
        "você rodou de outra pasta. No VS Code: Terminal → New Terminal (ele abre na pasta que você abriu).",
    )

    e.h_secao(doc, "Conferir se está pronto")
    e.corpo(doc, "Passo 1. `python --version` — precisa ser 3.x")
    e.corpo(doc, "Passo 2. `python exemplos/01_array.py` — precisa mostrar o estado da memória e, no fim, um erro de capacidade.")

    e.quebra(doc)
    e.h_titulo(doc, "Se deu erro, faça isto", e.slug("Se deu erro, faça isto"))
    e.corpo(doc, "Leia a última linha da mensagem em vermelho. Ache o sintoma abaixo e faça o X.")

    e.h_secao(doc, "Python não encontrado")
    e.corpo(
        doc,
        "Sintoma: `python is not recognized`, comando não encontrado ou o VS Code pede para "
        "escolher um interpretador e a lista vem vazia.",
    )
    e.bullets(
        doc,
        [
            "O Python não está instalado, ou foi instalado sem marcar Add python.exe to PATH.",
            "Feche o VS Code, instale de novo pelo capítulo de Instalação e reabra o programa.",
            "No VS Code: Ctrl+Shift+P → Python: Select Interpreter → escolha o Python 3.",
            "Teste fora do editor: abra o Prompt e digite `python --version`.",
        ],
    )

    e.h_secao(doc, "IndentationError")
    e.corpo(
        doc,
        "Sintoma: `IndentationError: expected an indented block`. O Python usa os espaços "
        "da esquerda para saber o que está dentro do `if`, `for` ou `def`.",
    )
    e.bullets(
        doc,
        [
            "Tudo que pertence ao if/for/def deve ficar 4 espaços mais à direita.",
            "Não misture Tab com espaço. No VS Code use só espaço (já vem assim).",
            "Se copiou código do WhatsApp, cole no editor e realinhe as linhas.",
            "A linha logo abaixo de `:` sempre precisa estar mais para dentro.",
        ],
    )

    e.h_secao(doc, "Arquivo na pasta errada")
    e.corpo(doc, "Sintoma: `FileNotFoundError` ao rodar `python exemplos/01_array.py`.")
    e.bullets(
        doc,
        [
            "O terminal tem que estar na pasta do projeto (aquela que contém `exemplos/`).",
            "No VS Code: File → Open Folder nessa pasta, depois Terminal → New Terminal.",
            "Não rode o arquivo de dentro da pasta `Downloads` se o projeto está em outro lugar.",
        ],
    )

    e.h_secao(doc, "NoneType e ponteiro")
    e.corpo(
        doc,
        "Sintoma: `'NoneType' object has no attribute 'proximo'` (ou `dado`, `anterior`). "
        "Você andou para além do último nó.",
    )
    e.bullets(
        doc,
        [
            "Antes de usar `atual.proximo`, teste `if atual is not None`.",
            "Lista vazia: a cabeça (`cabeca`) é `None`. Não chame método nela.",
            "Esse erro é o equivalente ao NullPointerException de outras linguagens.",
        ],
    )

    e.quebra(doc)
    e.h_titulo(doc, "Boas práticas de programação", e.slug("Boas práticas de programação"))
    e.corpo(
        doc,
        "Código não é só para o computador. Daqui a uma semana você vai reler o que escreveu hoje. "
        "O professor também. Por isso esta apostila cobra hábito, não só o programa que “funciona”.",
    )

    e.h_secao(doc, "Nomes que explicam")
    e.corpo(
        doc,
        "Use snake_case: `inserir_no_inicio`, `faixa_atual`, `tabela_hash`. Função começa com verbo. "
        "Evite `x`, `temp`, `coisa`, `l2`.",
    )
    e.codigo(
        doc,
        "# ruim\nn = n.p\n\n# bom\natual = atual.proximo",
        "Nomes",
    )

    e.h_secao(doc, "Indentação e uma ideia por vez")
    e.corpo(doc, "Python usa 4 espaços. Uma linha, uma ideia. Não esprema inserção, ponteiro e print na mesma linha.")

    e.h_secao(doc, "Funções curtas")
    e.corpo(
        doc,
        "Cada operação da estrutura faz uma coisa: inserir, remover, buscar, exibir. "
        "O `main` só demonstra. Isso vale da Aula 1 até o projeto.",
    )

    e.h_secao(doc, "Não se repita")
    e.corpo(
        doc,
        "Copiar o mesmo `while atual is not None` em quatro métodos é armadilha. "
        "Quando a lista muda, você corrige um e esquece os outros.",
    )

    e.h_secao(doc, "Comente o porquê, não o óbvio")
    e.codigo(
        doc,
        "# ruim\nself.topo = novo  # atribui topo\n\n"
        "# bom\n# o novo nó passa a ser o topo: LIFO só mexe nesta ponta\nself.topo = novo",
        "Comentários",
    )

    e.h_secao(doc, "Não copie sem entender")
    e.atencao(
        doc,
        "Colar uma BST da internet sem saber apontar a regra esquerda/direita é nota baixa. "
        "Se não consegue explicar em voz alta por que escolheu hash em vez de árvore, "
        "ainda não é seu código.",
    )
    e.dica(
        doc,
        "No projeto, o README pede exatamente isso: onde está cada estrutura. "
        "Quem escreveu com clareza preenche o README em dois minutos.",
    )

    e.h_secao(doc, "Checklist rápido (todas as aulas)")
    e.bullets(
        doc,
        [
            "Nomes em português ou inglês, mas consistentes.",
            "Arquivo `.py` salvo; terminal na pasta do projeto.",
            "Erro em vermelho: leia a última linha da mensagem primeiro.",
            "Antes de apresentar: rode de novo do zero. O que não roda, não entrega.",
        ],
    )
