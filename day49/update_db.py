import sqlite3

conexao = sqlite3.connect("exemplo.db")

cursor = conexao.cursor()

cursor.execute("UPDATE personagens SET poder = 9500 WHERE nome = 'Goku'")

conexao.commit()

print("Dados atualizados para o Goku")

cursor.close()
conexao.close()