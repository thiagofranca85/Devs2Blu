from datetime import datetime, date, time
import os

    # Salva os dados em um dicionario dentro do arquivo txt.
def entrada(carro):
    with open('estacionamento.txt', 'a') as arquivo:
        arquivo.write(str(carro)+"\n")

    # Exibe uma tabela simples de preços usando print.
def tabelaPrecos():
    os.system('cls')
    print(f"{'*'*10} Tabela de Preços {'*'*10}\n\t1a e 2a Horas = R$5\n\tHoras Adicionais = R$2\n")

    # Função de saída / Verificar placa e pegar valores que serao usados no calculo do pagamento
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
            # Salva entradaHora e entradaMinuto como valores inteiros que serão usados ..
            # .. para o calculo de tempo posteriormente.
            entradaHora = aux['entradaHora']
            entradaMinuto = aux['entradaMinuto']          
            placaEncontrada = True
            # Hora de entrada vinda do txt pelas chaves acima >> entradaHora entradaMinuto
            horaEntrada = datetime.combine(date.today(), time(entradaHora, entradaMinuto))
            # Alterando as informações da linha txt usando NESTED Replace
            print()
            relatorio = linha.replace("{'placa':","Placa:").replace("'","").replace("modelo:","Modelo:").replace("cor:","Cor:").replace("entradaHora:","Hora Entrada >").replace(", entradaMinuto:"," :").replace("}","")
            print(relatorio)
            # Passando a placa e a horaEntrada como Parametros pra função saidaPagamento()
            saidaPagamento(placa, horaEntrada)
        
    # Se não encontrar a placa mostra a mensagem abaixo e volta para o menu
    if placaEncontrada == False:
        print("\nPLACA NÃO ENCONTRADA.\n")

    # Função de pagamento / Pegando a placa(chave) e a horaEntrada caso a placa seja encontrada como parametros.
def saidaPagamento(placa, horaEntrada):    
    while True:

        # Pega Data e Horário Atual do Sistema
        horaAtual = datetime.now()
        print(horaAtual)

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
                
                # Imprime o valor do estacionamento
                print(f"\nValor R${valor:.2f}")

                # Agora vem os comandos pra salvar o index e deletar a linha da placa ao efetuar o pagamento
                # Abre o arquivo estacionamento
                arquivo = open('estacionamento.txt')

                # Variavel pra salvar o index que sera salvo a seguir
                index = 0

                # Aqui procura a placa pela chave e salva o indice da linha encontrada como placaDelete recebendo index
                for linha in arquivo:
                    aux = eval(linha)

                    index += 1
                    
                    if placa == aux['placa']:
                        placaDelete = index
                
                # Agora que encontramos a pladaDelete fechamos o arquivo.
                arquivo.close()

                # Abrindo novamente o arquivo, agora usando o with open e salvando as linhas com readlines()
                with open('estacionamento.txt', 'r') as arquivo:
                    linhas = arquivo.readlines()

                    # Reabrindo o arquivo agora com o parametro w para re-escrever o txt
                    with open('estacionamento.txt', 'w') as arquivo:

                        # Variavel criada recebendo valor inteiro igual a 1
                        posicao = 1
                        # Estrutura de repetião lendo linhas do arquivo txt
                        for linha in linhas:
                            # condicao if se a posicao for diferente da chave
                            if posicao != placaDelete:

                                # Se a posicao for diferente do indice da placaDelete ele re-escreve o arquivo
                                arquivo.write(linha)
                            # Incremento da variavel posicao dentro do FOR
                            posicao += 1

                    #Print de saida do bloco           
                    print("Estacionamento Finalizado.\n")
                    break
            case '2':
                break
            case _:
                print("Selecione uma opção válida.")
