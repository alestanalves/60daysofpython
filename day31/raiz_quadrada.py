import math

def raiz_quadrada(numero):
    """
    Calcula a raiz quadrada de um numero

    Args:
        numero (float): O numero a ser calculado a raiz quadrada

    Return:
        float: A raiz quadrada calculada
    """

    if numero < 0:
        raise ValueError("Nao foi possivel calcular, coloque numeros positivos")
    
    return round(math.sqrt(numero), 2)

if __name__ == "__main__":
    print(raiz_quadrada(36))