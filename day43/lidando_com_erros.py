def dividir(numerador, denonimador):
    try:
        resultado = numerador / denonimador
        print(f"O resultado da divisao eh {resultado}")
    except ZeroDivisionError:
        print("A divisao por 0 nao pode ocorrer")
    except TypeError:
        print("O codigo nao pode aceitar strings apenas numeros")
    print("Funcao rodou")

if __name__ == "__main__":
    dividir(5,"e")