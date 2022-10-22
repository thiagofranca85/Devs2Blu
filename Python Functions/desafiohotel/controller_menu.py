import datetime
import os
from time import sleep

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
        hospede.write(f"{str(dados)}\n")

def listarHospede():
    with open('hospedes.txt') as arquivo:
        # print(arquivo.read())
        for number, line in enumerate(arquivo):
            print(number+1, line)

def procurarHospedes(hospedeFind):
    index=0
    flag=0
    arquivo = open("hospedes.txt", "r")

    for line in arquivo:
        index +=1
        if hospedeFind == eval(line)['nome']:
            print(line)
            flag=1
        if flag == 0:
            print("Hospede não encontrado.")


def checkout(HospedeCheckout):
    index=0
    flag=0
    arquivo = open('hospedes.txt', 'r')

    for line in arquivo:
        index += 1
        if HospedeCheckout == eval(line)['nome']:
            chave = index
            flag = 1
        if flag == 0:
            print("Cliente não encontrado.")
        arquivo.close()