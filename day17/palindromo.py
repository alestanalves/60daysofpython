def eh_palindromo(texto):
    """
    Verificar se um numero, texto ou palavra eh um palindromo
    :param texto: Palavra, texto ou numero
    :return: Uma mensagem indicando se eh um palindromo ou nao
    """
    texto = str(texto).replace(" ", "").lower()

    if texto == texto[::-1]:
        return f"{texto} eh um palindromo"
    return f"{texto} nao eh um palindromo"

print(eh_palindromo(123321))