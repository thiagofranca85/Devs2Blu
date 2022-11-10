from conta import Conta

print("\nCONTA 1")
conta1 = Conta(input("Digite um titular: "),int(input("Nr da Conta: ")),float(input("Digite o saldo: ")),float(input("Digite o limite: ")))

print("\n*EXTRATO*")
print(conta1.extrato())

print("\n*DEPOSITAR*")
valor = conta1.depositar(float(input("Digite o valor do DEPOSITO: ")))
print(f"O valor do deposito foi {valor}, o saldo atual é {conta1.saldo}")

print("\n*SACAR*")
valor = conta1.sacar(float(input("Digite o valor do SAQUE: ")))
print(f"O valor do saque foi {valor}, o saldo atual é {conta1.saldo}")

print("\nCONTA 2")
conta2 = Conta(input("Digite um titular: "),int(input("Nr da Conta: ")),float(input("Digite o saldo: ")),float(input("Digite o limite: ")))

print("\nTRANSFERENCIA CONTA 2 PARA CONTA 1")
valor = conta2.transferir(float(input("Digite o valor de TRANSFERENCIA: ")),conta2,conta1)
if valor:
    print(f"O valor de transferencia foi {valor}.")

print("\n*EXTRATO*")
print(conta1.extrato())

print("\n*EXTRATO*")
print(conta2.extrato())

