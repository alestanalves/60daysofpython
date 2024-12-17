def celsius_para_fahrenheit(celsius):
    """
    Converte a temperatura de Celsius para Fahrenheit

    Arg:
        celsius (float): A temperatura em Celsius

    Returns:
        float: A temperatura em Fahrenheit
    """
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_para_celsius(fahrenheit):
    """
    Converte a temperatura de Fahrenheit para Celsius

    Args:
        fahrenheit (float): A temperatura em Fahrenheit

    Returns:
        float: A temperatura em Celsius
    """
    return round((fahrenheit - 32) * 5/9, 2)

def main(temperatura, tipo_conversao):
    """
    Funcao principal que recebe a temperatura e o tipo de conversao e retorna a temperatura convertida

    Args:
        temperatura (float): A temperatura a ser convertida
        tipo_conversao (str): O tipo de conversao a ser realizada

    Returns:
        float: A temperatura convertida
    """
    if tipo_conversao == "celsius":
        print(celsius_para_fahrenheit(temperatura))
    elif tipo_conversao == "fahrenheit":
        print(fahrenheit_para_celsius(temperatura))
    else:
        return print("Tipo de conversao invalido")


if __name__ == "__main__":
    main(20, "celsius")
    main(20, "fahrenheit")
