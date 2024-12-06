def contar_palavras(texto):
    """
    Contar palavras em uma string
    :param texto: String de entrada
    :return: Numero de palavras 
    """
    #Vai separar as palavras usando o espaco entre as palavras
    palavras = texto.split()

    return len(palavras)

print(contar_palavras("oi tudo bem, como vai vc?"))

# texto = "oi tudo bem, como vai vc?"
# palavras = texto.split()
# print(palavras)