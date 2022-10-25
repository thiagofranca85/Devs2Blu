# Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa e cadastre-os 
# através de um dicionário em um input , se o número da carteira de trabalho for diferente de ZERO, o 
# dicionário receberá através de uma condicional também os dados do primeiro ano de contratação e o salário. 
# ao final do programa imprima os dados solicitados, esta construção deve ser feita através de funções
from controller import cadfuncionario, listarFuncionarios

def menu():
    while True:
        opcao = int(input("[1] Cadastro de Funcionário\n[2] Listar Funcionários\n[3] Fechar Programa\n:> "))

        match opcao:
            case 1:
                nome = input("Nome: ")
                nascimento = input("Nascimento: ")
                while True:
                    carteira = input("Carteira: ")  
                    if carteira != '':
                        anoContratacao = input("Ano Contratação: ")
                        salario = input("Salario: ")
                        break
                cadfuncionario(nome,nascimento,carteira,anoContratacao,salario)
            case 2:
                listarFuncionarios()
            case 3:
                print("Fechou o programa")
                break
            case _:
                print("Opção Inválida")

menu()