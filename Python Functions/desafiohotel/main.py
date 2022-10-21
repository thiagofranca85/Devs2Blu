from controller_menu import *

def menu():
    saudacao()

    cond = 'sim'
    while cond == 'sim':

        opcao = input(f'\n{"*"*10} HOTEL {"*"*10}\n[1]Fazer Check-In\n[2]Relatório de Hospedes\n[3]Procurar Hospedes\n[4]Fazer Check-Out\n[5]Finalizar Atendimento\n:> ')

        match opcao:
            case '1':
                checkin()
            case '2':
                listarHospede()
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case _:
                print("Digite uma Opção Válida.")
        
        cond = str(input("Deseja voltar ao MENU?\nSim\nNao\n>: ")).lower()





menu()