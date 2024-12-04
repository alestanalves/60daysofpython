def anagrama(palavra1, palavra2):
    """
    Verificar se duas palavras sao um anagrama ou nao
    :param palavra1: Primeira palavra
    :param palavra2: Segunda palavra
    :return: True se as palavras forem um anagrama
    """

     # Removendo espaços e convertendo para letras minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras sao anagramas"
    return f"Essas palavras nao sao anagramas"

print(anagrama("roma", "amor"))