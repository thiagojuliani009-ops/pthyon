import sqlite3
import json


conexao = sqlite3.connect('novo_banco.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome Produto TEXT NOT NULL,
    Categoria TEXT NOT NULL,
    Marca TEXT NOT NULL,
    Preco Custo REAL NOT NULL,
    Preco Venda REAL NOT NULL,
        
)''')

def salvar_json():
    """Salva todos os produtos do banco em JSON"""
    cursor.execute('SELECT Nome Produto, Categoria, Marca, Preco Custo, Preco Venda FROM produtos')
    produtos = cursor.fetchall()
    produtos_lista = [
        {'Nome Produto': p[0], 'Categoria': p[1], 'Marca': p[2], 'Preco Custo': p[3], 'Preco Venda': p[4]} 
        for p in produtos
    ]
    with open('produtos.json', 'w', encoding='utf-8') as f:
        json.dump(produtos_lista, f, indent=4, ensure_ascii=False)

def adicionar_produto():
    """Adiciona um novo produto"""
    print("\n=== Novo Produto ===")
    nome_produto = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria: ")
    marca = input("Digite a marca: ")
    preco_custo = float(input("Digite o preço de custo: "))
    preco_venda = float(input("Digite o preço de venda: "))
    
    try:
        cursor.execute('''INSERT INTO produtos (Nome Produto, Categoria, Marca, Preco Custo, Preco Venda)
                          VALUES (?, ?, ?, ?, ?)''', (nome_produto, categoria, marca, preco_custo, preco_venda))
        conexao.commit()
        print(f"✓ Produto {nome_produto} inserido com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"✗ Erro: {e}")
def listar_produtos():
    """Lista todos os produtos"""
    cursor.execute('SELECT id, Nome Produto, Categoria, Marca, Preco Custo, Preco Venda FROM produtos')
    produtos = cursor.fetchall()
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return
    print("\n=== Lista de Produtos ===")
    for p in produtos:
        print(f"ID: {p[0]} | Nome Produto: {p[1]} | Categoria: {p[2]} | Marca: {p[3]} | Preço Custo: {p[4]} | Preço Venda: {p[5]}")
def excluir_produto():
    """Exclui um produto pelo nome"""
    print("\n=== Excluir Produto ===")
    nome_produto = input("Digite o nome do produto a excluir: ")
    
    cursor.execute('DELETE FROM produtos WHERE Nome Produto = ?', (nome_produto,))
    if cursor.rowcount > 0:
        conexao.commit()
        print(f"✓ Produto {nome_produto} excluído com sucesso!")
    else:
        print(f"✗ Produto {nome_produto} não encontrado.")
def atualizar_produto():
    """Atualiza dados de um produto existente"""
    print("\n=== Atualizar Produto ===")
    nome_produto = input("Digite o nome do produto a atualizar: ")
    
    cursor.execute('SELECT id FROM produtos WHERE Nome Produto = ?', (nome_produto,))
    resultado = cursor.fetchone()
    if resultado:
        id_produto = resultado[0]
        nova_categoria = input("Digite a nova categoria: ")
        nova_marca = input("Digite a nova marca: ")
        novo_preco_custo = float(input("Digite o novo preço de custo: "))
        novo_preco_venda = float(input("Digite o novo preço de venda: "))
        
        cursor.execute('''UPDATE produtos 
                          SET Categoria = ?, Marca = ?, Preco Custo = ?, Preco Venda = ? 
                          WHERE id = ?''', (nova_categoria, nova_marca, novo_preco_custo, novo_preco_venda, id_produto))
        conexao.commit()
        print(f"✓ Produto {nome_produto} atualizado com sucesso!")
    else:
        print(f"✗ Produto {nome_produto} não encontrado.")

# Salvar JSON antes de sair
salvar_json()
conexao.commit()
conexao.close()
