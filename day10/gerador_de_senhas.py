import random
import string 

#random fornece funcoes para gerar numeros aleatorios
#string fornece um conjunto de caracteres prontos
#como letras maisculas, numeros e simbolos

def gerador_de_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''

    while len(senha) < comprimento:
        senha += random.choice(caracteres)

    print(f"Sua senha ficou assim: {senha}")

gerador_de_senhas(10)