
# importação de funções do arquivo controller.py
from controller import listar_curso, media, salvar
from controller import salvarAlunos, listarAlunos
from controller import salvar_professor, exibir_professor
import os

if __name__ == "__main__":    
    
    # função menu() recebendo os dados iniciais do usuário.
    def menu():
        
        while True:
            # variável menuPrincipal com as opções
            menuPrincipal = int(input("MENU PRINCIPAL\n1. FAZER CADASTROS\n2. MOSTRAR LISTAGENS\nPor favor, digite o nr. da opção desejada: "))       
                        
            # condicional if para identificar o input da variável menuPrincipal.
            if menuPrincipal == 1:
                os.system('cls')
                menuSecundario = int(input("MENU DE CADASTROS\n1. Cadastro de Alunos\n2. Cadastro de Professores\n3. Cadastro de Cursos\n4. Simular Média\n5. SAIR\nPor favor, digite o nr. da opção desejada: "))
                match menuSecundario:
                    case 1:
                        os.system('cls')
                        print("-"*25, "CADASTRO DE ALUNOS", "-"*25) # imprimindo com o polimorfismo
                        #Dicionário salvando o cadastro de alunos.
                        
                        dados_aluno = {}                        
                        dados_aluno['nome'] = str(input("Digite o nome completo do aluno: "))
                        dados_aluno['CPF'] = str(input("Digite o CPF do aluno: "))
                        dados_aluno['matricula'] = int(input("Digite o número da matrícula do aluno: "))
                        salvarAlunos(dados_aluno) 
                        os.system('cls')                       
                        print(f"Aluno cadastrado!\n{listarAlunos()}")                        
                        
                    case 2:
                        os.system('cls') 
                        print("-"*25, "CADASTRO PROFESSOR", "-"*25) # imprimindo "CADASTRO PROFESSOR" com o polimorfismo ------
                        
                        professores = {} #dicionario sem dados                        
                        professores['nome'] = str(input("Insira o nome do professor que queira cadastrar: ")) #exibindo uma informacao e salvando ela como 'nome'
                        professores['idade'] = int(input("Insira a idade do professor que queira cadastrar: ")) #exibindo uma informacao e salvando ela como 'idade' 
                        professores['salario'] = float(input("Insira o salario do professor que queira cadastrar: "))  #exibindo uma informacao e salvando ela como 'salario'     
                        salvar_professor(professores) #salvando as informacoes no dicionario professores  
                        os.system('cls')                  
                        print(f"Professor cadastrado!\n{exibir_professor()}") #exibindo os dados

                    case 3:
                        os.system('cls')
                        print("-"*25, "CADASTRO DE CURSOS", "-"*25) # imprimindo com o polimorfismo ------

                        curso = {}
                        curso['nome'] = str(input("Digite o nome do curso: "))
                        curso['carga_horaria'] = int(input("Digite a carga-horária : "))
                        curso['modalidade'] = str(input("Digite a modalidade (presencial ou EAD) : ")) 
                        curso['investimento'] = float(input("Digite o valor da mensalidade : "))
                        salvar(curso)
                        os.system('cls')                  
                        print(f"Curso cadastrado!\n{listar_curso()}") #exibindo os dados              
                                   
                    case 4:
                        os.system('cls') 
                        print("-"*25, "SIMULADOR DE MÉDIA", "-"*25) # imprimindo com o polimorfismo ------

                        nome = str(input('Digite o nome do aluno para simular as notas: '))
                        n1 = float(input('Digite a primeira nota: '))
                        n2 = float(input('Digite a segunda nota: '))
                        n3 = float(input('Digite a terceira nota: '))
                        mediaAluno = (n1 + n2 + n3)/3
                        resultado = media(n1, n2, n3)
                        os.system('cls') 
                        print(f'Calculo da Media do aluno: {nome} \nPrimeira nota: {n1} \nSegunda nota: {n2} \nTerceira nota: {n3}\n\nO Aluno esta com a média {mediaAluno:.2f}\nResultado: {resultado}\n')

                    case 5:
                        break                      
                                    
                    case _:
                        os.system('cls')
                        print("Opção Inválida. Escolha entre 1 e 5!\n")

            if menuPrincipal == 2:
                os.system('cls')
                menuSecundario = int(input("MENU DE LISTAGENS\n1. Lista de Alunos\n2. Lista de Professores\n3. Lista de Cursos\n4. SAIR\nPor favor, digite o nr. da opção desejada: "))
                
                match menuSecundario:                    
                    case 1:
                        os.system('cls')
                        print("-"*25, "LISTA DE ALUNOS CADASTRADOS", "-"*25) # imprimindo com o polimorfismo
                        print(listarAlunos())
                        

                    case 2:
                        os.system('cls')
                        print("-"*25, "LISTA DE PROFESSORES", "-"*25) # imprimindo com o polimorfismo
                        print(exibir_professor()) #exibindo os dados
                        

                    case 3:
                        os.system('cls')
                        print("-"*25, "LISTA DE CURSOS", "-"*25) # imprimindo com o polimorfismo
                        print(listar_curso())                        
               
                    case 4:
                        os.system('cls')
                        print("Programa Encerrado.")
                        break                       
                                    
                    case _:
                        os.system('cls')
                        print("Opção Inválida. Escolha entre 1 e 4!\n")

    menu()
