nome = str(input("Digite seu nome: "))
sobreNome = str(input("Digite seu sobrenome: "))
idade = int(input("Digite a sua idade: "))

print(f"nome: {sobreNome} sobrenome: {nome} \nIdade: {idade}",type(nome), type(sobreNome), type(idade))

lista = ['joao', 'gabriel','paulo']
lista.sort(reverse=True)

for i in lista:
    print(i)


