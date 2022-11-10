class Conta:

    def __init__(self, titular, numero, saldo, limite):
        
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        return f'Nr Conta: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}'

    def depositar(self, valor):
        self.saldo += valor
        return valor

    def sacar(self, valor):
        self.saldo -= valor
        return valor

    def transferir(self, valor, origem, destino):
        if (origem.saldo - valor) < 0:
            print("Saldo Insuficiente")
            return False
        else:
            origem.sacar(valor)
            destino.depositar(valor)
            print("Transferencia Efetuada com sucesso.")
            return valor
