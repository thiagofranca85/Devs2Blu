# importação do pacote os
import os
# importação das funções do controller
from controller import LerArquivo, SetChave, GerarDicio, criptografar, descriptografar, GravarArquivo
# constante que indica os caracteres permitidos de usar na mensagem
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.?ãÃõÕÉé"

# função que faz o tratamento da opção de criptografar
def tratarOpcao1():
    # chama a função SetChave
    chave = SetChave()
    # chama a função GerarDicio
    dicio = GerarDicio(CARACTERES)
    # recebe a mensagem
    mensagem = str(input('Digite sua Mensagem: '))
    # separa a mensagem e a envia para a criptografia
    mensagemCriptografada = criptografar(mensagem.split('\\n'), dicio)
    # grava a mensagem no arquivo
    GravarArquivo(mensagemCriptografada)
    # mostra a chave gerada na criptografia
    os.system("cls")
    print(f'Sua chave de acesso é: {chave}')

# função que trata a opção de descriptografar
def tratarOpcao2():
    # cria uma criavel que guardará o caminho para o arquivo
    arquivo = ''
    # enquanto o caminho digitado não existir, continua a perguntar
    while not(os.path.isfile(arquivo)):
        # recebe o caminho do arquivo   
        arquivo = input('Digite o nome do arquivo (Ex: arquivo.txt): ')
    
    # recebe a chave de decodificação
    SetChave(int(input('Digite sua chave: ')))

    # gera o dicionário de caracteres
    dicio = GerarDicio(CARACTERES)
    
    os.system("cls") # limpa o console
    # print pra bonito
    print('='*10, 'MENSAGEM DESCRIPTOGRAFADA', '='*10)
    # chama a função de ler arquivo, descriptografar e printa a mensagem descriptografada
    print(descriptografar(LerArquivo(arquivo), dicio))

# função que mostra o menu
def Menu():
    # while infinito
    while True:
        # print pra bonito
        print('='*10, 'CRIPTOGRAFIA BOLADONA', '='*10)
        # recebe a opção do usuário
        opcao = input("1 - Criptografar mensagem\n2 - Descriptografar mensagem\n3 - Sair\n:> ")
        
        # verifica a opção escolhida
        match opcao:
            case "1":
                tratarOpcao1()

            case "2":
                tratarOpcao2()

            case "3":
                print("Obrigado por utilizar nosso código ;)")
                break

            case _:
                os.system("cls") # limpa o console
                print("Função inválida!!")
