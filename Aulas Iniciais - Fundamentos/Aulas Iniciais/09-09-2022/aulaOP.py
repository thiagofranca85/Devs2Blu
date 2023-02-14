validador = True
validador = False

idade = int(input("Digite sua idade: "))

print(" "*15, "Expressão de Igualdade", " "*15)


validador = (idade == 18)
print(validador)

# " "*15 <<< Isso é polimorfismo
print(" "*15, "Expressao de diferença", " "*15)

validador = ( idade != 18)
print(validador)

print(" "*15, "Expressao de maior", " "*15)
validador = ( idade > 18 )
print(validador)

print(" "*15, "Expressao de menor", " "*15)
validador = ( idade < 18 )
print(validador)

print(" "*15, "Expressao de maior e igual", " "*15)
validador = ( idade >= 18 )
print(validador)

print(" "*15, "Expressao de menor e igual", " "*15)
validador = ( idade <= 18 )
print(validador)
