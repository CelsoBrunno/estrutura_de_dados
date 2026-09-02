"""Capa, sumário e capítulos de apoio."""

import estilo as e


def escrever_capa(doc):
    e.capa(doc)


def escrever_preambulo(doc):
    e.h1(doc, "Antes de começar")
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
    e.h1(doc, e.TITULO_INSTALACAO)
    e.atencao(
        doc,
        "Este capítulo *não* é aula. Nas 8 aulas o professor considera Python e VS Code "
        "já instalados. Use estas páginas em casa, antes do curso ou se o computador for novo.",
    )

    e.h_secao(doc, "Python 3")
    e.passo(doc, 1, "Abra python.org e baixe o instalador do Python 3.")
    e.passo(doc, 2, "No Windows, marque *Add python.exe to PATH* antes de clicar em Install Now.")
    e.passo(
        doc,
        3,
        "Termine a instalação. Depois abra o Prompt e digite `python --version`. Deve aparecer 3.x.",
    )

    e.h_secao(doc, "VS Code")
    e.passo(doc, 1, "Baixe em code.visualstudio.com e instale.")
    e.passo(doc, 2, "Abra o VS Code → ícone de extensões → instale a extensão *Python* (Microsoft).")
    e.passo(
        doc,
        3,
        "File → Open Folder na pasta do projeto (a pasta que contém `exemplos/`). "
        "Abra um `.py` e rode no terminal: `python exemplos/01_array.py`.",
    )
    e.dica(
        doc,
        "O terminal precisa estar *na pasta do projeto*. Se aparecer `FileNotFoundError`, "
        "você rodou de outra pasta. No VS Code: Terminal → New Terminal (ele abre na pasta que você abriu).",
    )

    e.h_secao(doc, "Conferir se está pronto")
    e.passo(doc, 1, "`python --version` — precisa ser 3.x")
    e.passo(
        doc,
        2,
        "`python exemplos/01_array.py` — precisa mostrar o estado da memória e, no fim, um erro de capacidade.",
    )

    e.quebra(doc)
    e.h1(doc, e.TITULO_ERROS)
    e.corpo(doc, "Leia a *última* linha da mensagem em vermelho. Ache o sintoma abaixo e faça o X.")

    e.h_secao(doc, "Python não encontrado")
    e.corpo(
        doc,
        "Sintoma: `python is not recognized`, comando não encontrado ou o VS Code pede para "
        "escolher um interpretador e a lista vem vazia.",
    )
    e.bullets(
        doc,
        [
            "O Python não está instalado, ou foi instalado *sem* marcar Add python.exe to PATH.",
            "Feche o VS Code, instale de novo pelo capítulo de Instalação e *reabra* o programa.",
            "No VS Code: Ctrl+Shift+P → *Python: Select Interpreter* → escolha o Python 3.",
            "Teste fora do editor: abra o Prompt e digite `python --version`.",
        ],
    )
    par = doc.add_paragraph()
    r = par.add_run("Passo a passo da instalação: ")
    e._rpr(r, e.BODY, 11, False, e.TEXTO)
    e.frase_com_pagina(par, e.TITULO_INSTALACAO, "Instalação")

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
    e.h1(doc, "Boas práticas de programação")
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
