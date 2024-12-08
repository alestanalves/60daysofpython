def calcular_media_notas(notas):
    """
    Calculando media de notas a partir de uma lista de notas

    Arg:
    notas (lista)

    Return:
    float da media das notas
    """

    media = sum(notas) / len(notas) 

    #round arrendonda a nossa media para duas casas decimais
    return round(media, 2)

print(calcular_media_notas([10,4,5,6,9]))

