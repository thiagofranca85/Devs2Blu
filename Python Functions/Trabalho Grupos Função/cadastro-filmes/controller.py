import os
#from random import randrange
#import linecache
import ast

os.system('cls' if os.name == 'nt' else 'clear')

def buscaTitulo(nome): #recebe o nome do título da obra.

    with open('database.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['titulo'] == nome:
                return line
            
    return False



def cadastraTitulo(titulo): #Recebe um titulo [Dicionário] e converte para string e salva no final do arquivo.
    with open('database.txt', 'a') as writer:
        writer.write(f'\n{titulo}')
        # o \n é usado criar uma nova linha, caso contrário ele irá salvar um do lado do outro.



def menu():
    print("1- Cadastrar Títulos:")
    print("2- Editar Títulos")
    print("3- Mostrar todos os Títulos") #Dieter
    print("4- Procurar Título") #Luiza
    print("5- Sair do programa")
    
def pegaDadosCadastro():
    tipo = input("Tipo: ") #
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    duracao = input("Duracao: ")
    assistido = input("Assitido S/N: ")
    if assistido.lower() == "s":
        assistido = '1'
    else:
        assistido = '0'
    titulo = ("{" + f"'tipo': {tipo}, 'titulo': '{titulo}', 'genero':'{genero}', 'duracao':'{duracao}'"+"}")
    return titulo



def relatorioHospedes():

    #sintax com funcao open para arquivo txt
    with open('hotel/hotel.txt') as arquivo:  

        #print recebendo a variavel arquivo que referencia arquivo txt, sendo lida pela funcao internalizada read
        print(arquivo.read())

        



def listaTodosOsTitulos():
    pass

def listaTodosDeGenero(generos):
    pass

