from controller import entrada, tabelaPrecos, saida
from time import sleep
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
                os.system('cls')
                with open('estacionamento.txt') as file:
                    lines = file.readlines()
                dispo = 0
                dispo = 10 - len(lines)
                if dispo >0:
                    print(f"Existem {dispo} vagas disponíveis\n")
                    sleep(0.5)
                    dados = {}
                    dados['placa'] = str(input("Placa do Veículo: ")).upper().strip()
                    dados['modelo'] = str(input("Marca/Modelo: ")).upper().strip()
                    dados['cor'] = str(input("Cor do veículo: ")).upper().strip()
                    # Input de Hora e Minutos pra Hora de Entrada
                    dados['entradaHora'] = int(input("Digite a hora de entrada: "))
                    dados['entradaMinuto'] = int(input("E os minutos: "))
                    # Salva o Horário de Entrada em Horas e Minutos
                    entrada(dados)
                else:
                    print("Não há vagas disponíveis no momento!\n")
            case "2":
                os.system('cls')
                # Tabela de preços basica exibida com prints.
                tabelaPrecos()
            case "3":
                os.system('cls')
                 # Informa a placa e busca no estacionamento.txt
                placa = input("Digite a placa Ex[ABCD1234]: ").strip().upper()
                saida(placa)
            case "4":
                os.system('cls')
                # Encerra o Programa
                print("** Programa Encerrado **\n")
                break
            case _:
                print("Opção Inválida.")

menu()