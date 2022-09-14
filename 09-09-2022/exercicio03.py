# 3-EXERCÍCIO: Crie variáveis com tipos predefinidos, utilizando a função de inserção de dados, 
# fica a seu critério a utilização de nomes de variáveis, crie no mínimo 4 variáveis, 
# usando máscara de substituição atribua estas variáveis as suas respectivas descrições

nome = str(input("Qual seu nome? "))
idade = int(input("Qual a sua idade? "))
altura = float(input("Qual a sua altura? "))
pizza = bool(int(input("Voce gosta de Pizza? 1-SIM / 0-NAO ")))

# A mascara de substituicao é feita usando format
print("Nome: {}. Idade: {}. Altura: {}. Pizza? {}".format(nome,idade,altura,pizza))