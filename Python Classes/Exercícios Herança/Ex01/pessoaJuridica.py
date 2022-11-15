from conta import Conta

class PessoaJuridica(Conta):

    __segundo_titular = ''
    
    def __init__(self, titular, cnpj, saldo_inicial):
        super().__init__('456', 'Conta Pessoa Juridica')
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo_inicial = saldo_inicial
        print("Construtor da Classe Pessoa Juridica")

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, titular):
        self.__segundo_titular = titular

    def __str__(self):
        return f'{super().__str__()}\nTitular: {self.__titular}\nCNPJ: {self.__cnpj}\nSaldo Inicial: {self.__saldo_inicial}\nSegundo Titular: {self.segundo_titular}'