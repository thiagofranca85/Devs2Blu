from model.pessoaFisica import PessoaFisica

def create_psf(conta):
    contas = open('pessoafisica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def read_psf():
    lista_contas = []
    contas = open('pessoafisica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        print(conta_objeto)

        conta = PessoaFisica()
        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cpf = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        lista_contas.append(conta)
    contas.close()
    return lista_contas