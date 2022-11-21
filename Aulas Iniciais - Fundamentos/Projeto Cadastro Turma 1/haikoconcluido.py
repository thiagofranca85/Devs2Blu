n1 = str(input("Nome do primeiro usuario: "))
n2 = str(input("Nome do segundo usuario: "))
n3 = str(input("Nome do terceiro usuario: "))

lista = [n1, n2, n3]

print ("Você deseja alterar algum dado? \n Se sim - S \n Se não - N")
simounao = input()

while simounao == "S":

    nomeAlterar = str(input("Digite o nome que queira alterar: "))
    nomeNovo = str(input("Digite o novo nome alterar: "))

    for i in range(len(lista)):
        if lista[i] == nomeAlterar:
           lista[i] = nomeNovo

    for x in range(0, len(lista)):
        print(lista[x])
    print ("Você deseja alterar algum dado novamente? \n Se sim - S \n Se não - N")
    simounao = input()

print("Você alterou seu dados")