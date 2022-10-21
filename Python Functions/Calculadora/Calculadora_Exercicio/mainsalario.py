# crie novo documento mainSalario Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais representando 
# os 4 últimos salários de uma pessoa. crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, utilizando o 
# conceito de polimorfismo e imprima a palavra, Calculadora no centro da sua aplicação console. utilizando o conceito de máscara de 
# substituição imprima descritivamente cada salário e a soma entre os mesmos imprimindo o resultado final. Ex " primeira variável : {} " 
# os dados devem ser apresentados um em cada linha na sua aplicação console, deve ser utilizado os caracteres especiais de quebra de linha
# e na impressão deve apresentar apenas duas casas após a vírgula imprima no final utilizando a variável de soma para imprimir o resultado 
# final do seu exercício. no documento controller crie uma função para calcular a soma do salario
from controller import somasalario

poli = "="*50

print(poli)
print(f" Calculadora Salarial ".center(50,"="))
s01 = float(input("Digite seus ultimos salarios: "))
s02 = float(input("Digite seus ultimos salarios: "))
s03 = float(input("Digite seus ultimos salarios: "))
s04 = float(input("Digite seus ultimos salarios: "))
print(poli)
print(f" O total de salarios é R${somasalario(s01,s02,s03,s04):.2f} ".center(50,"="))
print(poli)
