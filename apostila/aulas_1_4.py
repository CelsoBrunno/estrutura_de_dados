import estilo as e

ARRAY = '''class ArrayEstatico:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho_atual = 0
        self.dados = [None] * capacidade

    def acessar(self, indice):
        if 0 <= indice < self.tamanho_atual:
            return self.dados[indice]
        raise IndexError("Índice fora dos limites.")

    def inserir_no_final(self, valor):
        if self.tamanho_atual < self.capacidade:
            self.dados[self.tamanho_atual] = valor
            self.tamanho_atual += 1
        else:
            raise OverflowError("Array cheio.")

    def exibir(self):
        print("Estado da memória:", self.dados)


lista = ArrayEstatico(5)
lista.inserir_no_final(10)
lista.inserir_no_final(20)
lista.inserir_no_final(30)
lista.exibir()
print("posição 1:", lista.acessar(1))
'''

MOCHILA = '''class MochilaRPG:
    def __init__(self, slots):
        self.slots = slots
        self.itens_guardados = 0
        self.inventario = [None] * slots

    def coletar_item(self, item):
        print(f"Tentando coletar: {item}...")
        if self.itens_guardados < self.slots:
            self.inventario[self.itens_guardados] = item
            self.itens_guardados += 1
            print(f"[Sucesso] {item} no slot {self.itens_guardados - 1}.")
        else:
            print(f"[Falha] Mochila cheia! Descarte algo para pegar {item}.")

    def abrir_mochila(self):
        print("--- Conteúdo da Mochila ---")
        for i in range(self.slots):
            status = self.inventario[i] or "[Vazio]"
            print(f"Slot {i}: {status}")


mochila = MochilaRPG(4)
for item in ("Poção de Cura", "Espada de Ferro", "Mapa Antigo", "Tocha"):
    mochila.coletar_item(item)
mochila.abrir_mochila()
mochila.coletar_item("Amuleto Mágico")
'''

LISTA = '''class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, dado):
        novo = No(dado)
        novo.proximo = self.cabeca
        self.cabeca = novo
        print(f"[{dado}] inserido no início.")

    def exibir(self):
        atual = self.cabeca
        partes = []
        while atual is not None:
            partes.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(partes) + " -> None")


lista = ListaEncadeada()
lista.inserir_no_inicio("Terceiro")
lista.inserir_no_inicio("Segundo")
lista.inserir_no_inicio("Primeiro")
lista.exibir()
'''

PLAYER = '''class Faixa:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None
        self.anterior = None


class ReprodutorStreaming:
    def __init__(self):
        self.faixa_atual = None

    def adicionar_na_fila(self, musica):
        nova = Faixa(musica)
        if self.faixa_atual is None:
            self.faixa_atual = nova
            print(f"Playlist iniciada: {musica}")
            return
        nova.anterior = self.faixa_atual
        nova.proximo = self.faixa_atual.proximo
        if self.faixa_atual.proximo:
            self.faixa_atual.proximo.anterior = nova
        self.faixa_atual.proximo = nova
        print(f"Faixa [{musica}] adicionada como próxima.")

    def proxima_faixa(self):
        if self.faixa_atual and self.faixa_atual.proximo:
            self.faixa_atual = self.faixa_atual.proximo
            print(f">> {self.faixa_atual.musica}")
        else:
            print(">> Fim da playlist.")

    def faixa_anterior(self):
        if self.faixa_atual and self.faixa_atual.anterior:
            self.faixa_atual = self.faixa_atual.anterior
            print(f"<< {self.faixa_atual.musica}")
        else:
            print("<< Início da playlist.")


player = ReprodutorStreaming()
player.adicionar_na_fila("Bohemian Rhapsody")
player.adicionar_na_fila("Stairway to Heaven")
player.adicionar_na_fila("Hotel California")
player.proxima_faixa()
player.proxima_faixa()
player.faixa_anterior()
'''

