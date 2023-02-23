import requests
import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bs

# Esse arquivo usei pra aprender a coletar os dados inicialmente
# Ele busca nome, valores etc da pagina INDEX do produto

url = 'site aqui'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

r = requests.get(url = url, headers = headers)

page = bs(r.text, 'html.parser')

upcoming_events_div = page.select_one('a.btn')

# Lista pra pegar os atributos da classe do Produto
dadosProduto = page.findAll(attrs = {'class': 'box-produto'}) # Depois adicionamos um indice aqui p/ os Fors ou Whiles da vida

# Pega o nome do produto
nome_produto = dadosProduto[0].find('h3').text.strip()

# Pega os tamanhos do produto
tamanho_produto = dadosProduto[0].find(attrs={'class':'obs'}).text.strip()

# Pega o valor do produto
valor_produto = dadosProduto[0].find(attrs={'class':'valor'}).text.strip()

# Aqui pega o link href do produto
print(dadosProduto[0].find('a').get('href'))

# Imprime dados dos produtos
print(nome_produto)
print(tamanho_produto)
print(valor_produto)

# Pra testar buscar informações das seleções do produto #1 [0]
url2 = 'link do site + produto'
r2 = requests.get(url = url2, headers = headers)
pageselecoes = bs(r2.text, 'html.parser')

dadosSelecoes = pageselecoes.find(attrs = {'class':'form_input'}).get_text("\n",strip=True).replace('Selecione','').strip()
print(dadosSelecoes)

# Pegar link das imagens
dadosImagens = pageselecoes.findAll('img')
linksImagens = dadosImagens[0].get('src')
for imagem in dadosImagens:
    print(imagem.get('src'))

print(linksImagens)






