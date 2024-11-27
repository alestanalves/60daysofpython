#Um contador que para quando atingir um valor definido pelo usuário.
def contador_personalizado():
    try:
        limite = int(input("Digite o valor maximo do contador: "))
        #funcao range cria uma lista de numero a partir do 0
        #ate o valor definido pelo usuario
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contador atingiu o limite")
                break
    except ValueError:
        print("Entrada invalida. Por Favor insira um numero inteiro.")

contador_personalizado()