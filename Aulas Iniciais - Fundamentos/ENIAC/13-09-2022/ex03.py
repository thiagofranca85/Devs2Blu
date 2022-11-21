'''
*Crie uma variável do tipo inteiro solicitando dados.
*Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
*Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string 
*cabeçalho adicione quebra de linha, ao final.
*Crie um laço de repetição que execute o índice de contagem crescente até o número digitado pelo usuário.
*Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois do string utilize 
como rodapé.
'''
n1 = int(input('Escreva algum número inteiro: '))
poli = '='*5

print(f'\n {poli} INICIO {poli}\n')

for c in range(0,n1+1):
    print(c)

print(f'\n {poli} FIM {poli}\n')