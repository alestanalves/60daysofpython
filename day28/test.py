import random

def jogar_forca():
    """
    Jogo da Forca: o usuário tenta adivinhar a palavra secreta antes de esgotar as tentativas.
    """
    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra secreta, letra por letra.")
    
    # Lista de palavras para o jogo
    palavras = ["python", "programacao", "desenvolvimento", "jogos", "computador"]

    # Escolhe uma palavra secreta aleatoriamente
    palavra_secreta = random.choice(palavras).lower()
    letras_corretas = ["_" for _ in palavra_secreta]  # Mostra "_" para cada letra da palavra
    tentativas_restantes = 6  # Número de tentativas disponíveis
    letras_erradas = []  # Lista para armazenar as letras já tentadas, mas incorretas

    # Loop do jogo
    while tentativas_restantes > 0:
        # Exibe o estado atual do jogo
        print("\n" + " ".join(letras_corretas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        # Solicita ao usuário uma letra
        tentativa = input("Digite uma letra: ").lower()

        # Verifica se o usuário já tentou essa letra
        if tentativa in letras_erradas or tentativa in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Verifica se a letra está na palavra secreta
        if tentativa in palavra_secreta:
            print("Acertou!")
            for i, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_corretas[i] = tentativa
        else:
            print("Errou!")
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1

        # Verifica se o jogador acertou toda a palavra
        if "_" not in letras_corretas:
            print("\nParabéns! Você acertou a palavra:", palavra_secreta)
            break
    else:
        # Caso o jogador perca
        print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    jogar_forca()
