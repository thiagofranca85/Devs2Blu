class Conta:

    def __init__(self, numero, agencia, tipo):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        print("Passando pelo Construtor da Classe Conta")
    
    def __str__(self):
        return f'Numero: {self.numero}\nAgencia: {self.agencia}\nTipo: {self.tipo}'