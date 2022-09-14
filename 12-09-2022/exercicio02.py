# exercício-02 usando a biblioteca interna random use o conceito de importação de toda biblioteca. 
# crie quatro variáveis recebendo valores, essas variáveis devem ser com tipos predefinidos tipo string, 
# crie uma variável recebendo uma lista das 4 variáveis, logo em seguida utilize importação da biblioteca e 
# atribua a função embaralhar(shuffle). essa importação irá realizar o embaralhamento dos valores recebidos 
# atribua a lista a esta função. crie uma função de impressão utilizando polimorfismo e quebra de linhas para 
# definir um cabeçalho para sua aplicação console. utilizando a interpolação exiba em seguida com a função 
# de impressão a ordem definida dos nomes da variável lista.

import random

n1 = input("Digite um nome: ")
n2 = input("Digite um nome: ")
n3 = input("Digite um nome: ")
n4 = input("Digite um nome: ")
lista = [n1, n2, n3, n4]

random.shuffle(lista)
print("-"*10, "Lista Embaralhada", "-"*10)
print(f"Nomes: {lista}")

