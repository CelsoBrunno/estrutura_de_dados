# Aula 4 — Tabelas Hash (versão didática — rascunho)

> Rascunho de referência. **Já aplicado** em `aulas_1_4.py` + gabarito em `apendice.py`.
> Objetivo: explicar o “porquê” com calma e só depois chegar no código.

---

## 1. O problema (antes da técnica)

Com **array**, achar o elemento na posição `3` é instantâneo (`O(1)`):

```text
dados[3]  →  você já sabe o endereço
```

Na vida real a pergunta costuma ser outra:

```text
“Qual o nome do usuário u001?”
“Qual o preço do produto SKU-9981?”
```

Aqui a chave **não** é o índice. Se você só tiver uma lista, precisa **percorrer** até achar → `O(n)`.

**Pergunta da aula:** como transformar uma chave qualquer (texto, id, CPF) em um **índice** rápido?

---

## 2. Resposta em uma frase

> **Hash** = função que transforma a chave em um número; esse número vira o índice de um “balde” na tabela.

Depois disso, você só procura **dentro daquele balde**, não na tabela inteira.

---

## 3. Analogia do prédio

Imagine um prédio com **5 andares** (baldes 0 a 4).

1. Chega a moradora com a chave `"u001"`.
2. O porteiro (função de hash) calcula: “ela mora no andar 2”.
3. Você sobe **só** o andar 2 e procura o nome dela na listinha daquele andar.

Se duas pessoas caírem no mesmo andar, as duas ficam na listinha do andar — isso é **colisão**. Ainda assim você não vasculha o prédio inteiro.

---

## 4. O `dict` do Python já é isso

```python
pessoa = {"nome": "Bruna", "idade": "20"}
print(pessoa["nome"])  # rápido
```

O `dict` nativo **é** uma tabela hash (bem otimizada).

Nesta aula você **não usa o `dict`** para guardar o catálogo: recria a ideia na mão, para entender o que o Python faz por baixo.

| Ferramenta | Papel |
|---|---|
| `dict` do Python | hash pronto, uso diário |
| `TabelaHash` da aula | hash didático, para estudar o mecanismo |

---

## 5. Peças da tabela hash

1. **Tabela** — um array de tamanho fixo (ex.: 5 ou 8 posições).
2. **Balde** — cada posição é uma listinha (vazia no início).
3. **Função de hash** — transforma a chave em inteiro.
4. **Índice** — `hash(chave) % tamanho` (garante índice entre `0` e `tamanho - 1`).
5. **Par** — dentro do balde guardamos `[chave, valor]`.

Esquema:

```text
tamanho = 5

baldes:
  [0] []
  [1] []
  [2] [ ["u001", "João"], ["outra", "..."] ]   ← colisão
  [3] [ ["u002", "Maria"] ]
  [4] []
```

Fórmula usada no curso:

```text
indice = (soma dos códigos dos caracteres da chave) % tamanho
```

Em Python (versão didática):

```python
def _hash(self, chave):
    return sum(ord(c) for c in str(chave)) % self.tamanho
```

`ord("A")` devolve o código numérico do caractere. Somamos todos e tiramos o resto da divisão pelo tamanho.

> Observação honesta: essa função é **só para aprender**. Hash real (do `dict`) é mais sofisticada. O que importa agora é o **fluxo**: chave → número → balde → buscar/atualizar.

---

## 6. Inserir e buscar (fluxo mental)

### Inserir `"u001" → "João"`

1. Calcular `indice = _hash("u001")`.
2. Ir ao `baldes[indice]`.
3. Se a chave **já existe** nesse balde → **atualiza** o valor (não duplica).
4. Se não existe → **append** `[chave, valor]` na listinha.

### Buscar `"u001"`

1. Calcular o **mesmo** índice.
2. Percorrer **só** aquele balde.
3. Se achar a chave → devolve o valor.
4. Se não achar → `None`.

Por que é rápido no caso médio? Porque a maioria dos baldes tem poucos itens. Você quase não percorre a tabela toda.

---

## 7. Colisão — o ponto que mais confunde

**Colisão** = duas chaves **diferentes** geram o **mesmo índice**.

Isso **não é erro**. É esperado.

Tratamento desta aula: **encadeamento (chaining)**  
→ cada balde é uma listinha; as chaves colidentes ficam juntas no mesmo balde.

Consequência de Big-O:

| Situação | Busca |
|---|---|
| Chaves bem espalhadas, tabela folgada | média ≈ `O(1)` |
| Quase tudo no mesmo balde | piora para `O(n)` |

Por isso o **tamanho da tabela importa**. Tabela pequena demais → mais colisões → mais lento.

---

## 8. Comparação rápida (para não misturar com as outras aulas)

