def calcular_imc():
    """
    Funcao que calcula o IMC
    """

    print("Bem vindos a calculadora de IMC")

    try:
        peso = float(input("Digite o seu peso em quilogramas: "))

        altura = float(input("Digite sua altura em metros: "))

        if peso < 0 or altura < 0:
            print("O peso e altura deve ser maior que O")
            return #encerrar a funcao
    
        imc = round(peso / (altura ** 2), 2)

        if imc < 18.5:
            print("Voce esta abaixo do peso ideal")
        elif 18.5 <= imc < 24.9:
            print("Voce esta no peso normal")
        elif 25 <= imc < 29.9:
            print("Voce esta de sobrepeso")
        else:
            print("Voce esta com obesidade")

    except ValueError:
        print("A entrada esta invalida")

def hello_world():
    print('ola mundo')

# Significa que estamos rodando esse codigo internamente 
# Apenas roda se eu rodar o meu script calcular_imc 
if __name__ == "__main__":
    calcular_imc()