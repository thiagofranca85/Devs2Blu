# crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
# crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da 
# string cabeçalho adicione quebra de linha, ao final.
# crie um laço de repetição recebendo uma condição que irá executar apenas números pares esses números 
# devem percorrer até 1500.
# crie uma função de impressão após laço com a descrição parabéns você conseguiu!
# crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois 
# da string utilize como rodapé, definindo o fim do laço repetição!

border = "="*5
print(f"{border} CABEÇALHO {border}\n")
for i in range(0, 1501):
    if i % 2 == 0:
        print(i)

print("Parabens !!! Você conseguiu.\n")
print(f"{border} RODAPÉ {border}")