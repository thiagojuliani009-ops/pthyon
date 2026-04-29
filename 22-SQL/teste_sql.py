import sqlite3
import json

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Criar tabela (sem limpar para manter dados existentes)
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cidade TEXT,
    cpf TEXT UNIQUE NOT NULL
)''')

def salvar_json():
    """Salva todos os clientes do banco em JSON"""
    cursor.execute('SELECT nome, email, cidade, cpf FROM clientes')
    clientes = cursor.fetchall()
    clientes_lista = [
        {'nome': c[0], 'email': c[1], 'cidade': c[2], 'cpf': c[3]} 
        for c in clientes
    ]
    with open('clientes.json', 'w', encoding='utf-8') as f:
        json.dump(clientes_lista, f, indent=4, ensure_ascii=False)

def adicionar_cliente():
    """Adiciona um novo cliente"""
    print("\n=== Novo Cliente ===")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    cidade = input("Digite a cidade: ")
    cpf = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
    
    try:
        cursor.execute('''INSERT INTO clientes (nome, email, cidade, cpf)
                          VALUES (?, ?, ?, ?)''', (nome, email, cidade, cpf))
        conexao.commit()
        print(f"✓ Cliente {nome} inserido com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"✗ Erro: {e}")

def listar_clientes():
    """Lista todos os clientes"""
    cursor.execute('SELECT id, nome, email, cidade, cpf FROM clientes')
    clientes = cursor.fetchall()
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return
    print("\n=== Lista de Clientes ===")
    for c in clientes:
        print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]} | Cidade: {c[3]} | CPF: {c[4]}")

def excluir_cliente():
    """Exclui um cliente pelo nome"""
    print("\n=== Excluir Cliente ===")
    nome = input("Digite o nome do cliente a excluir: ")
    
    cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome,))
    if cursor.rowcount > 0:
        conexao.commit()
        print(f"✓ Cliente {nome} excluído com sucesso!")
    else:
        print(f"✗ Cliente {nome} não encontrado.")

# Menu principal
while True:
    print("\n=== MENU ===")
    print("1. Adicionar cliente")
    print("2. Listar clientes")
    print("3. Excluir cliente")
    print("4. Sair")
    
    opcao = input("\nEscolha uma opção (1-4): ")
    
    if opcao == '1':
        adicionar_cliente()
    elif opcao == '2':
        listar_clientes()
    elif opcao == '3':
        excluir_cliente()
    elif opcao == '4':
        break
    else:
        print("Opção inválida!")

# Salvar JSON antes de sair
salvar_json()

cursor.execute('SELECT COUNT(*) FROM clientes')
total = cursor.fetchone()[0]
print(f"\n✓ Total de clientes: {total}")
print("✓ Dados salvos em clientes.json")

conexao.close()

