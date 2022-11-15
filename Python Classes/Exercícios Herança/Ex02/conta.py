class Conta:

    def __init__(self, numero, agencia, tipo):
        self.__numero = numero
        self.__agencia = agencia
        self.__tipo = tipo
        print("Passando pelo Construtor da Classe Conta")
    
    def __str__(self):
        return f'Numero: {self.__numero}\nAgencia: {self.__agencia}\nTipo: {self.__tipo}'