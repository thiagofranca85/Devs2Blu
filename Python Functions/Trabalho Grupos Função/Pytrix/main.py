# importando biblioteca
from time import sleep
import os

# importando as funcoes
from controller import saudacao, cadastrarcliente, salvar_itens, salvar_pagamento, ticket, salvarfilme, salvarpoltrona, limparticket

# Função Menu de clientePremium
def menuPremium():
    # chamando a funcao saudação da controller
    saudacao()

    while True:
            # criando a variavel de selecao da opcao premium
            clientePremium = str(input("Você gostaria de ser cliente Pytrix Premium e ter acesso à vários benefícios, como desconto em ingressos, bomboniere, e prioridade na escolha de assento? \nEsse cadastro é totalmente gratuito e sem outras taxas*:  [S/N] ")).strip().upper()

            while True:
                if clientePremium not in 'SN':
                    print('Opção Inválida, digite somente S ou N')
                    clientePremium = str(input("Você gostaria de ser cliente Pytrix Premium e ter acesso à vários benefícios, como desconto em ingressos, bomboniere, e prioridade na escolha de assento? \nEsse cadastro é totalmente gratuito e sem outras taxas*:  [S/N] ")).strip().upper()
                    sleep(1)
                else:
                    break    
                # condicao caso cliente premium for sim
            if clientePremium in 'S':
                # criando um dicionario vazio
                cliente = {}
                # inserindo os dados na variavel cliente via input
                cliente["Nome"] = str(input("Digite seu Nome: "))
                cliente["CPF"] = str(input("Digite seu CPF: "))
                cliente["Telefone"] = str(input("Digite Seu Telefone: "))
                cliente["Datanasc"] = str(input("Data de Nascimento: "))
                # gravando os dados inseridos no dicionario cliente dentro do arquivo txt
                cadastrarcliente(cliente.copy())
                os.system("cls")
                break
            else:
                #caso a opcao seja não irá direto pro menu
                os.system("cls")
                break

# Função Menu Filme
def menufilme():
    while True:
        filmes = {}
        # Aqui vem o menu com as opções de filmes, e uma validação caso não foi selecionado uma as opções válidas.
        filme = input("Qual filme você gostaria de assistir hoje? \n1- Matrix \n2- Star Wars IV - Uma Nova Esperança \n3- Clube da Luta \n4- Harry Potter e o Prisioneiro de Azkaban \n5- Top Gun - Maverick \n\nEscolha uma opção: ")
        match filme:
            # Se opção for 1
            case "1":
                filmes["Filme"] = "Matrix"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 2
            case "2":
                filmes["Filme"] = "Star Wars IV - Uma Nova Esperança"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 3
            case "3":
                filmes["Filme"] = "Clube da Luta"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 4        
            case "4":
                filmes["Filme"] = "Harry Potter e o Prisioneiro de Azkaban"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for 5
            case "5":
                filmes["Filme"] = "Top Gun - Maverick"
                # Chama a função para salvar no Dicionário
                salvarfilme(filmes)
                # Break para sair do Menu
                break
            # Se opção for inválida
            case _:
                print("\nOpção inválida.")
                print("\nEscolha um dos filmes em cartaz. \n")
                sleep(1)
        
    os.system("cls")  
    sleep(1)

# Função Menu de Poltrona    
def menupoltrona():
        #ofertar as opções de poltronas dentro de uma lista, e se possível - deve-se eliminar a opção selecionada pelo anterior.
        listaPoltronas = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5"]
        print(f"Escolha uma das poltronas disponíveis na lista {listaPoltronas}")

        #Aqui deve-se colocar uma validação para caso não selecionar uma das opções.
        while True:
            posicaoPoltrona = {}

            posicaoPoltrona["Poltrona"] = input("Escolha uma opção: ").upper()
    
            while True:
                if posicaoPoltrona["Poltrona"] not in listaPoltronas:
                    print("\nEscolha uma das opções oferecidas.")
                    print(f"\nEscolha uma das poltronas disponíveis na lista {listaPoltronas}")
                    posicaoPoltrona["Poltrona"] = input("\n>: ").upper()
                    
                else:
                    salvarpoltrona(posicaoPoltrona)
                    break
            break    
        os.system("cls")        
        sleep(1)

