from conta import Conta

class PessoaFisica(Conta):

    __segundo_titular = ''

    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__(123456, 5469, 'Conta Pessoa Fisica')
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial
        print("Passando pelo Construtor da Classe Pessoa Fisica")

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular:str):
        self.__titular = titular.title()

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, titular):
        self.__segundo_titular = titular

    def __str__(self):
        return f"{super().__str__()}\nTitular: {self.titular}\nCPF: {self.cpf}\nSaldo Inicial: {self.saldo_inicial}\nSegundo Titular: {self.segundo_titular}"