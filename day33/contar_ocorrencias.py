from collections import Counter

def contar_ocorrencias(lista):
    """
    Contar as ocorrencias de cada elemento em uma list
    Arg:
        lista (list): A lista de elemento a ser analisada

    Return:
        Counter: Um objeto do tipo counter contendo a contagem de cada elemento
    """

    contagem = Counter(lista)

    for elemento, quantidade in contagem.items():
        print(f"{elemento}: {quantidade}")

    return "Contagem realizada com sucesso"

if __name__ == "__main__":
    lista_exemplo = ['banana', 'laranja', 'uva', 'laranja', 'uva', 'pera']

    #print(contar_ocorrencias(lista_exemplo))

print(Counter(lista_exemplo))