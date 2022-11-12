from pessoa import Pessoa

def criaPessoa():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    altura = input("Altura: ")
    return Pessoa(nome, cpf, idade, altura)
    
pessoa1 = criaPessoa()
print(pessoa1)

pessoa2 = criaPessoa()
print(pessoa2)
