from controller import somasalario

def menu():
    print("="*15, "Calculadora Salario", "="*15, "\n")
    var = 'sim'
    while var == 'sim':
        n1 = float(input("Digite salario: "))
        n2 = float(input("Digite salario: "))
        n3 = float(input("Digite salario: "))
        n4 = float(input("Digite salario: "))

        resultado = somasalario(n1, n2, n3, n4)
        print("A soma dos salarios é: {}".format(resultado))

        var = input("Voce deseja continuar? \nsim \nnao\n:>")

menu()
print("Voce saiu do programa")