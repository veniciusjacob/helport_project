import sqlite3
import os

# Conexão com o banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'database', 'support_database.db')
conn = sqlite3.connect(db_path)


cursor = conn.cursor()

# Criação da tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS support
                  (problem TEXT, response TEXT)''')

# Inserção de dados de exemplo
data = []
cursor.executemany('INSERT INTO support VALUES (?, ?)', data)

# Salva as alterações e fecha o banco de dados
conn.commit()
conn.close()
