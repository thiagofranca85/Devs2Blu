from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):
    contas = open('pessoajuridica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def read_pj():
    lista_contas = []
    contas = open('pessoajuridica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        print(conta_objeto)

        conta = PessoaJuridica()
        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cnpj = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        lista_contas.append(conta)
    contas.close()
    return lista_contas

def update_pj(nome):
    conta_update = PessoaJuridica()
    conta_update.titular = input('Nome do Titular: ')
    conta_update.cpf = input('Digite o CPF: ')
    conta_update.saldo_inicial = input('Qual o Saldo Inicial: ')
    segundo_titular = input("Deseja cadastrar o Segundo Titular? [SIM/NAO]").upper()
    if segundo_titular == 'SIM':
        conta.segundo_titular = input('Qual o nome do Segundo Titular: ')

    lista_contas = []
    contas = open('pessoajuridica.txt', 'r')
    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')

        if nome == conta_objeto[2]:
            lista_contas.append(str(conta_update)+'\n')
        else:
            lista_contas.append(conta)
    contas.close()
    contas = open('pessoajuridica.txt', 'w')
    contas.writelines(lista_contas)
    contas.close()

def delete_pj(titular_conta):
    lista_contas = []
    contas = open('pessoajuridica.txt', 'r')
    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')

        if titular_conta == conta_objeto[2]:
            pass
        else:
            lista_contas.append(conta)
    contas.close()
    contas = open('pessoajuridica.txt', 'w')
    contas.writelines(lista_contas)
    contas.close()