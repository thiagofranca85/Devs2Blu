from conta import Conta

def criaConta():
    titular = input("Titular: ")
    numero = input("Numero: ")
    saldo = input("Saldo: ")
    limite = input("Limite: ")
    return Conta(titular, numero, saldo, limite)

conta1 = criaConta()
print(f"{conta1.titular} - {conta1.numero} - {conta1.saldo}")

conta2 = criaConta()
print(f"{conta2.titular} - {conta2.numero} - {conta2.saldo}")

