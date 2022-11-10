class Animal:

    especie = ''
    raca = ''
    cor = ''

    def __str__(self):
        return f'{self.especie} - {self.raca} - {self.cor}'