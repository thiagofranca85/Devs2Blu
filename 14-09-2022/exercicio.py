# Faça do cadastro dos membros de sua equipe

from time import sleep

border = "-"*5
livros = []

while True:
    print(f"{border} Cadastro de Livros {border}\n(1) Cadastrar Livros\n(2) Listar Livros Cadastrados\n(3) Sair")
    id = input("Opção: ")
    
    if not(id.isnumeric()):
        print("Letras nao são validas como opção!")
        pass
    if id == str(1):
        livro = input("Digite um nome: ")
        livros.append(livro)
    elif id == str(2):
        print(f"{border} Lista de Membros {border}")
        for i in livros:
            print(f"{livros.index(i)} - {i}")
            sleep(2)
            
        print(f"{border}   Fim da Lista   {border}")
    elif id == str(3):
        print("Voce Fechou o Programa.")
        break
    else:
        print("Digite uma opção valida")











