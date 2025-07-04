# 🧩 Desafio 1: Inventário de uma Loja Mágica

## Descrição

Uma loja de itens mágicos está atualizando seu sistema de inventário. Cada item tem um nome, uma quantidade em estoque e um preço por unidade. Os dados são armazenados como uma lista de tuplas, onde cada tupla representa um item no formato:
`(nome_do_item: str, quantidade: int, preco: float)`.

Você deverá escrever um programa que:

* Construa essa lista a partir de dados definidos no código;
* Crie um dicionário onde a **chave é o nome do item** e o **valor é o total em reais que o estoque desse item representa**;
* Imprima os **3 itens mais valiosos do estoque**, do mais caro para o mais barato.

## Condições

* A lista inicial deve conter **ao menos 8 itens distintos**.
* Use **tuplas para armazenar os dados originais** e **dicionários para calcular valores totais por item**.
* Você **não pode usar bibliotecas externas**.
* O programa deve imprimir a saída no seguinte formato:

  ```
  Top 3 Itens mais valiosos:
  1. Poção de Cura – R$450.00
  2. Elixir de Invisibilidade – R$390.00
  3. Varinha de Carvalho – R$250.00
  ```

---

# 🧩 Desafio 2: Analisador de Notas de Alunos

## Descrição

Você recebeu uma lista de alunos e suas notas em uma disciplina. Cada entrada é uma tupla com o nome do aluno e uma lista com as notas dele. Exemplo:

```python
("Joana", [7.5, 8.0, 9.0])
```

Seu programa deverá:

* Calcular a **média individual** de cada aluno;
* Armazenar os resultados num dicionário no formato:

  ```python
  {"Joana": 8.17, "Carlos": 6.33, ...}
  ```
* Ao final, imprimir:

  1. O nome do aluno com **maior média**
  2. O nome do aluno com **menor média**
  3. A **média geral da turma**

## Condições

* A lista inicial deve conter **pelo menos 6 alunos**, cada um com **3 ou mais notas**.
* Não use bibliotecas externas (como NumPy ou pandas).
* Todas as médias devem ser arredondadas com **2 casas decimais**.
* Utilize **dicionários e tuplas** de maneira clara.

---

# 🧩 Desafio 3: Estatísticas de Compras

## Descrição

Você está analisando dados de compras feitas por usuários de um app. Os dados estão armazenados como uma **lista de dicionários**, onde cada dicionário representa uma compra:

```python
{
  "usuario": "ana123",
  "valor": 89.90,
  "itens": ["caderno", "caneta", "borracha"]
}
```

Seu programa deverá:

1. Calcular o **total gasto por cada usuário**.
2. Identificar **quais usuários compraram mais de 5 itens no total** (somando os itens de todas as compras dele).
3. Listar os **3 itens mais comprados no geral**, considerando todas as compras.

## Condições

* A lista de compras deve conter **pelo menos 10 entradas** com **usuários variados**.
* O programa deve utilizar **listas, dicionários e tuplas** com propósito bem definido.
* O programa deve exibir os resultados em três seções bem delimitadas:

  ```
  Total por usuário:
  - ana123: R$210.50
  - joaozinho: R$89.90
  ...

  Usuários com mais de 5 itens:
  - ana123
  - felipe22

  Top 3 Itens:
  1. caderno – 6x
  2. caneta – 5x
  3. régua – 4x
  ```

---

