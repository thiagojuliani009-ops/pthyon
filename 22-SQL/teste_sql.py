import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)''')

# Inserir dados
cursor.execute('''INSERT INTO clientes (id, nome, email) 
                  VALUES (001, 'Thiago', 'thiagojuli@senac')''')

conexao.commit()
print("Dados inseridos com sucesso!")

conexao.close()

