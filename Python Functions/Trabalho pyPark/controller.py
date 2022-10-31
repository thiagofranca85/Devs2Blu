from datetime import datetime, date, time
import os

# Pega Data e Horário Atual do Sistema
horaAtual = datetime.now()

def disponivel():
    os.system('cls')
    with open('estacionamento.txt') as file:
        lines = file.readlines()
    
    if len(lines)<10:
        pass
    else:
        print("Não há vagas disponíveis no momento!")
    print(f"Existem vagas disponíveis")
    
def entrada(carro):
    with open('estacionamento.txt', 'a') as arquivo:
        arquivo.write(str(carro)+"\n")

def tabelaPrecos():
    os.system('cls')
    print(f"\n{'*'*10} Tabela de Preços {'*'*10}\n\t1a e 2a Horas = R$5\n\tHoras Adicionais = R$2\n")

def saida(placa):
    arquivo = open('estacionamento.txt')

    placaEncontrada = False
    # Verifica se existe a placa no estacionamento e mostra os dados do veiculo
    for linha in arquivo:
        aux = eval(linha)

        if placa == aux['placa']:
            entradaHora = aux['entradaHora']
            entradaMinuto = aux['entradaMinuto']          
            placaEncontrada = True
            relatorio = linha # Customizar informações (Essa linha adiciona é pra customizar o TXT depois com o Nested Replace)
            print(relatorio)
        
        # Se não encontrar a placa mostra a mensagem abaixo
        if placaEncontrada == False:
            print("PLACA NÃO ENCONTRADA.")

    while True:
        # Hora de entrada vinda do txt pelas chaves acima
        horaEntrada = datetime.combine(date.today(), time(entradaHora, entradaMinuto))
        # Salva o Horário de Saída em Horas e Minutos usando o horaAtual.hour e horaAtual.minute como parametros.
        horaSaidaAtual = datetime.combine(date.today(), time(horaAtual.hour, horaAtual.minute)) 
      
        opcao = input("[1] Efetuar Pagamento\n[2] Voltar ao Menu\n>> ")

        match opcao:
            case '1':
                horaSaida = horaSaidaAtual - horaEntrada
                # Transforma as horas em um numero float através dos segundos pra calcular o valor a pagar
                calcHora = (horaSaida.seconds/60)/60 

                valor = 0
                if calcHora < 1:
                    valor = 5
                    print(f"O carro ficou estacionado por {horaSaida.seconds/60} minutos.")
                elif calcHora < 2:
                    valor = 10
                    print(f"O carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} hora(s).")
                elif calcHora > 2:
                    valor = ((round(calcHora) * 2) - 4) + 10
                    print(f"O carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} horas.")
                
                print(f"Valor R${valor:.2f}")
                # Caixa (valor)
                
                with open('estacionamento.txt') as file:
                    lines = file.readlines()

                if(placa <= len(lines)):
                    del lines[placa]

                    with open('estacionamento.txt', "w") as file:
                        for line in lines:
                            file.write(line)
            case '2':
                break
            case _:
                print("Digite uma opção valida")
                




            # with open('estacionamento.txt') as arquivo:
            #     linhas = arquivo.readlines()

            # if placa == eval(linha)['placa']:
            #     del linhas['placa']
            
            # with open('estacionamento.txt', 'w') as arquivo:
            #     for linha in linhas:
            #         arquivo.write(linha)        

