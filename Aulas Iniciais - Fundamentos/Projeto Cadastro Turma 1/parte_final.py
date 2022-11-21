"""
O intuito é fazer um chatbot de suporte técnico.
1- Primeiramente terá um menu questionando ao usuário se ele quer se identificar ou não (reclamar de forma anônima)
- Se ele escolher se identificar, o usuário deve informar seu nome, CPF e telefone.

2- Após isso, o programa tem que questionar se o usuário quer fazer uma reclamação ou alterar um dado.
- Se ele escolher reclamação, ele deve digitar o que aconteceu, após isso o usuário poderá escolher entre
finalizar o suporte ou conversar com um atendente.

3- Se ele escolher falar com atendente deverá entrar na fila de espera

4- Se ele escolher alterar dados, o usuário deverá escolher qual dado quer alterar
- No caso dele alterar algum dado, as informações do usuário que estarão salva num dicionário deverão ser
atualizadas pelo programa.

5 - No caso da alteração do cpf, o programa deverá informar se o dado digitado pelo usuário é um valor de cpf válido.

1 - No caso de ser anônimo, o usuário vai direto pra parte de reclamar (já que não tem dado pra ser verificado ou coisa do tipo)
"""

from datetime import date               # biblioteca para utilização da data
from random import randint, choice      # biblioteca para sorteio de números inteiros e str
from os import system                   # biblioteca para "limpar a tela"
import time


# DEFINIÇÕES DE VARIÁVEIS
poli = "="*55
id = ''                 # variável utilizada para menu e demais opções
cadastro = dict()       # dicionário para salvar os dados do usuário
                        # cadastro = {'nome': 'joao', 'cpf': '78946667945'}  exemplo

# LISTAS
rLista = list()  # Respostas dos cálculos/validador  ** FOI USADA COMO TEMPORÁRIA NO VALIDADOR DE TELEFONE **
listaCPF = list()  # Lista do CPF fracionado em str
listaInt = list()  # LIsta do CPF fracionado em int

r = ['sim', 'não', 'nao']
# MENSAGEM DE INÍCIO DO BOT E CONFIRMACAO DE IDENTIFICAÇÃO
while True:
    id = str(input("\nBEM-VINDO(A) AO CHATBOT!\nPor favor, digite SIM para se identificar ou NÃO para continuar: ")).strip().lower()
    if id in 'simnaonão' :
        break


