import sqlite3
import json

conexao = sqlite3.connect('novo_banco.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    marca TEXT NOT NULL,
    preco_custo REAL NOT NULL,
    preco_venda REAL NOT NULL
)''')

def salvar_json():
    """Salva todos os produtos do banco em JSON"""
    cursor.execute('SELECT nome_produto, categoria, marca, preco_custo, preco_venda FROM produtos')
    produtos = cursor.fetchall()
    produtos_lista = [
        {'nome_produto': p[0], 'categoria': p[1], 'marca': p[2], 'preco_custo': p[3], 'preco_venda': p[4]}
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
        cursor.execute('''INSERT INTO produtos (nome_produto, categoria, marca, preco_custo, preco_venda)
                          VALUES (?, ?, ?, ?, ?)''', (nome_produto, categoria, marca, preco_custo, preco_venda))
        conexao.commit()
        print(f"✓ Produto {nome_produto} inserido com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"✗ Erro: {e}")


def listar_produtos():
    """Lista todos os produtos"""
    cursor.execute('SELECT id, nome_produto, categoria, marca, preco_custo, preco_venda FROM produtos')
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
    
    cursor.execute('DELETE FROM produtos WHERE nome_produto = ?', (nome_produto,))
    if cursor.rowcount > 0:
        conexao.commit()
        print(f"✓ Produto {nome_produto} excluído com sucesso!")
    else:
        print(f"✗ Produto {nome_produto} não encontrado.")


def atualizar_produto():
    """Atualiza dados de um produto existente"""
    print("\n=== Atualizar Produto ===")
    nome_produto = input("Digite o nome do produto a atualizar: ")
    
    cursor.execute('SELECT id, nome_produto, categoria, marca, preco_custo, preco_venda FROM produtos WHERE nome_produto = ?', (nome_produto,))
    produto = cursor.fetchone()
    
    if not produto:
        print(f"✗ Produto {nome_produto} não encontrado.")
        return
    
    print(f"\nDados atuais:")
    print(f"  Nome Produto: {produto[1]}")
    print(f"  Categoria: {produto[2]}")
    print(f"  Marca: {produto[3]}")
    print(f"  Preço Custo: {produto[4]}")
    print(f"  Preço Venda: {produto[5]}")
    
    print("\nO que deseja atualizar?")
    print("1. Categoria")
    print("2. Marca")
    print("3. Preço Custo")
    print("4. Preço Venda")
    
    opcao = input("\nEscolha (1-4): ")
    
    try:
        if opcao == '1':
            nova_categoria = input("Nova categoria: ")
            cursor.execute('UPDATE produtos SET categoria = ? WHERE nome_produto = ?', (nova_categoria, nome_produto))
        elif opcao == '2':
            nova_marca = input("Nova marca: ")
            cursor.execute('UPDATE produtos SET marca = ? WHERE nome_produto = ?', (nova_marca, nome_produto))
        elif opcao == '3':
            novo_preco_custo = float(input("Novo preço de custo: "))
            cursor.execute('UPDATE produtos SET preco_custo = ? WHERE nome_produto = ?', (novo_preco_custo, nome_produto))
        elif opcao == '4':
            novo_preco_venda = float(input("Novo preço de venda: "))
            cursor.execute('UPDATE produtos SET preco_venda = ? WHERE nome_produto = ?', (novo_preco_venda, nome_produto))
        else:
            print("Opção inválida!")
            return
        
        conexao.commit()
        print("✓ Produto atualizado com sucesso!")
        
    except sqlite3.IntegrityError as e:
        print(f"✗ Erro: {e}")


# Menu principal
while True:
    print("\n=== MENU PRODUTOS ===")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Excluir produto")
    print("4. Atualizar produto")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção (1-5): ")
    
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        excluir_produto()
    elif opcao == '4':
        atualizar_produto()
    elif opcao == '5':
        break
    else:
        print("Opção inválida!")

# Salvar JSON antes de sair
salvar_json()

cursor.execute('SELECT COUNT(*) FROM produtos')
total = cursor.fetchone()[0]
print(f"\n✓ Total de produtos: {total}")
print("✓ Dados salvos em produtos.json")

conexao.close()
