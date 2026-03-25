import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect (ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor): 
   cursor.execute(
      "CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
   conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
 data = ("nome, email")
 cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", data) 
 conexao.commit()

def atulizar_registro(conexao, cursos, nome, email, id):
  data = (nome, email, id)
  cursos.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", data)
  conexao.commit()

def excluir_registro(conexao, cursor, id):
  data=(id,)
  cursor.execute("DELETE FROM clientes WHERE id=?;", data)
  conexao.commit()

excluir_registro(conexao, cursor, 1)

def inserir_muitos(conexao, cursor, dados):
  cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
  conexao.commit()

dados = [
  ("Thiago", "tjo@gmail.com"),
  ("James", "j.silva@gmail.com"),
  ("eduarda", "duda@gmail.com"),
]
for clientes in dados:
    inserir_registro(conexao, cursor, clientes[0], clientes[1])
#inserir _muitos(conexao, cursor, dados)