# SOLICITACAO DE DADOS DO USUARIO.
while True:
    system('cls')
    if id == "sim":
        print("\nPara darmos seguimento tenha em mãos os seguintes dados: Nome completo, número de CPF e telefone")

        # NOME
        cadastro['nome'] = str(input("Agora, por favor informe seu nome: "))
        print(f"Obrigado, {cadastro['nome'].upper()}! Agora precisamos de seu CPF! ")


        # VALIDADOR DE CPF
        # CPF deve ser salvo como STR porque caso inicie com '0' irá dar erro ao salvar no dicionário

        system('cls')
        while True:
            # VARIÁVEIS             # variáveis estão dentro do loop, porque elas precisam ter
            decrescente = 10        # esses valores quando iniciarem novamente
            posicao = 0
            listaCPF.clear()  # limpa as listas no inicio do loop
            rLista.clear()
            listaInt.clear()

            cadastro['cpf'] = str(input('Informe seu CPF: ')).strip()   # remoção de espaços no inicio e fim da str
            cadastro['cpf'] = cadastro['cpf'].replace('.', '')  # REMOÇÃO DE '.' E '-'
            cadastro['cpf'] = cadastro['cpf'].replace('-', '')

            if len(cadastro['cpf']) != 11 or not cadastro['cpf'].isdecimal() or len(set(cadastro['cpf'])) == 1:
                # IRÁ PROCEGUIR CASO PASSE A PRIMEIRA VALIDAÇÃO
                # se CPF for diferente de 11 e se não for decimal
                # SET() REMOVE OS ITENS DUPLICADOS ex:[1,2,2,2,2,1,1,1] = {1,2}
                print('Digite o CPF corretamente!\n')  # Se digitar a quantidade de números errada

            else:
                listaCPF = list(cadastro['cpf'])  # CPF AINDA É UMA str e FOI FATIADO NA LISTA

                # PRIMEIRO DIGITO
                # PADRÃO
                """
                for c in range(0, len(listaCPF)):
                    listaInt.append(int(listaCPF[c]))       # CPF NA LISTA INT
                """

                # LIST COMPREHENSION
                [listaInt.append(int(digito)) for digito in listaCPF]

                for c in range(10, 1, -1):
                    """
                    Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente
                    de números de 10 à 2 e soma os resultados
                    """
                    rLista.append(listaInt[posicao] * c)  # c=10,9,8,7...  posicao=0,1,2,3,4...
                    posicao += 1  # O RESULTADO ESTÁ SENDO ADICIONADO EM OUTRA LISTA COMO int
                    # EU NÃO CONSEGUI FAZER ISSO SEM USAR DUAS LISTAS

                # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
                # Caso resto da divisão = 10, considerar = 0
                # Se o resultado for igual ao primeiro digito do cpf (posição 9), primeira parte da validação OK

                resultado = (sum(rLista) * 10) % 11  # sum(rLista) soma todos os elementos de rLista
                if resultado == 10:  # usar '0' para validação caso o resultado for 10
                    resultado = 0

                if resultado == listaInt[-2]:  # IRÁ PROCEGUIR CASO PASSE A PRIMEIRA VALIDAÇÃO
                    # SEGUNDO DIGITO
                    # VARIÁVEIS
                    decrescente = 10
                    posicao = 0
                    rLista.clear()  # LIMPA rLista

                    for c in range(11, 1, -1):
                        """
                        Vamos multiplicar os 10 primeiros números (9 números + 1 digito verificador) pela 
                        sequência decrescente de números de 11 à 2 
                        """
                        rLista.append(listaInt[posicao] * c)  # c=11,9,8,7...  posicao=0,1,2,3,4...
                        posicao += 1  # O RESULTADO ESTÁ SEDO ADICIONADO EM OUTRA LISTA COMO int E NÃO MAIS str
                        # EU NÃO CONSEGUI FAZER ISSO DE OUTRO JEITO

                    # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
                    # Caso resto da divisão = 10, considerar = 0
                    # Se o resultado for igual ao primeiro digito do cpf (posição 10) , primeira parte da validação OK

                    resultado = (sum(rLista) * 10) % 11
                    if resultado == 10:  # usar '0' para validação caso o resultado for 10
                        resultado = 0

                    if resultado == listaInt[-1]:
                        # print('CPF ok') print teste
                        #       *** FAZER A ALTERAÇÃO OU CADASTRO DO CPF AQUI ***##
                        listaCPF.insert(3, '.')  # inserindo "." e "-" no cpf para melhor vizualização na biblioteca
                        listaCPF.insert(7, '.')
                        listaCPF.insert(11, '-')
                        temporario = ''.join(listaCPF)  # Junta a lista novamente e passa ela para a variável
                        cadastro['cpf'] = temporario  # ADICINANDO O NÚMERO PARA O DICIONÁRIO
                        # print((cadastro['cpf']))       ** print teste **
                        break
                else:
                    print('CPF inválido!\n')
            # FIM CPF


        print("Excelente, seu CPF é válido!")

        system('cls')
        # VALIDADOR DE TEL
        while True:
            rLista.clear()  # sempre irá limpar a lista temporária no inicio do loop
            cadastro['telefone'] = str(input("Por favor digite seu telefone para contato com DDD: ")).strip()  # recebe os dados (telefone) como STR
            cadastro['telefone'] = cadastro['telefone'].replace('.', '')  # REMOÇÃO DE '.' , ' ' E '-' caso o usuário utilize
            cadastro['telefone'] = cadastro['telefone'].replace('-', '')
            cadastro['telefone'] = cadastro['telefone'].replace(' ', '')

            if len(cadastro['telefone']) != 11 or not cadastro['telefone'].isdecimal():  # se telefone for diferente de 11 e se não for decimal
                print('Digite um número válido!\n')  # Se digitar a quantidade de números errada. correto: 47 98888-7777

            else:
                rLista = list(cadastro['telefone'])  # Adiciona o telefone a uma lista ex: [3, 5, 6, 5, 8, 7, 8, 7, 9, 7, 0]
                rLista.insert(2, ' ')  # Insere o espaço apos o "codigo de area" ex: [3, 5, ' ', 6, 5, 8, 7, 8, 7, 9, 7, 0]
                rLista.insert(8, '-')  # Insere o "-" no meio do número ex: [3, 5, ' ', 6, 5, 8, 7, 8, '-', 7, 9, 7, 0]
                temporario = ''.join(rLista)  # Junta a lista novamente e passa ela para a variável ex: ['35 65878-7970]
                # print(cadastro['telefone'])  ** print p teste **
                cadastro['telefone'] = temporario  # ADICINANDO O NÚMERO PARA O DICIONÁRIO
                break
        # FIM VALIDADOR DE TELEFONE


    #MENU PRINCIPAL
    if id in 'simnaonão' :
        #GERADOR DE NÚMERO DE PROTOCOLO
        protocolo = [randint(1,9), randint(0,9), randint(0,9), randint(0,9),
                     randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
        anoProtocolo = date.today().year
        protocolostr = ""

        for c in range (0,len(protocolo)):
            protocolostr += str(protocolo[c])       # Transforma em str para ficar sem os [] da lista

        system('cls')
        while True:         # validador do menu
            system('cls')
            # se possuir algo em cadastro irá aparecer a opção de alterar dados
            print("O que você deseja fazer?\n"
                  " 1- Reclamação.\n", "2- Alteração de Dados.\n" if len(cadastro) !=0 else "")

            id = int(input("Por favor, digite o numero da opção escolhida: "))

            system('cls')

            if id == 3:     # SAIR
                break

            elif id == 1:     # RECLAMAÇÃO
                system('cls')
                reclamacao = str(input(f"A opção escolhida foi: {id}\nQual é a sua reclamação? "))
                print(f"{poli}")
                print(f"Obrigado(a) pelas informações fornecidas! O seu protocolo é o número {protocolostr}-{anoProtocolo}\n"
                      f"Iremos avaliar sua reclamação e entraremos em contato no telefone informado.")
                break


            elif id == 2 and len(cadastro) != 0:     # ALTERAR DADOS
                system('cls')
                poli = '=' * 70  # alterando o poliforfismo para criação de tabela
                print(poli)
                print(f'{" Banco de Dados ":^70}')
                print(poli)

                for k, v in cadastro.items():  # k = chave / v = value / items = itens
                    print(f' {k.title():.<8}{v.title():.>60}')

                print(poli)



                # irá entrar no while porque id será =2
                while id not in cadastro:       # irá ficar no loop até digitar a opção correta (nome, telefone, cpf)

                    id = str(input('Qual dados você gostaria de alterar? [Digite "SAIR" para voltar]: ')).strip().lower()

                    if id == 'telefone':

                        # VALIDADOR DE TEL
                        while True:
                                rLista.clear()  # sempre irá limpar a lista temporária no inicio do loop
                                cadastro['telefone'] = str(input("Digite a alteração em TELEFONE :")).strip()  # recebe os dados (telefone) como STR
                                cadastro['telefone'] = cadastro['telefone'].replace('.', '')  # REMOÇÃO DE '.' , ' ' E '-' caso o usuário utilize
                                cadastro['telefone'] = cadastro['telefone'].replace('-', '')
                                cadastro['telefone'] = cadastro['telefone'].replace(' ', '')

                                if len(cadastro['telefone']) != 11 or not cadastro['telefone'].isdecimal():  # se telefone for diferente de 11 e se não for decimal
                                    print('Digite um número válido!\n')  # Se digitar a quantidade de números errada. correto: 47 98888-7777

                                else:
                                    rLista = list(cadastro['telefone'])  # Adiciona o telefone a uma lista ex: [3, 5, 6, 5, 8, 7, 8, 7, 9, 7, 0]
                                    rLista.insert(2, ' ')  # Insere o espaço apos o "codigo de area" ex: [3, 5, ' ', 6, 5, 8, 7, 8, 7, 9, 7, 0]
                                    rLista.insert(8, '-')  # Insere o "-" no meio do número ex: [3, 5, ' ', 6, 5, 8, 7, 8, '-', 7, 9, 7, 0]
                                    temporario = ''.join(rLista)  # Junta a lista novamente e passa ela para a variável ex: ['35 65878-7970]
                                    # print(cadastro['telefone'])  ** print p teste **
                                    cadastro['telefone'] = temporario  # ADICINANDO O NÚMERO PARA O DICIONÁRIO
                                    break
                        # FIM VALIDADOR DE TELEFONE
                        # O CORRETO SERIA CRIAR UMA FUNÇÃO

                    elif id == 'cpf':
                        # VALIDADOR DE CPF
                        # CPF deve ser salvo como STR porque caso inicie com '0' irá dar erro ao salvar no dicionário

                        while True:
                                # VARIÁVEIS             # variáveis estão dentro do loop, porque elas precisam ter
                                decrescente = 10  # esses valores quando iniciarem novamente
                                posicao = 0
                                listaCPF.clear()  # limpa as listas no inicio do loop
                                rLista.clear()
                                listaInt.clear()

                                cadastro['cpf'] = str(input('Digite a alteração em CPF: ')).strip()  # remoção de espaços no inicio e fim da str
                                cadastro['cpf'] = cadastro['cpf'].replace('.', '')  # REMOÇÃO DE '.' E '-'
                                cadastro['cpf'] = cadastro['cpf'].replace('-', '')

                                if len(cadastro['cpf']) != 11 or not cadastro['cpf'].isdecimal() or len(
                                        set(cadastro['cpf'])) == 1:
                                    # IRÁ PROCEGUIR CASO PASSE A PRIMEIRA VALIDAÇÃO
                                    # se CPF for diferente de 11 e se não for decimal
                                    # SET() REMOVE OS ITENS DUPLICADOS ex:[1,2,2,2,2,1,1,1] = {1,2}
                                    print('Digite o CPF corretamente!\n')  # Se digitar a quantidade de números errada

                                else:
                                    listaCPF = list(cadastro['cpf'])  # CPF AINDA É UMA str e FOI FATIADO NA LISTA

                                    # PRIMEIRO DIGITO
                                    # PADRÃO
                                    """
                                    for c in range(0, len(listaCPF)):
                                        listaInt.append(int(listaCPF[c]))       # CPF NA LISTA INT
                                    """

                                    # LIST COMPREHENSION
                                    [listaInt.append(int(digito)) for digito in listaCPF]

                                    for c in range(10, 1, -1):
                                        """
                                        Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente
                                        de números de 10 à 2 e soma os resultados
                                        """
                                        rLista.append(listaInt[posicao] * c)  # c=10,9,8,7...  posicao=0,1,2,3,4...
                                        posicao += 1  # O RESULTADO ESTÁ SENDO ADICIONADO EM OUTRA LISTA COMO int
                                        # EU NÃO CONSEGUI FAZER ISSO SEM USAR DUAS LISTAS

                                    # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
                                    # Caso resto da divisão = 10, considerar = 0
                                    # Se o resultado for igual ao primeiro digito do cpf (posição 9), primeira parte da validação OK

                                    resultado = (sum(rLista) * 10) % 11  # sum(rLista) soma todos os elementos de rLista
                                    if resultado == 10:  # usar '0' para validação caso o resultado for 10
                                        resultado = 0

                                    if resultado == listaInt[-2]:  # IRÁ PROCEGUIR CASO PASSE A PRIMEIRA VALIDAÇÃO
                                        # SEGUNDO DIGITO
                                        # VARIÁVEIS
                                        decrescente = 10
                                        posicao = 0
                                        rLista.clear()  # LIMPA rLista

                                        for c in range(11, 1, -1):
                                            """
                                            Vamos multiplicar os 10 primeiros números (9 números + 1 digito verificador) pela 
                                            sequência decrescente de números de 11 à 2 
                                            """
                                            rLista.append(listaInt[posicao] * c)  # c=11,9,8,7...  posicao=0,1,2,3,4...
                                            posicao += 1  # O RESULTADO ESTÁ SEDO ADICIONADO EM OUTRA LISTA COMO int E NÃO MAIS str
                                            # EU NÃO CONSEGUI FAZER ISSO DE OUTRO JEITO

                                        # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
                                        # Caso resto da divisão = 10, considerar = 0
                                        # Se o resultado for igual ao primeiro digito do cpf (posição 10) , primeira parte da validação OK

                                        resultado = (sum(rLista) * 10) % 11
                                        if resultado == 10:  # usar '0' para validação caso o resultado for 10
                                            resultado = 0

                                        if resultado == listaInt[-1]:
                                            # print('CPF ok') print teste
                                            #       *** FAZER A ALTERAÇÃO OU CADASTRO DO CPF AQUI ***##
                                            listaCPF.insert(3,
                                                            '.')  # inserindo "." e "-" no cpf para melhor vizualização na biblioteca
                                            listaCPF.insert(7, '.')
                                            listaCPF.insert(11, '-')
                                            temporario = ''.join(
                                                listaCPF)  # Junta a lista novamente e passa ela para a variável
                                            cadastro['cpf'] = temporario  # ADICINANDO O NÚMERO PARA O DICIONÁRIO
                                            # print((cadastro['cpf']))       ** print teste **
                                            break
                                    else:
                                        print('CPF inválido!\n')
                        # FIM VALIDADOR DE TELEFONE
                        # O CORRETO SERIA CRIAR UMA FUNÇÃO

                    elif id == 'nome':
                        system('cls')
                        cadastro['nome'] = str(input("Digite o novo NOME: ")).strip().lower()

                    elif id =='sair':
                        system('cls')
                        break

                    else:
                        print("Opção Inválida.")


                # PRINT DO BANCO DE DADOS ALTERADO
                system('cls')
                print(poli)
                print(f'{" Banco de Dados ":^70}')
                print(poli)

                for k, v in enumerate(cadastro):
                    print(f' {v.title():.<8}{cadastro[v].title():.>60}')

                print(poli)
                time.sleep(5)  # irá ficar na tela durante 5 segundo e logo irá ao menu
                # Deseja finalizar o atendimento ou conversar com um atendente?"

        system('cls')
        #MENU DE FALAR COM ATENDENTE OU FINALIZAR ATENDIMENTO
        id = int(input("Deseja finalizar o atendimento ou conversar com um atendente? Escolha: \n"
                       "1- Finalizar atendimento.\n"
                       "2- Conversar com um atendente\n"))

        if id == 1: # finalizar atendimento
            break

        elif id == 2:    # se for escolhido falar com atendente, inicia o código
            system('cls')
            atendentes = ['Xuxa', 'Shakira', 'Faustão', 'Ana Maria Braga']

            for x in range(10, 0, -1):
                system('cls')

                print(f"\n{poli}\nSOLICITANDO AJUDA A UM DE NOSSOS ATENDENTES\n{poli}\n"
                      f"Você está na posição {x}\n*música de fundo*") #diz a posição
                time.sleep(randint(0,2)) #possui intervalo aleatório entre uma posição e outra

            system('cls')

            print('Erro no sistema!\nEstamos reiniciando...')

            time.sleep(3)

            for x in range(5, 0, -1): #a posição é aleatória entre 9 e 15
                system('cls')
                print(f"\n{poli}\nSOLICITANDO AJUDA A UM DE NOSSOS ATENDENTES\n{poli}\n"
                      f"Você está na posição {x}\n*música de fundo*")  # diz a posição

                time.sleep(randint(0, 2))  # possui intervalo aleatório entre uma posição e outra

                print(f'Você está na posição {x}\n*música de fundo*') #diz a posição

                time.sleep(randint(0,3)) #possui intervalo aleatório entre uma posição e outra

            system('cls')
            print("Atendente {} irá te recepcionar! Por favor aguarde.".format(choice(atendentes))) #um atendente aleatório da lista será chamados
            print('\n\n\n\nInicia a conversa com o atendente\n\n\n\n')

            time.sleep(5)
            system('cls')
            break

# FIM
system('cls')
poli = '=' * 40
print(f"{poli}")
print(f'{"Obrigada por ter nos escolhido!":^40}')  # ISSO FOI SÓ PRA TER ALGO NO FINAL DO MEU CÓDIGO E PODE SAIR.
print(f"{poli}")
