class Animal:

    def __init__(self,especie,genero,idade,cor):
        print(f"Imprimindo construtor {self}")

        self.especie = especie
        self.genero = genero
        self.idade = idade
        self.cor = cor