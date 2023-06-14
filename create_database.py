import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('support_database.db')
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
