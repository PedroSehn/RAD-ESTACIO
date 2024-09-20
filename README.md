# Sistema de Gestão de Compras de Supermercado

Este é um sistema de gestão de compras de supermercado, desenvolvido em Python, que utiliza o banco de dados PostgreSQL para armazenar informações sobre categorias de produtos, produtos, compras e itens de compra. O sistema permite realizar operações básicas de inserção e listagem de dados.

## Estrutura do Banco de Dados

### Tabelas

O banco de dados **gestao** é composto pelas seguintes tabelas:

#### 1. **categorias**
Tabela que armazena as categorias dos produtos.

| Coluna | Tipo        | Descrição              |
|--------|-------------|------------------------|
| id     | SERIAL      | Chave primária          |
| nome   | VARCHAR(100)| Nome da categoria       |

#### 2. **produtos**
Tabela que armazena os produtos, seus preços, categorias e datas de inserção.

| Coluna         | Tipo         | Descrição                              |
|----------------|--------------|----------------------------------------|
| id             | SERIAL       | Chave primária                         |
| nome           | VARCHAR(100) | Nome do produto                        |
| preco          | DECIMAL(10,2)| Preço do produto                       |
| categoria_id   | INT          | Chave estrangeira (referencia `categorias`) |
| data_insercao  | DATE         | Data de inserção do produto            |

#### 3. **compras**
Tabela que armazena as compras realizadas no supermercado.

| Coluna | Tipo         | Descrição             |
|--------|--------------|-----------------------|
| id     | SERIAL       | Chave primária         |
| data   | DATE         | Data da compra         |
| total  | DECIMAL(10,2)| Valor total da compra  |

#### 4. **itens_compra**
Tabela que armazena os itens de uma compra, incluindo produto, quantidade e preço unitário.

| Coluna        | Tipo         | Descrição                              |
|---------------|--------------|----------------------------------------|
| id            | SERIAL       | Chave primária                         |
| compra_id     | INT          | Chave estrangeira (referencia `compras`) |
| produto_id    | INT          | Chave estrangeira (referencia `produtos`) |
| quantidade    | INT          | Quantidade do produto comprado         |
| preco_unitario| DECIMAL(10,2)| Preço unitário do produto              |

## Funcionalidades

As principais funcionalidades do sistema são:

1. **Inserção de Categorias**:
   - Função `inserir_categoria(nome)` para adicionar uma nova categoria à tabela `categorias`.

2. **Inserção de Produtos**:
   - Função `inserir_produto(nome, preco, categoria_id)` para adicionar um novo produto à tabela `produtos`.

3. **Inserção de Compras**:
   - Função `inserir_compra(total)` para registrar uma nova compra na tabela `compras`.

4. **Inserção de Itens de Compra**:
   - Função `inserir_item_compra(compra_id, produto_id, quantidade, preco_unitario)` para adicionar um item à tabela `itens_compra` vinculada a uma compra.

5. **Listagem de Categorias**:
   - Função `listar_categorias()` para listar todas as categorias cadastradas.

6. **Listagem de Produtos**:
   - Função `listar_produtos()` para listar todos os produtos cadastrados.

7. **Listagem de Compras**:
   - Função `listar_compras()` para listar todas as compras realizadas.

8. **Listagem de Itens de Compra**:
   - Função `listar_itens_compra()` para listar todos os itens de compra registrados.

## Configuração do Ambiente

### 1. Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [pgAdmin](https://www.pgadmin.org/download/) (opcional)
- Biblioteca `psycopg2` instalada no ambiente Python.

### 2. Instalando a Biblioteca `psycopg2`

Execute o seguinte comando no terminal para instalar a biblioteca:

```bash
pip install psycopg2
