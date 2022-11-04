#importando as bibliotecas
from datetime import datetime
import os

#criando a funcao saudação
def saudacao():
    
    # criando uma variavel recebendo a hora atual
    hora = datetime.today().strftime('%H:%M')
    saudacao = ''
    # condicao de verificao da saudacao do dia
    if hora > ('06:00') and hora < ('12:00'):
        saudacao = 'Bom dia!'
    elif hora > ('12:00') and hora < ('18:00'):
        saudacao = 'Boa tarde!'
    else: 
        saudacao = 'Boa noite!'

    # printando a hora e saudação
    print(hora, '\n')
    print('Boa Noite! Seja bem vindo ao Cinema Pytrix\n'.format(saudacao))    

#Funcao limpar arquivo
def limparticket():
    with open('registro_cliente.txt', 'w') as arquivo:
        arquivo.write(str(""))

# funcao de  salvar o cliente no arquivo txt
def cadastrarcliente(cliente):
    with open('registro_cliente.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+'\n')

#Função Salvarfilme
def salvarfilme(filme):
    with open('registro_cliente.txt', 'a') as arquivo:
        arquivo.write(str(filme)+'\n')

#Função Salvar Poltrona
def salvarpoltrona(poltrona):
    with open('registro_cliente.txt', 'a') as arquivo:
        arquivo.write(str(poltrona)+'\n')        
        
# Função para registrar a escolha da bomboniere
def salvar_itens(bomboniere):
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "a") as arquivo:
        # Salva o Dicionário do arquivo
        arquivo.write(f"{bomboniere}\n")

# Função para registrar a forma de pagamento
def salvar_pagamento(forma_pagamento):
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "a") as arquivo:
        # Salva o Dicionário do arquivo
        arquivo.write(f"{forma_pagamento}\n")

# Função para impressão do ticket do cliente 
def ticket():
    # Abre o arquivo .txt
    with open("registro_cliente.txt", "r") as arquivo:
        # Percorre as linhas do arquivo
        for linha in arquivo:
            # Transforma cada linha em um Dicionário
            dicio = eval(linha)
            # Percorre o Dicionário
            for chave, valor in dicio.items():
                # Verifica se é a primeira chave de cada Dicionário
                if chave == "Nome":
                    # Imprime a Label Premium   
                    print('\n- Cliente Premium\n')
                # Verifica se é a primeira chave de cada Dicionário
                if chave == 'Filme':
                    # Imprime a Label Filme  
                    print('\n- Filme Escolhido\n')    
                # Verifica se é a primeira chave de cada Dicionário
                if chave == 'Poltrona':
                    # Imprime a Label Poltrona
                    print('\n- Poltrona escolhida\n')    
                # Verifica se é a primeira chave de cada Dicionário
                if chave == "Pipoca":
                    # Imprime a Label Bomboniere
                    print("\n- Bomboniere\n")
                # Verifica se é a primeira chave de cada Dicionário
                if chave == "Pagamento":
                    # Imprime a Label Forma de pagamento
                    print("\n- Forma de pagamento\n")
                # Imprime as Chaves e Valores do Dicionário
                print(f"   * {chave} ----- {valor}")

        # Imprime a saudação final
        print("\n", "-" * 5, "Volte Sempre", "-" * 5)