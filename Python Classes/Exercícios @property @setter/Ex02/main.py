from carro import Carro

def criaCarro():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    categoria = input("Categoria: ")
    return Carro(marca, modelo, cor, categoria)

carro1 = criaCarro()
print(carro1)

carro2 = criaCarro()
print(f"{carro2.marca} - {carro2.modelo} - {carro2.categoria}")

