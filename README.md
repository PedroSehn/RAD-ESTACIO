# Sistema de Gestão de Compras de Supermercado

Este é um sistema de gestão de compras de supermercado, desenvolvido em Python, que utiliza o banco de dados PostgreSQL para armazenar informações sobre categorias de produtos, produtos, compras e itens de compra. O sistema permite realizar operações básicas de inserção e listagem de dados.

## Estrutura do Banco de Dados

### Tabelas

No diretório do projeto, há dois arquivos `.txt` que ajudarão na configuração do banco de dados:

- **`geracao-tabelas.txt`**: Este arquivo contém os comandos SQL para criar as tabelas do banco de dados. Use o pgAdmin ou o terminal PostgreSQL para executar este arquivo.

  Para executar no pgAdmin:
  
  1. Vá até o menu de query.
  2. Copie e cole o conteúdo do arquivo `geracao-tabelas.txt`.
  3. Execute o script para criar as tabelas.

  As tabelas incluídas são:
  - `categorias`
  - `produtos`
  - `compras`
  - `itens_compra`

- **`populando-tabelas.txt`**: Este arquivo contém comandos SQL para inserir dados de exemplo nas tabelas criadas.

  Para popular o banco:
  
  1. Abra o menu de query no pgAdmin ou terminal.
  2. Copie e cole o conteúdo do arquivo `populando-tabelas.txt`.
  3. Execute o script para inserir os dados de exemplo.


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
