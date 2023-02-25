# Source desse código
# https://github.com/MariyaSha/WebScraping/blob/master/WebScraping.ipynb
# No exemplo do repositório foi feito em jupyter notebook 
# Se quiser testar por lá, só digitar "pip install notebook" 
# Depois no terminal "jupyter notebook"

import urllib.request
from bs4 import BeautifulSoup as bs
from html.parser import HTMLParser
import re
import pandas as pd

# Carrega o código HTML do Link
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page, 'html.parser')

# Procura todos os nomes de função
# Interessante aqui que ele busca tudo 'dt' dentro do body inteiro.
names = soup.body.findAll('dt')
# Procura todas as funções que tem "random" no nome
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

# Procura todas as descrições das funções
description = soup.body.findAll('dd')
function_usage = []

for item in description:
  item = item.text
  item = item.replace('\n', ' ')
  function_usage.append(item)

print('Lista de nomes das funcoes:',function_names[:5])
print('\nDescrição da funcao:', function_usage[0])
print('\nNumero de funcoes:', len(function_names))
print('Numero de descricoes:', len(function_usage))

#create a dataframe
data = pd.DataFrame({'Nome da funcao': function_names, 'Uso da funcao': function_usage})
data.head()
data.to_csv('lista_funcoes_random.csv')