from animal import Animal

animal1 = Animal(input("Especie: "),input("Raça: "), input("Porte: "), input("Cor: "))
print(animal1)

animal2 = Animal(input("Especie: "),input("Raça: "), input("Porte: "), input("Cor: "))
print(f"Especie: {animal2.get_especie()} - Raça: {animal2.get_raca()} - Cor: {animal2.get_cor()}")