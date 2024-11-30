def busca_linear(lista, numero_procurado):
    """
    Procurar um numero dentro de uma lista utilizando busca linear

    :param lista: lista de numeros 
    :param numero_procurado: o numero que procurar
    """
    for i, numero in enumerate(lista): #funcao nativa do python enumerate 
    #enumerate passa por cada item dentro de uma lista enquanto contabiliza
        if numero == numero_procurado:
            return i
    return -1

lista = [10,2,4,6,7,8,11]
numero_procurado = 12

buscando_o_numero = busca_linear(lista, numero_procurado)
#print(buscando_o_numero)

if buscando_o_numero != -1:
    print(f"o numero se encotrando no indice: {buscando_o_numero}")
else:
    print("numero nao encontrado")

