from conta import Conta
from controller import create, read

def menu():

    conta = Conta()
    conta.titular = 'Thiago'
    conta.numero = 123
    conta.saldo = 50000
    create(conta)

    lista_contas = read()

    for c in lista_contas:
        print(c)

menu()