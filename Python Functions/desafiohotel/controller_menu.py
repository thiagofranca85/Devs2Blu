import datetime
import os
from time import sleep
from itertools import islice

def saudacao():
    horaAtual = datetime.datetime.now()
    diaAtual = horaAtual.strftime("%d/%m/%Y")

    if horaAtual.hour < 6:
        print(f"Boa Noite !!! Bem vindo ao Hotel.\nData: {diaAtual}\nHora: {horaAtual.hour}:{horaAtual.minute}")
    elif horaAtual.hour < 12:
        print(f"Bom Dia !!! Bem vindo ao Hotel.\nData: {diaAtual}\nHora: {horaAtual.hour}:{horaAtual.minute}")
    elif horaAtual.hour < 18:
        print(f"Boa Tarde !!! Bem vindo ao Hotel.\nData: {diaAtual}\nHora: {horaAtual.hour}:{horaAtual.minute}")

def salvarHospede(dados):
    with open('hospedes.txt', 'a') as hospede:
        hospede.write(f"{str(dados)}\n")

def listarHospede():
    os.system('cls')
    with open('hospedes.txt') as arquivo:
        # print(arquivo.read())
        print("\n*** Lista de Hospedes ***\n")
        for number, line in enumerate(arquivo):
            print(number + 1, line)


def procurarHospedes(hospedeFind):
    os.system('cls')
    arquivo = open('hospedes.txt', 'r')

    hospedeEncontrado = False
    for linha in arquivo:
        if hospedeFind == eval(linha)['nome']:
            hospedeEncontrado = True
            print(f"\n{linha}")
    
    if hospedeEncontrado == False:
        print("\nNão existe Hospede registrado com esse nome.\n")

def checkout(HospedeCheckout):
    os.system('cls')
    with open('hospedes.txt') as file:
        lines = file.readlines()

    if(HospedeCheckout <= len(lines)):
        del lines[HospedeCheckout - 1]

        with open('hospedes.txt', "w") as file:
            for line in lines:
                file.write(line)
    else:
        print(f"\nNão existe um hospede com este índice > {HospedeCheckout} <\n")


# Guia usado pra fazer o checkout
# def delete_line(filename, line_number):

#     with open(filename) as file:
#         lines = file.readlines()

#     if(line_number <= len(lines)):
#         del lines[line_number - 1]

#         with open(filename, "w") as file:
#             for line in lines:
#                 file.write(line)
#     else:
#         print(f"Não existe um hospede com este índice. {line_number}")

#     print(lines)

#     delete_filename = input("File: ")
#     delete_line_number = int(input("Line: "))
#     print(f"Atualmente temos {len(lines)} hospedados.")

# delete_line(delete_filename, delete_line_number)