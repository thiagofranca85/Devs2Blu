import os

# Função de save dos dados de cadastro do aluno.
def salvar(curso):
    
    with open('cursos.txt', 'a') as arquivo: #função 'open' abre o arquivo txt para ser editado.       
        arquivo.write(str(curso)+"\n") #função 'write' escreve no arq. txt as informações cadastradas pelo usuário.
        os.system('cls')
        print(f"Curso cadastrado:\n{curso}")
        
        
def listar_curso():    
    with open('cursos.txt') as arquivo:  #função 'open' abre o arquivo txt para ser editado.
        print(f"Lista de cursos cadastrados:\n{arquivo.read()}") #função 'read' lê o arq. txt com informações cadastradas pelo usuário e exibe.

def media(n1, n2, n3):

    media = (n1 + n2 + n3) / 3
    if media >= 7:
        media = f'Aprovado'
    elif media >= 5:
        media = f'Em recuperação'
    else:
        media = f'Reprovado'
    return media

# Função de save dos dados de cadastro do aluno.
def salvarAlunos(dados_aluno): #(dados_aluno) é o dicionário em que consta as informações cadastradas.
    with open('alunosCadastrados.txt','a') as arquivo: #função 'open' abre o arquivo txt para ser editado.
        arquivo.write(str(dados_aluno)+"\n") #função 'write' escreve no arq. txt as informações cadastradas pelo usuário.

#Funçaõ de listagem dos dados cadastrados.
def listarAlunos():
    with open('alunosCadastrados.txt') as arquivo: #função 'open' abre o arquivo txt para ser editado.
        print(arquivo.read()) #função 'read' lê o arq. txt com informações cadastradas pelo usuário e exibe.


def salvar_professor(professores):#criando funcao e pegando os dados dos professores
    with open('dadosProfessor.txt', 'a') as arquivo: #abrindo o arquivo txt
        arquivo.write(f'{professores}\n') #salvando tudo no arquivo txt os dados que tinham no professor

def exibir_professor(): #criando uma funcao 
    with open('dadosProfessor.txt', 'r') as arquivo: #abrindo o arquivo txt
         print(arquivo.read())# exibindo todas as informacao do arquivo txt