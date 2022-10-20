from controller import salvar, listar

def menu():
    print('*'*20, "MENU", '*'*20)

    cond = 'sim'
    while cond == 'sim':
        nome = salvar(input("Digite seu nome: "))
        cond = str(input("Deseja Continuar \nSim\nNão\n:> "))

menu()

print("A lista de Nomes Inseridos\n", listar())