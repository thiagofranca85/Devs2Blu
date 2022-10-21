import datetime
from time import sleep

hospedes = []

def saudacao():
    horaAtual = datetime.datetime.now()
    diaAtual = horaAtual.strftime("%d/%m/%Y")

    if horaAtual.hour < 12:
        print(f"Bom Dia !!! Bem vindo ao Hotel.\nData: {diaAtual}\nHora: {horaAtual.hour}:{horaAtual.minute}")
    elif horaAtual.hour < 18:
        print(f"Boa Tarde !!! Bem vindo ao Hotel.\nData: {diaAtual}\nHora: {horaAtual.hour}:{horaAtual.minute}")
    else:
        print(f"Boa Noite !!! Bem vindo ao Hotel.\nData: {diaAtual}\nHora: {horaAtual.hour}:{horaAtual.minute}")

def salvarHospede(dados):
    with open('hospedes.txt', 'a') as hospede:
        hospede.write(str(hospedes))

def listarHospede():
    nomes = []
    with open('hospedes.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes

def checkin():
    print("===")
    nome = input("Nome do Hospede: ").title()
    while True:
        telefone = input("Telefone: ")
        if not(telefone.isnumeric()):
            print("Digite um telefone valido.")
        else:
            break
    while True:
        varcpf = input("CPF: ")
        
        hasError = False
        # Limpa o cpf, retira pontos traços e tudo que não seja um número
        cpf = [int(char) for char in varcpf if char.isdigit()]        

        # verifica se o tamanho está correto
        if len(cpf) != 11:
            hasError = True

        if not(hasError):
            for i in range(9, 11):
                value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
                digit = ((value * 10) % 11) % 10
                if digit != cpf[i]:
                    hasError = True
            
        if hasError:
            print(f"CPF inválido!")
        else: 
            dados = {
                'nome': nome, 
                'telefone': telefone,
                'cpf': varcpf
            }
            hospedes.append(dados)
            salvarHospede(hospedes) 
            print(f"Hospede cadastrado com sucesso")
            break