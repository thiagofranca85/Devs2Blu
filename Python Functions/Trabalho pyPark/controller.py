from datetime import datetime, date, time
import os

# Pega Data e Horário Atual do Sistema
horaAtual = datetime.now()

def disponivel():
    # Le o arquivo estacionamento.
    os.system('cls')
    with open('estacionamento.txt') as file:
        lines = file.readlines()
    
    # Estipulamos que o estacionamento teria 10 vagas, então se o len for maior que 10 ele nao aceita..
    # ..novos cadastros
    if len(lines)<10:
        pass
    else:
        print("Não há vagas disponíveis no momento!")
    print(f"Existem vagas disponíveis")
    
    # Salva os dados em um dicionario dentro do arquivo txt.
def entrada(carro):
    with open('estacionamento.txt', 'a') as arquivo:
        arquivo.write(str(carro)+"\n")

    # Exibe uma tabela simples de preços usando print.
def tabelaPrecos():
    os.system('cls')
    print(f"\n{'*'*10} Tabela de Preços {'*'*10}\n\t1a e 2a Horas = R$5\n\tHoras Adicionais = R$2\n")

    # Função de saída / Efetuar pagamento
def saida(placa):

    # Abre o arquivo do estacionamento
    arquivo = open('estacionamento.txt')

    # Variavel de controle caso nao exista um carro com a placa específica
    placaEncontrada = False
    # Verifica se existe a placa no estacionamento e mostra os dados do veiculo
    for linha in arquivo:
        aux = eval(linha)

        if placa == aux['placa']:
            # Ao encontrar a placa exibe as todas informaçoes do carro
            # Salva entradaHora e entradaMinuto como valores inteiros que serão usadas ..
            # .. para o calculo de tempo posteriormente.
            entradaHora = aux['entradaHora']
            entradaMinuto = aux['entradaMinuto']          
            placaEncontrada = True
            # Hora de entrada vinda do txt pelas chaves acima
            horaEntrada = datetime.combine(date.today(), time(entradaHora, entradaMinuto))
            relatorio = linha # Customizar informações (Essa linha adiciona é pra customizar o TXT depois com o Nested Replace)
            print(relatorio)
        
        # Se não encontrar a placa mostra a mensagem abaixo
        if placaEncontrada == False:
            print("PLACA NÃO ENCONTRADA.")
            break
    
    while True:
        # Salva o Horário de Saída em Horas e Minutos usando o horaAtual.hour e horaAtual.minute como parametros.
        horaSaidaAtual = datetime.combine(date.today(), time(horaAtual.hour, horaAtual.minute)) 
      
        # Opção para efetuar o pagamento e sair ou voltar ao menu.
        opcao = input("[1] Efetuar Pagamento\n[2] Voltar ao Menu\n>> ")

        match opcao:
            case '1':
                # Calcula a hora de saída.
                horaSaida = horaSaidaAtual - horaEntrada

                # Transforma as horas em um numero float através dos segundos pra calcular o valor a pagar
                calcHora = (horaSaida.seconds/60)/60 

                # Calcula o valor das horas e exibe valor e tempo estacionando
                valor = 0
                if calcHora < 1:
                    valor = 5
                    print(f"\nO carro ficou estacionado por {horaSaida.seconds/60} minutos.")
                elif calcHora < 2:
                    valor = 10
                    print(f"\nO carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} hora(s).")
                elif calcHora > 2:
                    valor = ((round(calcHora) * 2) - 4) + 10
                    print(f"\nO carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} horas.")
                
                print(f"\nValor R${valor:.2f}")


                #variavel criada recebendo valor inteiro 
                index=0

                #variavel criada recebendo valor inteiro 
                flag=0

                #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
                arquivo = open("estacionamento.txt", "r") 

                #estrutura repeticao recebendo uma variavel line para ler o arquivo(txt)
                for line in arquivo:

                    #variavel index recebendo operador relacional de incremento
                    index +=1

                    #if condicional recebendo o clinteFind, que é o atributo principal da funcao,
                    # que recebe funcao interna do python eval(), permitindo assim manipular a linha atravez da chave condicional nome, ultilindo o meu dicionario inserido como um objeto
                    if placa == eval(line)['placa']:

                        #Variavel chave criada recebendo incremento do indice atraves da variavel index
                        chave = index

                        #variavel flag recendo incremento do dicionario

                        flag =1

                #variavel arquivo que representa arquivo txt recebendo funcao internalizada do python.        
                #close() fecha o arquivo aberto. Um arquivo fechado não pode mais ser lido ou escrito
                arquivo.close()

                # condional da variavel flag atribuindo atraves de operador relacional condicao de cliente nao encontrado 
                if flag == 0:
                    pass

                #condicional else, se nenhuma das condicoes estiverem nas condicionais acima o programa irá entra nesta condiçao
                else:

                    #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
                    with open('estacionamento.txt', 'r') as arquivo:

                        # variavel lines criada, recebendo a variavel que representa o caminho do txt.
                        # funcao readlines() Retorna todas as linhas do arquivo, como uma lista onde cada linha é um item  objeto de lista:
                        lines = arquivo.readlines()
                            
                        #Variavel criada recebendo valor inteiro igual a 1
                        posicao = 1
                
                        #funcao open recebendo  o caminho do arquivo, variavel referencia  arquivo txt letra(w) tem a funcao de escrever no arquivo
                        with open('estacionamento.txt', 'w') as arquivo:

                            #estrutura de repeticao com variavel criada lendo as linhas atraves da chave do dicionario
                            for line in lines:
                                # condicao if se a posicao for diferente da chave
                                if posicao != chave:

                                    #variavel arquivo recebendo a funcao escrita, ira percorrer linha a linha identificando se o valor digitado contem na lista
                                    arquivo.write(line)

                                #variavel posicao incrementando, se o valor da chave que foi digitado  o cliente é deletado
                                posicao += 1

                        #Print de saida do bloco           
                        print("Estacionamento Finalizado\n")
                break
            case '2':
                break
            case _:
                print("Digite uma opção valida")     

