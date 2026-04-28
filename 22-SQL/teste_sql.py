import _sqlite3
conn = _sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE usuario (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')
conn.commit()
conn.close()