PILHA_FILA = '''class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, dado):
        novo = No(dado)
        novo.proximo = self.topo
        self.topo = novo

    def desempilhar(self):
        if self.topo is None:
            raise IndexError("Pilha vazia.")
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado

    def vazia(self):
        return self.topo is None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, dado):
        novo = No(dado)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def desenfileirar(self):
        if self.inicio is None:
            raise IndexError("Fila vazia.")
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return dado

    def vazia(self):
        return self.inicio is None
'''

CALLCENTER = '''from collections import deque


class CallCenter:
    def __init__(self):
        self.fila_espera = deque()      # Fila: quem chega
        self.historico_acoes = []       # Pilha: desfazer (Ctrl+Z)

    def novo_cliente(self, nome):
        self.fila_espera.append(nome)
        print(f"[Entrada] Cliente {nome} entrou na fila de espera.")

    def atender_proximo(self):
        if len(self.fila_espera) > 0:
            cliente_atendido = self.fila_espera.popleft()  # O(1)
            self.historico_acoes.append(cliente_atendido)
            print(f"[Atendimento] Atendendo cliente: {cliente_atendido}")
        else:
            print("[Atendimento] A fila de espera está vazia.")

    def desfazer_encerramento(self):
        if len(self.historico_acoes) > 0:
            cliente_recuperado = self.historico_acoes.pop()  # O(1)
            self.fila_espera.appendleft(cliente_recuperado)
            print(f"[Desfazer] Erro! {cliente_recuperado} voltou ao início da fila.")
        else:
            print("[Desfazer] Não há ações recentes para desfazer.")

    def mostrar_painel(self):
        print(f"\\nPainel - Fila atual: {list(self.fila_espera)}")
        print("-" * 30)


sistema = CallCenter()
sistema.novo_cliente("João")
sistema.novo_cliente("Maria")
sistema.novo_cliente("Carlos")
sistema.mostrar_painel()
sistema.atender_proximo()
sistema.atender_proximo()
sistema.mostrar_painel()
sistema.desfazer_encerramento()
sistema.mostrar_painel()
sistema.atender_proximo()
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


def escrever_aulas_1_4(doc):
    _aula1(doc)
    _aula2(doc)
    _aula3(doc)
    _aula4(doc)


def _aula1(doc):
    e.h_aula(doc, 1, "Fundamentos de Memória, Big-O e Arrays")
    e.objetivo(
        doc,
        "Entender alocação contígua na RAM, ler Big-O no pior caso e simular um array "
        "estático em Python — inclusive o erro de capacidade cheia.",
    )
    e.caixa(
        doc,
        "Para seguir, use o VS Code",
        "A instalação não entra no tempo de aula. Se ainda não tiver o programa, faça o "
        "passo a passo em Instalação. Se a tela falhar, vá para Se deu erro, faça isto.",
        e.FILL_DICA,
    )

    e.h_secao(doc, "Como a RAM guarda um array")
    e.corpo(
        doc,
        "A memória RAM é um armário com gavetas numeradas (endereços). Um array estático "
        "pede um bloco de gavetas vizinhas. Se você declara capacidade 5, o sistema reserva "
        "exatamente 5 espaços contíguos.",
    )
    e.corpo(
        doc,
        "Antes do array, o aluno precisa ver o tijolo: o bit. 2 bits são 4 combinações "
        "(lâmpada ligada/desligada). 32 bits de um `int` clássico têm teto; passar disso "
        "é overflow — em linguagens de tamanho fixo. O Python mascara isso; a estrutura de "
        "dados, não.",
    )
    e.figura(
        doc,
        "01_bits.png",
        "Dois bits: quatro combinações. Cada lâmpada acesa vale um 1.",
    )
    e.figura(
        doc,
        "01_faixas.png",
        "Faixas com e sem sinal. Na lousa, complete 8 e 16 bits com a turma antes de mostrar a tabela.",
        15.2,
    )
    e.figura(
        doc,
        "01_array_ram.png",
        "Cinco slots vizinhos. O bloco rosa já está ocupado: não dá para “empurrar” o 6 ali.",
    )
    e.corpo(
        doc,
        "Se precisar do 6º item, a próxima gaveta pode estar ocupada por outro programa. "
        "Aí o computador procura um bloco de 6, copia os 5 itens e adiciona o novo. "
        "Essa cópia é o custo: tempo linear, `O(n)`.",
    )
    e.figura(
        doc,
        "01_array_copia.png",
        "O append que parece O(1) às vezes copia a lista inteira. Por isso o “5 segundos / 6 segundos” da lousa.",
    )
    e.atencao(
        doc,
        "A `list` do Python (`[]`) é um array dinâmico escrito em C. Ela mascara o "
        "redimensionamento. Nesta aula você simula o array rígido para ver o limite.",
    )

    e.h_secao(doc, "Big-O em uma frase")
    e.corpo(
        doc,
        "Big-O descreve o pior caso quando a entrada cresce. Não é “segundos no seu PC”: "
        "é como o trabalho cresce.",
    )
    e.bullets(
        doc,
        [
            "`O(1)` — constante. Acesso por índice: `endereço_base + (índice * tamanho_do_dado)`.",
            "`O(n)` — linear. Inserir no meio exige empurrar os elementos seguintes.",
            "`O(n²)` — quadrático. Dois laços aninhados sobre a mesma coleção (aparece como contraste).",
        ],
    )
    e.figura(
        doc,
        "01_big_o.png",
        "O eixo horizontal é o tamanho da entrada; o vertical é o trabalho. O(1) é a reta baixa; O(n²) dispara.",
    )

    e.h_secao(doc, "Live coding: array estático")
    e.corpo(
        doc,
        "Crie `exemplos/01_array.py`. Force o `OverflowError`: os alunos precisam ver o erro "
        "para entender a rigidez da estrutura.",
    )
    e.codigo(doc, ARRAY, "exemplos/01_array.py")
    e.dica(
        doc,
        "Se `acessar` receber um índice dentro da capacidade mas além de `tamanho_atual`, "
        "o slot ainda é `None`. Distinguir “existe na memória” de “já foi preenchido” é o ponto da aula.",
    )
    e.boa_pratica(doc, "Sempre teste o limite: um array que nunca enche não ensina capacidade.")

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática A — Sistema de inventário restrito",
        "Vocês foram contratados para o inventário de um jogo clássico. O personagem tem "
        "uma mochila com exatamente 4 slots. Dá para adicionar, listar e recusar item extra "
        "sem travar o jogo.",
    )
    e.codigo(doc, MOCHILA, "exemplos/01_mochila.py")
    e.pratica(
        doc,
        "Prática B — Inserir no meio (discussão)",
        "No caderno (não precisa implementar agora): se a mochila tivesse que abrir o slot 0 "
        "para um item novo, quantos elementos andam? Isso é `O(n)`. Guarde essa resposta — "
        "é o gancho da Aula 2.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Explicar por que o acesso por índice é `O(1)` e a inserção no meio é `O(n)`.",
            "Rodar o array estático e provocar o estouro de capacidade.",
            "Dizer o que aconteceria se a mochila ganhasse um “upgrade” de slots usando só array estático.",
        ],
    )


def _aula2(doc):
    e.h_aula(doc, 2, "Listas Encadeadas (Linked Lists)")
    e.objetivo(
        doc,
        "Quebrar a contiguidade da RAM: montar nós com ponteiros, inserir no início em `O(1)` "
        "e navegar para frente e para trás numa lista dupla.",
    )
    e.corpo(
        doc,
        "Retome a pergunta da Aula 1: como aumentar a mochila sem um bloco contínuo novo?",
    )

    e.h_secao(doc, "Nós e ponteiros")
    e.corpo(
        doc,
        "A lista encadeada espalha os dados em qualquer gaveta livre. Para não se perder, "
        "cada nó guarda duas coisas: o dado e o endereço do próximo nó.",
    )
    e.bullets(
        doc,
        [
            "Simplesmente encadeada — mão única. Cada nó só conhece o próximo.",
            "Duplamente encadeada — mão dupla. Conhece o anterior e o próximo (gasta mais memória).",
        ],
    )
    e.figura(
        doc,
        "02_lista_simples.png",
        "HEAD aponta o primeiro nó; TAIL o último; o prox do último é None.",
    )
    e.figura(
        doc,
        "02_lista_dupla.png",
        "Seta verde = próximo. Seta vermelha = anterior. É o custo extra de memória da lista dupla.",
    )

    e.h_secao(doc, "Trade-off de Big-O")
    e.bullets(
        doc,
        [
            "Acesso ao k-ésimo item piora: vira `O(n)` — é preciso andar nó a nó.",
            "Inserção/remoção no início (com o ponteiro na mão) vira `O(1)`: só troca referências.",
        ],
    )

    e.h_secao(doc, "Live coding: lista simples")
    e.codigo(doc, LISTA, "exemplos/02_lista.py")
    e.dica(
        doc,
        "Inserir no início inverte a ordem de chegada. “Terceiro, Segundo, Primeiro” no código "
        "aparece como Primeiro → Segundo → Terceiro. Mostre isso na lousa.",
    )

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática — Reprodutor de mídia",
        "Playlist sem limite prévio de faixas, com botões Próximo e Anterior. Use lista "
        "duplamente encadeada. Cuidado com `None` nas pontas.",
    )
    e.figura(
        doc,
        "02_reprodutor.png",
        "A faixa atual (centro) conhece a anterior e a próxima — botões do player.",
    )
    e.codigo(doc, PLAYER, "exemplos/02_reprodutor.py")
    e.boa_pratica(
        doc,
        "Toda navegação testa `if self.faixa_atual and self.faixa_atual.proximo`. "
        "Sem isso, o NoneType aparece na hora da demo.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Desenhar três nós no papel e o ponteiro `cabeca`.",
            "Inserir no início de uma lista simples e exibir até `None`.",
            "Explicar por que o botão Anterior precisa do ponteiro `anterior`.",
        ],
    )


def _aula3(doc):
    e.h_aula(doc, 3, "Pilhas (Stacks) e Filas (Queues)")
    e.objetivo(
        doc,
        "Restringir o acesso: LIFO na pilha e FIFO na fila. Na live coding as duas nascem "
        "sobre nós; na prática (Call Center) usamos `deque` e `list`, ambos em `O(1)`.",
    )
    e.corpo(
        doc,
        "Nas Aulas 1 e 2 o tema era “onde a memória mora”. Agora o tema é a regra de negócio: "
        "de que ponta o dado entra e de que ponta sai.",
    )

    e.h_secao(doc, "Pilha — LIFO")
    e.corpo(
        doc,
        "Last In, First Out. Analogia: pilha de pratos. Só mexe no topo. Uso real: Ctrl+Z, "
        "botão Voltar do navegador, pilha de chamadas do Python.",
    )
    e.figura(
        doc,
        "03_pilha.png",
        "Pratos e nós: só o topo muda. Empilhar e desempilhar são O(1).",
    )

    e.h_secao(doc, "Fila — FIFO")
    e.corpo(
        doc,
        "First In, First Out. Analogia: fila de banco. Entra no fim, sai no início. "
        "Uso real: impressão, requisições de servidor, matchmaking de jogo.",
    )
    e.figura(
        doc,
        "03_fila.png",
        "Ana entra primeiro e sai primeiro. No slide da aula isso aparece como Head + deque; aqui a fila nasce nos nós.",
    )
    e.atencao(
        doc,
        "Usar `lista.pop(0)` numa `list` do Python para simular fila é `O(n)`: todos os "
        "itens andam para a esquerda (Aula 1). Por isso a fila da live coding tem ponteiro "
        "de início e de fim na lista encadeada. Na prática do Call Center, `collections.deque` "
        "resolve as duas pontas em `O(1)`; a `list` do histórico só empilha e desempilha no fim — também `O(1)`.",
    )

    e.h_secao(doc, "Live coding: pilha e fila sobre nós")
    e.codigo(doc, PILHA_FILA, "exemplos/03_pilha_fila.py")

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática — Call Center integrado",
        "Vocês foram contratados para o balcão de um Call Center. Clientes entram numa "
        "fila de espera e são atendidos na ordem de chegada. O atendente às vezes encerra "
        "o chamado sem querer: precisa de uma pilha de histórico para desfazer o último "
        "encerramento e devolver o cliente ao início da fila (não ao fim).",
    )
    e.figura(
        doc,
        "03_callcenter.png",
        "Fila = quem espera (FIFO). Pilha = histórico do atendente (LIFO). Desfazer usa appendleft.",
    )
    e.codigo(doc, CALLCENTER, "exemplos/03_callcenter.py")
    e.dica(
        doc,
        "Por que `appendleft` no desfazer, e não `append`? Se foi erro, a Maria não volta "
        "para o fim da fila atrás do Carlos: ela retoma a prioridade de quem já estava sendo atendido.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Dizer em uma frase a diferença LIFO / FIFO apontando a fila e a pilha do Call Center.",
            "Explicar por que `popleft` no `deque` é O(1) e `list.pop(0)` não é.",
            "Desfazer o encerramento da Maria e mostrar o painel com ela de volta na frente.",
        ],
    )


def _aula4(doc):
    e.h_aula(doc, 4, "Tabelas Hash (Dicionários/Mapas)")
    e.objetivo(
        doc,
        "Mapear chave → índice com uma função de hash, tratar colisão por encadeamento "
        "e buscar em tempo médio `O(1)` sem usar o `dict` nativo.",
    )
    e.corpo(
        doc,
        "Gancho da Aula 3: o gerente quer o cliente “Carlos” sem percorrer a fila inteira. "
        "Array é `O(1)` por índice, mas o índice não é o CPF. Hash transforma a chave em índice.",
    )

    e.h_secao(doc, "Função de hash e colisão")
    e.corpo(
        doc,
        "Uma função de hash devolve um inteiro. O índice na tabela é `hash(chave) % tamanho`. "
        "Duas chaves podem cair no mesmo balde: isso é colisão. Tratamos com uma listinha "
        "(chaining) dentro de cada posição — a lista da Aula 2 em miniatura.",
    )
    e.dica(
        doc,
        "Tempo médio `O(1)` assume tabela folgada e hash espalhada. Se todo mundo cai no "
        "mesmo balde, a busca vira `O(n)`. Por isso o tamanho da tabela importa.",
    )
    e.figura(
        doc,
        "04_hash.png",
        "Cada balde é uma listinha. Duas chaves no mesmo índice = colisão; as duas ficam no encadeamento.",
    )

    e.h_secao(doc, "Live coding: tabela com chaining")
    e.codigo(doc, HASH, "exemplos/04_hash.py")
    e.boa_pratica(
        doc,
        "Ao inserir, primeiro percorra o balde: se a chave já existe, atualize o valor. "
        "Senão a mesma chave aparece duas vezes e a busca pega a antiga.",
    )

    e.h_secao(doc, "Práticas da aula")
    e.pratica(
        doc,
        "Prática — Catálogo de usuários / cache",
        "Guarde id → nome (ou url → conteúdo). Busque por chave. Invente duas chaves que "
        "colidam no mesmo índice (mesmo `sum(ord) % tamanho`) e mostre os dois pares no balde.",
    )

    e.h_antes(doc)
    e.bullets(
        doc,
        [
            "Calcular na mão o índice de uma chave pequena.",
            "Inserir, buscar e explicar o que o encadeamento faz na colisão.",
            "Dizer quando hash ganha da lista e quando ainda precisa percorrer o balde.",
        ],
    )
