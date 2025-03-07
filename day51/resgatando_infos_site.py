from bs4 import BeautifulSoup
import requests 

url = "http://books.toscrape.com"

response = requests.get(url)
if response.status_code == 200:
    print("Sucesso ao acessar o site")
else: 
    print("Erro ao acessar o site")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# precos = soup.find_all("p", class_="price_color")

livros = soup.find_all("article", class_="product_pod")

for livro in livros:
    titulo = livro.find("h3").find("a")['title']
    preco = livro.find("p", class_="price_color")
    estrelas = livro.find("p", class_="star-rating")['class'][1]
    print(f"Titulo: {titulo}, preco: {preco.text}, estrelas: {estrelas}")