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

def atualizar_cliente():
    """Atualiza dados de um cliente existente"""
    print("\n=== Atualizar Cliente ===")
    nome = input("Digite o nome do cliente a atualizar: ")
    
    cursor.execute('SELECT nome, email, cidade, cpf FROM clientes WHERE nome = ?', (nome,))
    cliente = cursor.fetchone()
    
    if not cliente:
        print(f"✗ Cliente {nome} não encontrado.")
        return
    
    print(f"\nDados atuais:")
    print(f"  Nome: {cliente[0]}")
    print(f"  Email: {cliente[1]}")
    print(f"  Cidade: {cliente[2]}")
    print(f"  CPF: {cliente[3]}")
    
    print("\nO que deseja atualizar?")
    print("1. Nome")
    print("2. Email")
    print("3. Cidade")
    print("4. CPF")
    print("5. Todos os dados")
    
    opcao = input("\nEscolha (1-5): ")
    
    try:
        if opcao == '1':
            novo_nome = input("Novo nome: ")
            cursor.execute('UPDATE clientes SET nome = ? WHERE nome = ?', (novo_nome, nome))
        elif opcao == '2':
            novo_email = input("Novo email: ")
            cursor.execute('UPDATE clientes SET email = ? WHERE nome = ?', (novo_email, nome))
        elif opcao == '3':
            nova_cidade = input("Nova cidade: ")
            cursor.execute('UPDATE clientes SET cidade = ? WHERE nome = ?', (nova_cidade, nome))
        elif opcao == '4':
            novo_cpf = input("Novo CPF: ")
            cursor.execute('UPDATE clientes SET cpf = ? WHERE nome = ?', (novo_cpf, nome))
        elif opcao == '5':
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            nova_cidade = input("Nova cidade: ")
            novo_cpf = input("Novo CPF: ")
            cursor.execute('''UPDATE clientes SET nome = ?, email = ?, cidade = ?, cpf = ? 
                             WHERE nome = ?''', (novo_nome, novo_email, nova_cidade, novo_cpf, nome))
        else:
            print("Opção inválida!")
            return
        
        conexao.commit()
        print("✓ Cliente atualizado com sucesso!")
        
    except sqlite3.IntegrityError as e:
        print(f"✗ Erro: {e}")

# Menu principal
while True:
    print("\n=== MENU ===")
    print("1. Adicionar cliente")
    print("2. Listar clientes")
    print("3. Excluir cliente")
    print("4. Atualizar cliente")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção (1-5): ")
    
    if opcao == '1':
        adicionar_cliente()
    elif opcao == '2':
        listar_clientes()
    elif opcao == '3':
        excluir_cliente()
    elif opcao == '4':
        atualizar_cliente()
    elif opcao == '5':
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

