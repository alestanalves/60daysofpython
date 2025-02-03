class Ninja:
    def __init__(self, nome, chakra):
        self.nome = nome
        self.chakra = chakra

    def usar_jutsu(self, custo_crakra):
        try:
            if custo_crakra > self.chakra:
                raise ValueError("Chakra Insuficiente!")
            self.chakra -= custo_crakra
            print(f"{self.nome} usou o jutsu com sucesso")
        except ValueError as Error:
            print(f"Erro: {Error} foi detectado. O {self.nome} precisa recuperar seu crakra")

if __name__ == "__main__":
    naruto = Ninja(nome="Kakashi", chakra=200)
    naruto.usar_jutsu(300)