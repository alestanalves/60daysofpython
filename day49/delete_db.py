import sqlite3

conexao = sqlite3.connect("exemplo.db")

cursor = conexao.cursor()

cursor.execute("DELETE FROM personagens WHERE nome = 'Vegeta'")

conexao.commit()

print("O vegeta foi deletado com sucesso")

cursor.close()
conexao.close()