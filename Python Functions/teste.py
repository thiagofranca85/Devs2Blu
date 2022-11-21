lista = [[23,51],[53,5312],[3,1]]

def somar(numero1, numero2):
    print(numero1 + numero2)

def multiplicar(numero1, numero2):
    print(numero1 * numero2)

def calcVarios(calc):
    for numeros in lista:
        calc(numeros[0], numeros[1])

# coloca a função somar ou multiplicar como parametro da função calcVarios, lembrando que não se deve colocar o parenteses na frente delas
calcVarios(somar)
print(somar)