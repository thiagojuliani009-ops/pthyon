import sqlite3


conexao = sqlite3.connect('novo_banco.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)''')
conexao.commit()
conexao.close()