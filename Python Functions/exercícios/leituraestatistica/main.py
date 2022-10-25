# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um 
# dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas; 
# B) A média de idade do grupo; 
# C) Uma lista com todas as mulheres; 
# D) Uma lista com todas as pessoas com idade acima da média.
from controller import *

def menu():    
    while True:
        opcao = input("[1]Cadastrar\n[2]Listar Dados\n[3]Fechar Programa\n:> ")
        match opcao:
            case '1':
                nome = input("Nome: ")
                while True:
                    sexo = input("Sexo(m ou f ou nb): ")
                    match sexo:
                        case 'm':
                            sexo='m'
                            break
                        case 'f':
                            sexo='f'
                            break
                        case 'nb':
                            sexo='nb'
                            break
                        case _:
                            print("Digite sua orientação sexual corretamente.")                              
                while True:                                    
                    idade = input("Idade: ")
                    if not(idade.isnumeric()):
                        print("Digite uma idade válida.")
                    else:
                        break
                cadastro(nome,sexo,idade)                
            case '2':
                listarEstatistica()
            case '3':
                print("Falowss")
                break
            case _:
                print("Digite a opção certa ai jovem.")
menu()