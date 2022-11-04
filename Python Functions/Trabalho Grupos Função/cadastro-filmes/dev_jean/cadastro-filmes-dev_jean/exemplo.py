def soma(dado1, dado2):
    resultado = dado1 + dado2
    return resultado

dado1 = soma(1, 2)
dado2 = soma(5, 2)

soma3 = soma(dado1,dado2)
print (soma3)

soma4 = soma(soma(1, 2),soma(5, 2)) #Igual a função acima
print (soma4)

soma5 = soma(soma(dado1,dado2)-soma(10,5), 100)
print (soma5)


#Faça uma função para calcular a area de um triangulo retangulo
#Apos use a função de calculo de um triangulo retangulo para calcular a area de um quadrado.


#variavel = [1, 2, 3, 4, 5]

#print(variavel)

#print(variavel[2])

#for item in variavel:
#    print(item)

#for i in range(0,5,2):
#    print(variavel[i])
