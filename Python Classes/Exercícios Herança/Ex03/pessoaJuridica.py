from conta import Conta

class PessoaJuridica(Conta):

    __segundo_titular = ''

    def __init__(self, titular, cnpj, saldo_inicial):
        super().__init__(789456, 1212, 'Conta Pessoa Juridica')
        self.titular = titular
        self.cnpj = cnpj
        self.saldo_inicial = saldo_inicial

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular:str):
        self.__titular = titular.title()

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

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
        return f"{super().__str__()}\nTitular: {self.titular}\nCNPJ: {self.cnpj}\nSaldo Inicial: {self.saldo_inicial}\nSegundo Titular: {self.segundo_titular}"