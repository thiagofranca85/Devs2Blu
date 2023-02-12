nome = str(input("Qual seu nome: "))
sobreNome = str(input("Qual seu sobrenome: "))
idade = int(input("Qual sua idade: "))
salario = float(input("Qual seu salario: "))

print(f"Olá, Seja Bem Vindo !!! \nSeu nome é {nome} {sobreNome}. \nSua idade é {idade}. \nSeu salario é {salario:.2f}. {type(nome)}{type(sobreNome)}{type(idade)}{type(salario)}") 