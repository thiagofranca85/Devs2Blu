class Conta:

    # __init__ construtor
    def __init__(self,numero,titular,saldo,limite):
        print(f"Imprimindo construtor {self}")
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite