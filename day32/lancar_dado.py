import random 

def lancar_dado():
    """
    Simula o lancamento de um dado de 6 faces.
    Return:
        int: Um numero inteiro entre 1 a 6
    """

    return random.randint(1, 6)

if __name__ == "__main__":
    print(f"O resultado do dado eh: {lancar_dado()}")