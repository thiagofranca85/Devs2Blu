#from controller import * # Falta o listaTodosDeGenero, relatorioTitulos
from controller import menu, cadastraTitulo, buscaTitulo, mostraBonito, editaTitulo, pegaDadosCadastro, listaTodosOsTitulos
## Inicio do projeto com o import de todas as funções que utilizadas no projeto. 
while True:
#Definição de while: Esta instrução é usada quando não sabemos quantas vezes um determinado bloco de 
#instruções precisa ser repetido. Com ele, a execução das instruções vai continuar até que uma condição 
# seja verdadeira.
    menu()
    #Chama função menu. (Controller na linha 14)
    opcao = input("Digite uma opção: ")
    # Após chamar a função, atribuimos uma var chamada opcao, 
    # para trabalhar com o match abaixo.
    
    match opcao:
    #Match é um atributo do Python, que nesse caso  "substitui"  o if e else.
        case "1":
        #Ao apertar 1 "execute":
            cadastraTitulo(pegaDadosCadastro())
            #Nesse caso executar essa função 'cadastraTitulo'. (Controller na linha 14). 
            # O argumento da função chama: pegaDadosCadastro, que retorna um título dicionário
            # (Controller na linha 22, mais importante).
        case "2":
            opcao2 = buscaTitulo(input("Informe o nome do titulo a ser alterado: "))
            if opcao2:
                print("Informe os novos dados do tilulo: ")
                editaTitulo(pegaDadosCadastro(opcao2))
            else:
                print("Titulo não encontrado ")
        case "3":
            mostraBonito(listaTodosOsTitulos())
        case "4":
            mostraBonito(buscaTitulo(str(input("Digite o titulo: "))))
        case "5":
            break
        case _:
            print("NÃO!!!!")