from pathlib import Path
import sqlite3

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
conexao.row_factory = sqlite3.Row

cursor = conexao.cursor()

try:
    # 1. Executa todas as operações
    cursor.execute('DELETE FROM clientes WHERE id = 8')
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 3', 'teste3@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (9, 'Teste 4', 'teste4@gmail.com'))
    
    # 2. Se chegou até aqui sem erros, confirma tudo de uma vez
    conexao.commit()
    print("Transação concluída com sucesso!")

except Exception as exc:
    # 3. Se qualquer linha acima falhou, desfaz TUDO o que foi feito no bloco try
    print(f'Ops! um erro ocorreu! {exc}')
    conexao.rollback()