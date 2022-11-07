class Produto:

    def __init__(self,id,nomeProduto,valor,quantidade):
        print(f"Imprimindo construtor {self}")

        self.id = id
        self.nomeProduto = nomeProduto
        self.valor = valor
        self.quantidade = quantidade