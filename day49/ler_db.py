import sqlite3

conexao = sqlite3.connect("exemplo.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM personagens")

personagens = cursor.fetchall()

print("Personagens:")
for personagem in personagens:
    print(personagem)

cursor.close()
conexao.close()