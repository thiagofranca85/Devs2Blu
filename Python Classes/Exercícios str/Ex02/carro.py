class Carro:

    marca = ''
    modelo = ''
    valor = 0

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.valor}'