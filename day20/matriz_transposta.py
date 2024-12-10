def transpor_matriz(matriz):
    """
    Gerar uma matriz transposta de 3x3
    Substitui colunas horizontais por verticais

    Exemplo
    [1 , 2 , 3]    
    [1 , 2 , 4]
    [1 , 2 , 5]   

    [1 , 1 , 1]    
    [2 , 2 , 2]
    [3, 4, 5]    

    Arg: Matriz que vao listas de 3 numeros na horizantal e vertical
    Return: Matriz transposta
    Raises: ValueError: Se a matriz nao ter 3x3
    """

    #verificador se a matriz eh 3x3
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz nao possui o tamanho 3x3")
    
    #gerar a matriz transposta
    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]

    return transposta 

#explicacao da nossa matriz transposta utilizando iteradores e listas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = []

for i in range(3):
    # iniciando uma nova linha 
    nova_linha = []

    for j in range(3):
        #adiciona o elemento corresponde a matriz original
        nova_linha.append(matriz[j][i])

    #print(nova_linha)
    transposta.append(nova_linha)

for linha in transpor_matriz(matriz):
    print(linha)