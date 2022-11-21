from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.fisico import create_psf, read_psf, update_psf, delete_psf
from controller.juridico import create_pj, read_pj, update_pj, delete_pj

def menu():
    menu = 1

    while menu != 0:
        print("Digite a Opção Desejada")

        menu_inicial = int(input("[1]Pessoa Fisica\n[2]Pessoa Juridica\n[3]Sair do Programa\n>> "))

        match menu_inicial:
            case 1:
                menu = int(input('[1]Criar Conta PF\n[2]Listar Contas Pessoa Fisica\n[3]Alterar Titular/CPF/Saldo\n[4]Deletar Conta pelo Titular\n>> '))
                match menu:
                    case 1:
                        conta = PessoaFisica()
                        conta.titular = input('Nome do Titular: ')
                        conta.cpf = input('Digite o CPF: ')
                        conta.saldo_inicial = input('Qual o Saldo Inicial: ')
                        segundo_titular = input("Deseja cadastrar o Segundo Titular? [SIM/NAO]").upper()
                        if segundo_titular == 'SIM':
                            conta.segundo_titular = input('Qual o nome do Segundo Titular: ')
                        create_psf(conta)

                    case 2:
                        read_psf()

                    case 3:
                        altera_titular = input("Altere o nome do Titular\n>> ")
                        update_psf(altera_titular)

                    case 4:
                        titular_deleta = input("Digite o Titular para deletar a Conta\n>> ")
                        delete_psf(titular_deleta)

                    case _:
                        print('Opção Inválida. Retornando ao Menu Inicial.')

            case 2:
                menu = int(input('[1]Criar Conta PJ\n[2]Listar Contas Pessoa Juridica\n[3]Alterar Titular/CPF/Saldo\n[4]Deletar Conta pelo Titular\n>> >> '))
                match menu:
                    case 1:
                        conta = PessoaJuridica()
                        conta.titular = input('Nome do Titular: ')
                        conta.cnpj = input('Digite o CNPJ: ')
                        conta.saldo_inicial = input('Qual o Saldo Inicial: ')
                        segundo_titular = input("Deseja cadastrar o Segundo Titular? [SIM/NAO]").upper()
                        if segundo_titular == 'SIM':
                            conta.segundo_titular = input('Qual o nome do Segundo Titular: ')
                        create_pj(conta)

                    case 2:
                        read_pj()

                    case 3:
                        altera_titular = input("Altere o nome do Titular\n>> ")
                        update_pj(altera_titular)

                    case 4:
                        titular_deleta = input("Digite o Titular para deletar a Conta\n>> ")
                        delete_pj(titular_deleta)

                    case _:
                        print('Opção Inválida. Retornando ao Menu Inicial.')

            case 3:
                break
            case _:
                print('Digite uma Opção Válida.')

                        


