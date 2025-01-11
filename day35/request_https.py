import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    print("Sucesso!")
    data = response.json()

    print("Essa eh a piada do Chuch Norris")
    print(data['value'])
else:
    print("Erro ao chamar a API do Chuck Norris")