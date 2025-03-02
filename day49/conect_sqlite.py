import sqlite3

conexao = sqlite3.connect("exemplo.db")

cursor = conexao.cursor()

print("Conexao estabelecida com sucesso")

# cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS personagens (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                nome TEXT NOT NULL,
#                poder INTEGER NOT NULL,
#                universo TEXT NOT NULL)
#                """)

# print("A tabela foi criada com sucesso")

cursor.execute("""
                INSERT INTO personagens (nome, poder, universo)
                VALUES ("Goku", 9000, "Dragon Ball")
               """)

cursor.execute("""
                INSERT INTO personagens (nome, poder, universo)
                VALUES ("Vegeta", 8000, "Dragon Ball")
               """)

conexao.commit()

print("Dados inseridos com sucesso")

conexao.close()

