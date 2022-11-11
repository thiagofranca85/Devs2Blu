from pessoa import Pessoa

pessoa1 = Pessoa(input("Digite seu nome: "),input("Digite CPF: "), int(input("Digite sua Idade: ")),float(input("Digite Altura: ")))
print(pessoa1)

pessoa2 = Pessoa(input("Digite seu nome: "),input("Digite CPF: "), int(input("Digite sua Idade: ")),float(input("Digite Altura: ")))
print(f"Nome: {pessoa2.get_nome()} CPF: {pessoa2.get_cpf()} Idade: {pessoa2.get_idade()}")

