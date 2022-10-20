from printsCustomizado import *
from controller import *

import os

os.system("cls")

while True:
    menu()
    option = input("Digite uma das opções descritas: ")

    match option:
        case '1':
            qtt = int(input("Digite a quantidade de números que serão somados: "))
            numbers = []
            for i in range(1, qtt+1):
                numbers.append(int(input(f"Digite o {i}º número: ")))
            5
            os.system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customSum(numbers)}')

        case '2':
            qtt = int(input("Digite a quantidade de números que serão subtraidos: "))
            numbers = []
            for i in range(1, qtt+1):
                numbers.append(int(input(f"Digite o {i}º número: ")))
            
            os.system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customSubtract(numbers)}')

        case '3':
            number1 = int(input(f"Digite o 1º número: "))
            number2 = int(input(f"Digite o 2º número: "))
            
            os.system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customDivide(number1, number2)}')

        case '4':
            qtt = int(input("Digite a quantidade de números que serão multiplicados: "))
            numbers = []
            for i in range(1, qtt+1):
                numbers.append(int(input(f"Digite o {i}º número: ")))
            
            os.system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {customMultiply(numbers)}')

        case '5':
            advancedMenu()
            while True:
                try:
                    equation = eval(input("Digite a equação: "))
                    break
                except:
                    os.system("cls")
                    headerPrint()
                    tablePrint(f"{RED}EQUAÇÃO INVÁLIDA{CLEANCOLOR}", True, True)
                    headerPrint()

            os.system("cls")
            headerPrint(f"== {GREEN}RESULTADO{CLEANCOLOR} ==", True)
            tablePrint(f'Total: {equation}')

        case _:
            headerPrint()
            tablePrint(f"{RED}OPÇÃO INVÁLIDA{CLEANCOLOR}", True, True)
