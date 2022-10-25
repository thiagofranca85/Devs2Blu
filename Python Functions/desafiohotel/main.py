from controller_menu import *

def menu():
    
    while True:

        opcao = input(f'{"*"*10} HOTEL {"*"*10}\n[1]Fazer Check-In\n[2]Relatório de Hospedes\n[3]Procurar Hospedes\n[4]Fazer Check-Out\n[5]Finalizar Atendimento\n:> ')

        match opcao:
            case '1':
                os.system('cls')
                print("*** Check In - Hospedes ***")
                nome = input("Nome do Hospede: ").title()
                while True:
                    telefone = input("Telefone: ")
                    if not(telefone.isnumeric()):
                        print("Digite um telefone valido.")
                    else:
                        break
                while True:
                    varcpf = input("CPF: ")
                    
                    hasError = False
                    # Limpa o cpf, retira pontos traços e tudo que não seja um número
                    cpf = [int(char) for char in varcpf if char.isdigit()]        

                    # verifica se o tamanho está correto
                    if len(cpf) != 11:
                        hasError = True

                    if not(hasError):
                        for i in range(9, 11):
                            value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
                            digit = ((value * 10) % 11) % 10
                            if digit != cpf[i]:
                                hasError = True
            
                    if hasError:
                        print(f"CPF inválido!")
                    else: 
                        dados = {}
                        dados['nome']=nome
                        dados['telefone']=telefone
                        dados['cpf']=varcpf
                        print(f"\nHospede cadastrado com sucesso\n")
                        salvarHospede(dados)
                        os.system('cls')
                        break
            case '2':
                os.system('cls')
                listarHospede()
            case '3':
                os.system('cls')
                if os.path.getsize('hospedes.txt') == 0:
                    print(f"\nNÃO HÁ HÓSPEDES\n")
                else:
                    print(">>> BUSCAR HOSPEDE <<<")
                    nomeHospedeDigitado = input("Nome: ").title()
                    procurarHospedes(nomeHospedeDigitado)
            case '4':
                os.system('cls')
                if os.path.getsize('hospedes.txt') == 0:
                    print(f"\nNÃO HÁ HÓSPEDES\n")
                else:
                    arquivo = open('hospedes.txt', 'r')

                    for numero, linha in enumerate(arquivo):
                        relatorio = linha.replace("{'nome':","Nome:").replace("'","").replace("telefone:","Telefone:").replace("cpf:","CPF:").replace("}","")
                        print(f"{numero + 1} -", relatorio)

                    print(">>> CHECKOUT HOSPEDE <<<")
                    indiceCheckout = int(input("Índice - Checkout: "))
                    checkout(indiceCheckout)
            case '5':
                os.system('cls')
                print("*** Programa Finalizado ***\n")
                break
            case _:
                print("Digite uma Opção Válida.")

os.system('cls') 
menu()