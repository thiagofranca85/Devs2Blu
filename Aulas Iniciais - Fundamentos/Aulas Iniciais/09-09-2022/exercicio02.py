# 2-EXERCÍCIO: Crie Variáveis utilizando a função que solicita inserção de dados, 
# fica a seu critério a utilização de nomes de variáveis, 
# crie no mínimo 5 variáveis usando o conceito dinâmico onde o 
# python usa sua semântica para identificar o tipo da variável usando a função de 
# impressão de dados use o conceito de interpolação e imprima os dados atribuídos na chamada!

nome = input("Qual o seu nome?: ")
idade = input("Qual a sua idade?: ")
pretensao_salarial = input("Qual a sua pretensao Salarial?: ")
musica = input("Voce gosta de musica? ")
numero = input("Digite um numero aleatorio: ")

# Interpolação = variaveis entre strings conforme abaixo.
print(f"Nome:{nome} Idade:{idade} Pret. Salarial:{pretensao_salarial} Musica?{musica} Numero aleatorio:{numero}.")
