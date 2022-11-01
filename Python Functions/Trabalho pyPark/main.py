from controller import disponivel, entrada, tabelaPrecos, saida
import os

poli = "*" *28
def menu():
    #print ultilizando polimorfismo e quebra de linhas
    print(f"\n{poli} \nBem-vindo ao Menu do pyPark\n{poli}\n") 
        
    while True:        
        #variavel com input para escolher uma das opçoes
        escolha = input("Escolha a Opção Desejada:\n 1 => Entrada de Veículo\n 2 => Tabela de Preços\n 3 => Saída de Veículo\n 4 => Encerrar Programa\n>> ") 
        
        match escolha:
            case "1":                
                # Inserção de dados dos carros.
                dados = {}
                dados['placa'] = str(input("Placa do Veículo: ")).upper().strip()
                dados['modelo'] = str(input("Marca/Modelo: ")).upper().strip()
                dados['cor'] = str(input("Cor do veículo: ")).upper().strip()
                dados['entradaHora'] = int(input("Digite a hora de entrada: "))
                dados['entradaMinuto'] = int(input("E os minutos: "))
                entrada(dados)
            case "2":
                # Tabela de preços basica exibida com prints.
                tabelaPrecos()
            case "3":
                 # Informa a placa e busca no estacionamento.txt
                placa = input("Digite a placa Ex[ABCD1234]: ").strip().upper()
                saida(placa)
            case "4":
                # Encerra o Programa
                os.system('cls')
                print("** Programa Encerrado **\n")
                break
            case _:
                print("Opção Inválida.")
menu()