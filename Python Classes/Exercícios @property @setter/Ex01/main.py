from animal import Animal

def criaAnimal():
    especie = input("Especie: ")
    raca = input("Raca: ")
    porte = input("Porte: ")
    cor = input("Cor: ")
    return Animal(especie, raca, porte, cor)

animal1 = criaAnimal()
print(animal1)

animal2 = criaAnimal()
print(f"{animal2.especie} - {animal2.raca} - {animal2.cor}")

## Opção para criar animais "infinitos" inseridos em uma lista

# from animal import Animal

# def buscaDados():
#     aux = []
#     aux.append(input("Especie: "))
#     aux.append(input("RaÃ§a: "))
#     aux.append(input("Porte: "))
#     aux.append(input("Cor: "))
#     return aux

# animais = []

# while True:
#     aux = input("Cadastrar animal: S/N: ")
#     print(aux)
#     if aux.upper() == "S":
#         dadosAnimal = buscaDados()
#         animais.append(Animal(dadosAnimal[0], dadosAnimal[1], dadosAnimal[2],dadosAnimal[3]))
    
#     else:
#         for i in range(len(animais)):
#             print(animais[i])
#         break