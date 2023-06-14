import sqlite3
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def search_database(query):
    # Conexão com o banco de dados
    conn = sqlite3.connect('support_database.db')
    cursor = conn.cursor()

    # Tokenização e stemming da consulta
    tokens = word_tokenize(query)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Construção da consulta SQL usando LIKE para assimilação
    sql_query = "SELECT response FROM support WHERE "
    for i, token in enumerate(stemmed_tokens):
        if i > 0:
            sql_query += " AND "
        sql_query += "problem LIKE ?"
    
    # Executar a consulta no banco de dados com os bindings corretos
    cursor.execute(sql_query, tuple('%' + token + '%' for token in stemmed_tokens))
    result = cursor.fetchone()

    # Fechar o banco de dados
    cursor.close()
    conn.close()

    # Retornar a resposta encontrada ou None se não houver correspondência
    if result is not None:
        return result[0]
    else:
        return None


def add_to_database(input_text, response):
    # Conexão com o banco de dados
    conn = sqlite3.connect('support_database.db')
    cursor = conn.cursor()

    # Inserção da entrada e resposta no banco de dados
    cursor.execute("INSERT INTO support (problem, response) VALUES (?, ?)", (input_text, response))

    # Salva as alterações e fecha o banco de dados
    conn.commit()
    conn.close()
