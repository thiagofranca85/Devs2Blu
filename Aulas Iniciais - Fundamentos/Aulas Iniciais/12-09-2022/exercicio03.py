# Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão. 
# crie duas variáveis recebendo dados numéricos com casas decimais, a descrição deve ser relacionada 
# com primeira nota e segunda nota! crie uma variável para realizar este cálculo, não esqueça de utilizar o 
# conceito de ordem de procedência aritmética. crie uma função de impressão utilizando polimorfismo e 
# quebra de linhas para definir um cabeçalho para sua aplicação console. utilizando máscara de substituição 
# imprima de forma descritiva a primeira nota, utilize quebra de linha, imprima a segunda nota, utilize a 
# quebra de linha e imprima o resultado. usando estrutura de decisão crie uma condição onde o resultado for 
# maior que sete imprima na sua aplicação console que este aluno está acima da média. usando estrutura de 
# decisão crie uma condição onde o resultado for igual a sete imprima na sua aplicação console que este aluno 
# está na média. usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima 
# na sua aplicação console que este aluno pode solicitar recuperação. usando estrutura de decisão crie uma 
# condição onde o resultado for entre quatro e cinco imprima na sua aplicação console que este aluno deve 
# procurar o professor. Usando estrutura de decisão crie uma condição de saída e imprima na sua aplicação 
# console que este aluno infelizmente não atingiu o esperado!

n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite uma nota: "))
media = (n1 + n2) / 2

print("-"*5, " Calculadora ", "-"*5)
print("1a Nota: {}\n2a Nota: {}\nMedia: {}".format(n1, n2, media))

if media == 7.0:
    print("Voce esta na media")

elif media >=5.0 <7.0:
    print("Voce pode solicitar recuperação")

elif media >=4.0 <5.0:
    print("Voce deve procurar o professor")

else:
    print("Infelizmente voce nao atingiu o esperado")