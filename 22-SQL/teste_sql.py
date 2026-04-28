import  sqlite3
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)''')
conexao.commit()

cursor.execute('''INSERT INTO clientes (nome, email) VALUES (?, ?)''', ('João Silva', 'joao.silva@example.com'))
conexao.commit()
print('Cliente inserido com sucesso!')
cursor.execute('SELECT * FROM clientes')
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)
conexao.close()
