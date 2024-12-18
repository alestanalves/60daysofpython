import time 

def cronometro(tempo):
    """
    Funcao que cria um cronometro, que conta ate o tempo especificado
    """

    print("Iniciando cronometro...")

    for segundo in range(tempo + 1):
        print(f"Tempo: {segundo} segundos", end="\r")
        time.sleep(1)

    print("\nCronometro finalizado!")

if __name__ == "__main__":
    tempo = 10
    cronometro(tempo)
