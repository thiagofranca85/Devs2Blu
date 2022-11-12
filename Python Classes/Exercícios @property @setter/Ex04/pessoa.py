class Pessoa:

    # Construtor
    def __init__(self, nome, cpf, idade, altura):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__altura = altura

    # Getters and Setters
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    # Método str
    def __str__(self):
        return f"{self.nome} - {self.cpf} - {self.idade} - {self.altura}"