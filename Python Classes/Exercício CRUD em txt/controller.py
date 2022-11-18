from conta import Conta

def create(conta):
    # Criando / Escrevendo o Arquivo txt 
    contas = open('contas.txt', 'a') 
    contas.write(str(conta)+'\n')
    contas.close

def read():
    lista_contas = []
    contas = open('contas.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')

        # print(conta_objeto)

        conta = Conta()
        conta.titular = conta_objeto[0]
        conta.numero = conta_objeto[1]
        conta.saldo = conta_objeto[2]
        lista_contas.append(conta)
    contas.close()
    return lista_contas