| Estrutura | Força | Fraqueza típica |
|---|---|---|
| Lista encadeada | inserir no início fácil | busca `O(n)` |
| Array por índice | `O(1)` se souber o índice | índice ≠ CPF / id |
| **Hash** | busca por chave ≈ `O(1)` médio | não mantém ordem; colisões |
| BST (Aula 5) | mantém ordem + busca `O(log n)` | mais complexa; degenera se mal usada |

No projeto final (logística):

- **Hash** → `id_pacote → dados do pacote`
- **Heap** → ordem de prioridade
- **Grafo** → rota entre pontos

Hash acha a ficha do pacote; não decide quem sai primeiro (isso é heap).

---

## 9. Exercício “na mão” (sem digitar código ainda)

Use tabela de tamanho **5** e a função do curso:

```text
indice = sum(ord(c) for c in chave) % 5
```

Códigos úteis (só o que você precisa):

| Char | `ord` |
|---|---|
| `u` | 117 |
| `0` | 48 |
| `1` | 49 |
| `2` | 50 |
| `a` | 97 |
| `b` | 98 |

### Parte A — calcular índices

Calcule o índice de cada chave:

1. `"u001"`
2. `"u002"`
3. `"ab"`
4. `"ba"`

Escreva assim:

```text
chave | soma dos ord | soma % 5 | balde
u001  | ?            | ?        | ?
...
```

### Parte B — desenhar a tabela

Insira nesta ordem (como no exemplo da aula):

1. `"u001" → "João"`
2. `"u002" → "Maria"`

Desenhe os 5 baldes e diga o que tem em cada um.

### Parte C — forçar colisão

Encontre **duas chaves diferentes** que caiam no **mesmo balde** (mesmo `soma % 5`).

Sugestão de caminho:

- Comece com `"ab"` e `"ba"` — elas têm os **mesmos** caracteres, então a **soma** é igual → colidem de propósito com esta função didática.
- Ou invente outra chave cuja soma dê o mesmo resto que `"u001"`.

Depois desenhe de novo o balde que ficou com **dois** pares.

### Parte D — busca mental

Responda sem código:

1. Para buscar `"u001"`, quantos baldes você precisa abrir?
2. Se o balde tiver 2 pares, o que você compara para achar o valor certo?
3. Se a tabela tivesse tamanho `1`, o que aconteceria com todas as inserções?

---

## 10. Gabarito (olhe só depois de tentar)

### Parte A

```text
"u001": ord('u')+ord('0')+ord('0')+ord('1') = 117+48+48+49 = 262
262 % 5 = 2  → balde 2

"u002": 117+48+48+50 = 263
263 % 5 = 3  → balde 3

"ab": 97+98 = 195
195 % 5 = 0  → balde 0

"ba": 98+97 = 195
195 % 5 = 0  → balde 0  (colide com "ab")
```

### Parte B (depois de u001 e u002)

```text
[0] []
[1] []
[2] [["u001", "João"]]
[3] [["u002", "Maria"]]
[4] []
```

### Parte C (exemplo com ab/ba)

```text
[0] [["ab", ...], ["ba", ...]]   ← colisão
[1] []
[2] [["u001", "João"]]
[3] [["u002", "Maria"]]
[4] []
```

### Parte D

1. **Um** balde (o do índice calculado).
2. Compara a **chave** de cada par (`par[0]`), não o valor.
3. Tudo cai no balde `0` → vira uma lista só → busca `O(n)`.

---

## 11. Checkpoint (o que você precisa saber falar em voz alta)

1. Por que hash existe, se já temos lista?
2. O que significa `hash(chave) % tamanho`?
3. O que é colisão e como o encadeamento resolve?
4. Por que o tempo médio é `O(1)`, e quando isso falha?
5. Em uma frase: diferença entre `dict` nativo e a `TabelaHash` da aula.

---

## 12. Prática no computador (depois do exercício na mão)

Arquivo: `exemplos/04_hash.py`

```bash
python exemplos/04_hash.py
```

Desafio extra:

1. Mude o tamanho para `5` e imprima `catalogo.baldes` após cada inserção.
2. Insira duas chaves que colidem e mostre os dois pares no mesmo balde.
3. Explique em voz alta o que `_hash`, `inserir` e `buscar` fazem — sem olhar o código.

---

## Notas para a implementação futura na apostila

- Manter o tom da apostila (objetivo, dica, prática, checkpoint).
- Incluir a analogia do prédio + tabela “na mão” + gabarito em apêndice ou caixa “confira depois”.
- Não alongar demais: esta versão cabe em ~2–3 páginas se compactada no Word.
- Código live coding continua sendo o `04_hash.py` (sem mudar a API da classe).
