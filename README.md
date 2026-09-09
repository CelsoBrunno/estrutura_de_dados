# Estruturas de Dados

Apostila passo a passo do curso (8 aulas de 2h30). Público: quem já consegue rodar um `.py` e quer implementar as estruturas do zero — não só usar `list` e `dict`.

Professor: Celso Brunno Rocha Custódio de Campos.

## Pastas

- `apostila/` — gerador, aulas em Python e o Word para enviar ao aluno
- `apostila/imagens/` — diagramas (bits, memória, nós, pilha, hash, BST, grafo, heap)
- `exemplos/` — scripts na ordem das aulas

Para regenerar a apostila (atualiza o sumário interativo e, se o Word estiver instalado, os números de página e o PDF):

```
python -m pip install python-docx Pillow
cd apostila
python gerar_apostila.py
```

## Como estudar (você e o aluno)

Instale Python 3, abra esta pasta no VS Code.

```
python exemplos/01_array.py
python exemplos/01_mochila.py
python exemplos/02_lista.py
python exemplos/02_reprodutor.py
python exemplos/03_pilha_fila.py
python exemplos/03_callcenter.py
python exemplos/04_hash.py
python exemplos/05_bst.py
python exemplos/05_bst_pendente.py
python exemplos/05_bst_rebalance.py
python exemplos/05_bst_avl.py
python exemplos/06_grafo.py
python exemplos/07_heap.py
python exemplos/07_triagem.py
python exemplos/08_logistica.py
```

O alvo do projeto final é um simulador de logística (grafo + hash + heap). A Aula 8 cobra a defesa da escolha, não só a sintaxe.

## Calendário

1. Fundamentos de Memória, Big-O e Arrays
2. Listas Encadeadas
3. Pilhas e Filas (sobre a lista da Aula 2)
4. Tabelas Hash
5. Árvores Binárias e BST
6. Grafos e BFS
7. Heaps e briefing do projeto
8. Projeto final (PBL integrado)
