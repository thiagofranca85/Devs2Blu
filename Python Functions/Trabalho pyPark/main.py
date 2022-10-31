from controller import entrada, tabelaPrecos, saida
import os

poli = "*" *28
def menu():
    #print ultilizando polimorfismo e quebra de linhas
    print(f"\n{poli} \nBem-vindo ao Menu do pyPark\n{poli}\n") 
        
    while True:
        
        #variavel com input para escolher uma das opçoes
        escolha = input("Escolha a Opção Desejada:\n 1 => Entrada de Veículo\n 2 => Tabela de Preços\n 3 => Saída de Veículo\n 4 => Fechamento\n 5 => Encerrar Programa\n>> ") 
        match escolha:
            case "1":
                entrada()
            case "2":
                tabelaPrecos()
            case "3":
                 # Informa a placa e busca no estacionamento.txt
                placa = input("Digite a placa Ex[ABCD1234] :").strip().upper()
                saida(placa)
            case "4":
                # Fechamento
                # fechamento()
                pass
            case "5":
                os.system('cls')
                print("** Programa Encerrado **\n")
                break
            case _:
                print("Opção Inválida.")
menu()