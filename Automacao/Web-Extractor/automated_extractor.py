import requests
import pandas as pd
from pathlib import Path
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bs

# Requirements tem algumas bibliotecas que talves não estejam sendo usadas aqui
# Apenas para testes
# Arquivo .ipynb se abre com o Jupyter
# Pra instalar pip install notebook
# Pra abrir digite no console ou CMD "jupyter notebook"

url = 'site aqui'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
r = requests.get(url = url, headers = headers)
page = bs(r.text, 'html.parser')

#Le o arquivo e joga os dados para a variavel
# Essa linha apenas pega o padrao usado pelo cliente (CSV)
data = pd.read_csv(r'base-jean.csv')

#Joga os dados da data para um DataFrame
df = pd.DataFrame(data)

contaGotas = 1

# Lista pra pegar os atributos da classe do Produto
dadosProduto = page.findAll(attrs = {'class': 'box-produto'}) # Depois adicionamos um indice aqui p/ os Fors ou Whiles da vida

# Lista de Links dos Produtos
lista_Produtos = []

for link in dadosProduto:
    data = link.find('a').get('href')
    lista_Produtos.append(data)

for link in lista_Produtos:
    url_temp = 'site aqui'+link
    autoUrl = requests.get(url=url_temp, headers=headers)
    pageTemp = bs(autoUrl.text, 'html.parser')

    # Pega o nome do produto
    nome_produto = pageTemp.find(attrs={'class':'margin-info'}).find('h3').text.strip()
    # Pega os tamanhos do produto
    tamanho_produto = pageTemp.find(attrs={'class':'obs'}).text.strip('OFERTA Plus Size').strip().replace(' ', ',')

    # Pega o valor do produto
    valor_produto = pageTemp.find(attrs={'class':'valor'}).text.strip()

    # Pegar link das Cores
    listaSelecoesCores = []
    listaSelecoesCoresStr = ''

    dadosSelecoesCores = pageTemp.find(attrs = {'class':'form_input'}).findAll('option')
    
    for cor in dadosSelecoesCores:
        sel = cor.text.strip()

        if len(sel) > 2:
            if sel != 'Selecione':
                listaSelecoesCores.append(sel)
                listaSelecoesCoresStr += sel + ','
        else:
            listaSelecoesCoresStr = ''
            break

    if len(listaSelecoesCoresStr) > 3:
        listaSelecoesCoresStr = listaSelecoesCoresStr.rstrip(',')


    # Pegar link das imagens
    listaImgs = []
    listaImgsString = ''
    
    dadosImagens = pageTemp.find('form').find_all('img')

    for imagem in dadosImagens:
        img = imagem.get('src')
        listaImgs.append(img)
        listaImgsString += img+','

    listaImgsString = listaImgsString.rstrip(',')

    skuString = "SKU-"+str(contaGotas)

    newLineList = {
        'SKU': skuString,
        'Name': nome_produto,
        'Type': 'variable',
        'Published': '0',
        'Is featured?': '0',
        'Visibility in catalog': 'visible',
        'Description': 'Importado via Vision automation',
        'In stock?': '1',
        'Allow customer reviews?': '1',
        # 'Regular price': valor_produto.strip('R$').strip(),
        'Images': listaImgsString,
        'Attribute 1 name': 'Tamanho',
        'Attribute 1 value(s)': tamanho_produto,
        'Attribute 1 visible': '1',
        'Attribute 2 name': 'Cor',
        'Attribute 2 value(s)': listaSelecoesCoresStr,
        'Attribute 2 visible': '1'
    }
    
    newLineListChild = {
        'SKU': skuString+'-child',
        'Name': nome_produto,
        'Type': 'variation',
        'Published': '1',
        'Is featured?': '0',
        'Visibility in catalog': 'visible',
        # 'Description': 'Importado via Vision automation',
        'In stock?': '1',
        'Allow customer reviews?': '1',
        'Regular price': valor_produto.strip('R$').strip(),
        # 'Images': listaImgsString,
        'Parent': skuString,
        'Attribute 1 name': 'Tamanho',
        # 'Attribute 1 value(s)': tamanho_produto,
        # 'Attribute 1 visible': '1',
        'Attribute 2 name': 'Cor',
        # 'Attribute 2 value(s)': listaSelecoesCoresStr,
        # 'Attribute 2 visible': '1'
    }
    
    #Melhora para usar pandas concat, porem ainda não sei usar hehe
    # df2 = pd.DataFrame(newLineList)

    df = df.append(newLineList, ignore_index=True)
    df = df.append(newLineListChild, ignore_index=True)
    
    # df = df.concat([df, df2], ignore_index=True)
    
    # print(df)
    
    #Apenas um contador para terminar o loop com 10 tentativas
    contaGotas += 1
    if contaGotas == 10:
        break

df.to_csv('teste.csv')