# Função Menu de Bomboniere
def menu_bomboniere():
    while True: 
        bombonieri = input("Você gostaria de algum item de bomboniere? S ou N \nQual opção: [S/N] ").strip().upper()
        while True:
            if bombonieri not in 'SN':
                print('Opção Inválida, digite somente S ou N')
                bombonieri = input("Qual opção: [S/N] ").strip().upper()
            else:
                break   
        if bombonieri in 'S':
            os.system("cls")
            break

    # Cria um Dicionário para a Bomboniere
    bomboniere = {"Pipoca": 0, "Refrigerante": 0, "Chocolate": 0}

    # Cria uma variável para referencia ao While
    opcao = "0"

    # Cria uma estrutura de repetição para o Menu Bomboniere
    while opcao != "4":
        os.system("cls")
        print('Escolha o seu item de bomboniere')
        print("[ 1 ] = Pipoca\n[ 2 ] = Refrigerante\n[ 3 ] = Chocolate\n[ 4 ] = Sair...")
        

        # Variável recebe a opção do Menu
        opcao = str(input("Escolha uma opção: "))

        # Switch com as opções da Bomboniere
        match opcao:
            # Se opção for 1
            case "1":
                # Inserindo ou incrementa no Dicionário
                bomboniere["Pipoca"] += int(input("\nInforme a quantidade: "))
                sleep(1)
            # Se opção for 2
            case "2":
                # Inserindo ou incrementa no Dicionário
                bomboniere["Refrigerante"] += int(input("\nInforme a quantidade: "))
                sleep(1)
            # Se opção for 3
            case "3":
                # Inserindo ou incrementa no Dicionário
                bomboniere["Chocolate"] += int(input("\nInforme a quantidade: "))
                sleep(1)
            # Se opção for 4
            case "4":
                # Sai do menu
                print("\nFinalizando a bomboniere.\n")
                sleep(1)
            # Se opção for válida
            case _:
                # Informa opção inválida
                print("\nOpção inválida.")
                sleep(1)
    
    salvar_itens(bomboniere)
    os.system("cls")
    sleep(1)            

# Função Menu Forma de Pagamento
def menu_pagamento():


    # Cria o um Dicionário para forma de pagamento
    forma_pagamento = {}

    # Cria uma estrutura de repetição para o Menu Forma de Pagamento
    while True:
        print('Selecione a opção de pagamento.')
        print("[ 1 ] = Dinheiro\n[ 2 ] = Cartão\n[ 3 ] = Pix")

        # Variável recebe a opção do Menu forma de PagaMENTO
        opcao = str(input("Escolha uma opção: \n"))

        # Switch com as opções da Bomboniere
        match opcao:
            # Se opção for 1
            case "1":
                forma_pagamento["Pagamento"] = "Dinheiro"
                # Chama a função para salvar no Dicionário
                salvar_pagamento(forma_pagamento)
                # Break para sair do Menu
                break
            # Se opção for 2
            case "2":
                forma_pagamento["Pagamento"] = "Cartão"
                # Chama a função para salvar no Dicionário
                salvar_pagamento(forma_pagamento)
                # Break para sair do Menu
                break
            # Se opção for 3
            case "3":
                forma_pagamento["Pagamento"] = "Pix"
                # Chama a função para salvar no Dicionário
                salvar_pagamento(forma_pagamento)
                # Break para sair do Menu
                break
            # Se opção for inválida
            case _:
                print("\nOpção inválida.")

    os.system("cls")
    sleep(1)

#Programa principal
#Chamando as funções
limparticket()
menuPremium()       
menufilme()
menupoltrona()
menu_bomboniere()
menu_pagamento()
ticket()   
