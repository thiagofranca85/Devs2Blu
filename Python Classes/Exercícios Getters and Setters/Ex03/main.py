from carro import Carro

carro1 = Carro(input("Marca: "), input("Modelo: "), input("Cor: "), input("Categoria: "))
print(carro1)

carro2 = Carro(input("Marca: "), input("Modelo: "), input("Cor: "), input("Categoria: "))
print(f"Marca: {carro2.get_marca()} Modelo: {carro2.get_modelo()} Categoria: {carro2.get_categoria()}")