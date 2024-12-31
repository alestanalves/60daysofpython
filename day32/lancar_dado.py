from random import randint

def lancar_dado():
    """
    Simular o lancamento de um dado de 1 a 6

    Return:
        int: Um numero aleatorio de 1 a 6
    """

    return randint(1, 6)

if __name__ == "__main__":
    print(f"O resultado do dado foi: {lancar_dado()}")