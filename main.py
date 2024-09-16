import psycopg2
from psycopg2 import sql
from datetime import datetime

# Conectando ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="gestao",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

# Função para inserir uma nova categoria
def inserir_categoria(nome):
    with conn.cursor() as cur:
        query = sql.SQL("INSERT INTO categorias (nome) VALUES (%s)")
        cur.execute(query, (nome,))
        conn.commit()
        print(f"Categoria '{nome}' inserida com sucesso!")

# Função para inserir um novo produto
def inserir_produto(nome, preco, categoria_id):
    with conn.cursor() as cur:
        query = sql.SQL("INSERT INTO produtos (nome, preco, categoria_id) VALUES (%s, %s, %s)")
        cur.execute(query, (nome, preco, categoria_id))
        conn.commit()
        print(f"Produto '{nome}' inserido com sucesso!")

# Função para inserir uma nova compra
def inserir_compra(total):
    with conn.cursor() as cur:
        query = sql.SQL("INSERT INTO compras (total) VALUES (%s) RETURNING id")
        cur.execute(query, (total,))
        compra_id = cur.fetchone()[0]
        conn.commit()
        print(f"Compra inserida com sucesso! ID: {compra_id}")
        return compra_id

# Função para inserir um item de compra
def inserir_item_compra(compra_id, produto_id, quantidade, preco_unitario):
    with conn.cursor() as cur:
        query = sql.SQL("INSERT INTO itens_compra (compra_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)")
        cur.execute(query, (compra_id, produto_id, quantidade, preco_unitario))
        conn.commit()
        print(f"Item de compra inserido com sucesso!")

# Função para listar todas as categorias
def listar_categorias():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM categorias")
        resultados = cur.fetchall()
        for row in resultados:
            print(f"ID: {row[0]}, Nome: {row[1]}")

# Função para listar todos os produtos
def listar_produtos():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM produtos")
        resultados = cur.fetchall()
        for row in resultados:
            print(f"ID: {row[0]}, Nome: {row[1]}, Preço: {row[2]}, Categoria ID: {row[3]}, Data Inserção: {row[4]}")

# Função para listar todas as compras
def listar_compras():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM compras")
        resultados = cur.fetchall()
        for row in resultados:
            print(f"ID: {row[0]}, Data: {row[1]}, Total: {row[2]}")

# Função para listar todos os itens de compra
def listar_itens_compra():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM itens_compra")
        resultados = cur.fetchall()
        for row in resultados:
            print(f"ID: {row[0]}, Compra ID: {row[1]}, Produto ID: {row[2]}, Quantidade: {row[3]}, Preço Unitário: {row[4]}")

# Exemplo de uso das funções
if __name__ == "__main__":
    # Inserir categorias
    inserir_categoria("Alimentos")
    inserir_categoria("Eletrônicos")

    # Inserir produtos
    inserir_produto("Arroz", 20.50, 1)
    inserir_produto("TV", 1200.00, 2)

    # Inserir uma nova compra
    compra_id = inserir_compra(1220.50)

    # Inserir itens de compra
    inserir_item_compra(compra_id, 1, 2, 20.50)  # 2 pacotes de arroz
    inserir_item_compra(compra_id, 2, 1, 1200.00)  # 1 TV

    # Listar todos os dados
    print("Categorias:")
    listar_categorias()
    print("\nProdutos:")
    listar_produtos()
    print("\nCompras:")
    listar_compras()
    print("\nItens de Compra:")
    listar_itens_compra()
