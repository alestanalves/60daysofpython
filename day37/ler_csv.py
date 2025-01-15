#pip install pandas
#python3 -m pip install pandas
import pandas as pd

def main():
    nome_arquivo = "test.csv"

    df = pd.read_csv(nome_arquivo)

    print(df)

    #mostra apenas as 5 primeiras linhas
    print(df.head())

    #pegar informacoes do df
    print(df.info())

    #exibi o formato do df
    print(df.shape)

if __name__ == "__main__":
    main()