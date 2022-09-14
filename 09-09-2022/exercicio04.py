# 04-EXERCÍCIO: Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas 
# decimais representando os 4 últimos salários de uma (pessoa). 
# crie uma variável para realizar a soma entre estes salários. 
# crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, 
# utilizando o conceito de polimorfismo imprima a palavra Calculadora no centro da sua aplicação console, 
# Logo em seguida use apenas uma vez a função de impressão, 
# descreva cada campo com uma máscara de substituição, 
# Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na sua aplicação console, 
# deve ser utilizado os caracteres especiais de quebra de linha e na impressão deve apresentar 
# apenas duas casas após a vírgula imprima no final utilizando a variável de soma para imprimir o 
# resultado final do seu exercício.

salario1 = float(input("Qual seu primeiro salario? "))
salario2 = float(input("Qual seu primeiro salario? "))
salario3 = float(input("Qual seu primeiro salario? "))
salario4 = float(input("Qual seu primeiro salario? "))
total_salarios = salario1 + salario2 + salario3 + salario4

print("="*6, " CALCULADORA ", "="*6)
print("Salario 1: {:.2f}.\nSalario 2: {:.2f}.\nSalario 3: {:.2f}.\nSalario 4: {:.2f}.\nTotal: {:.2f}".format(salario1,salario2,salario3,salario4,total_salarios))
