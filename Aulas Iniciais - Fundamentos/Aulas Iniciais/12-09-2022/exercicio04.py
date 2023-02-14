# Com base nas aulas passadas vamos criar um sorteio de lista e utilizando o conceito de estrutura de 
# decisão exibir qual foi a posição de ordem de inserção de dados que foi sorteada! usando o conceito 
# de importação otimizada importe a função choice, logo em seguida crie quatro variáveis representadas 
# por nomes n1, n2, n3, n4, essas variáveis devem ser do tipo string e devem solicitar dados. crie uma 
# variável que receba como lista estas quatro variáveis. crie uma variável usando a importação otimizada 
# e atribuindo a variável lista. crie uma função de impressão utilizando polimorfismo e quebra de linhas 
# para definir um cabeçalho para sua aplicação console. utilizando o conceito de interpolação exiba qual 
# foi o nome sorteado. utilizando o conceito de estrutura de decisão cria uma condição que exiba a ordem 
# em que foi digitado o nome sorteado pela variável de sorteio da lista!

from random import choice

n1 = input("Digite um nome: ")
n2 = input("Digite um nome: ")
n3 = input("Digite um nome: ")
n4 = input("Digite um nome: ")
lista = [n1, n2, n3, n4]

sorteio = choice(lista)

print("-"*5, " NOME SORTEADO ", "-"*5)
print(f"O nome sorteado foi {sorteio} que esta na posicao {lista.index(sorteio)} ")