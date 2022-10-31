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
    
def entrada():
    os.system('cls')
    dados = dict()
    dados['placa'] = str(input("Placa do Veículo: ")).upper().strip()
    dados['modelo'] = str(input("Marca/Modelo: ")).upper().strip()
    dados['cor'] = str(input("Cor do veículo: ")).upper().strip()
    # Input de Hora e Minutos pra Hora de Entrada
    EntradaHora = int(input("Digite a hora de entrada: "))
    EntradaMinuto = int(input("E os minutos: "))
    # Salva o Horário de Entrada em Horas e Minutos
    horaEntrada = datetime.combine(date.today(), time(EntradaHora, EntradaMinuto)) 
    dados['entrada'] = horaEntrada
    carro = list()
    carro.append(dados.copy())
    print(carro)
    
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
        if placa == eval(linha)['placa']:
            # Aqui salvar o valor de entrada "datetime" como objeto pra poder fazer o calculo com a horaSaidaAtual no while seguinte.
            # >> horaEntrada = datetime.eval(linha)['entrada']
            placaEncontrada = True
            relatorio = linha # Customizar informações (Essa linha adiciona é pra customizar o TXT depois com o Nested Replace)
            print(relatorio)

        # Se não encontrar a placa mostra a mensagem abaixo
        if placaEncontrada == False:
            print("PLACA NÃO ENCONTRADA.")

    while True:
        opcao = input("[1] Efetuar Pagamento\n[2] Voltar ao Menu")
        horaSaidaAtual = datetime.combine(date.today(), time(horaAtual.hour, horaAtual.minute))

        match opcao:
            case '1':
                print("Opção de saída")
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

