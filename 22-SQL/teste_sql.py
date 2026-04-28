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

# Lista para salvar dados em JSON
clientes_lista = []

while True:
    print("\n=== Novo Cliente ===")
    nome = input("Digite o nome (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break

    email = input("Digite o email: ")
    cidade = input("Digite a cidade: ")
    cpf = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")

    try:
        # Inserir no banco
        cursor.execute('''INSERT INTO clientes (nome, email, cidade, cpf)
                          VALUES (?, ?, ?, ?)''', (nome, email, cidade, cpf))

        # Adicionar à lista para JSON
        clientes_lista.append({
            'nome': nome,
            'email': email,
            'cidade': cidade,
            'cpf': cpf
        })

        print(f"Cliente {nome} inserido com sucesso!")

    except sqlite3.IntegrityError as e:
        print(f"Erro: {e}. Dados não inseridos.")

# Salvar em JSON
with open('clientes.json', 'w', encoding='utf-8') as f:
    json.dump(clientes_lista, f, indent=4, ensure_ascii=False)

conexao.commit()
print(f"\nTotal de clientes inseridos: {len(clientes_lista)}")
print("Dados salvos no banco e em clientes.json")

conexao.close()

