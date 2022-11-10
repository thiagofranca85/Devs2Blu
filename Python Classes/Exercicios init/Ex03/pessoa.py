class Pessoa:

    def __init__(self,nome,sobreNome,idade,cpf):
        print(f"Imprimindo construtor {self}")

        self.nome = nome
        self.sobreNome = sobreNome
        self.idade = idade
        self.cpf = cpf