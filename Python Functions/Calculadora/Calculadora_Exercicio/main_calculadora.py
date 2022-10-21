from controller import soma,subtracao,multiplicacao,divisao

def menu():
    print('*'*25, 'MENU','*'*25)

    cond = 'sim'
    while cond == 'sim':
        n1 = int(input('Digite primeiro numero: '))
        n2 = int(input('Digite segundo numero: '))

        opcao = input('\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\nOperação :> ')

        match opcao:
            case '1':
                print(f"O resultado é {soma(n1, n2)}")
            case '2':
                print(f"O resultado é {subtracao(n1, n2)}")
            case '3':
                print(f"O resultado é {multiplicacao(n1, n2)}")
            case '4':
                print(f"O resultado é {divisao(n1, n2)}")
            case _:
                print("Seleciona uma opção valida.")

        cond = str(input('Deseja continuar?\nsim\nnao\n:>'))

menu()

print('Voce saiu da sua aplicação!')