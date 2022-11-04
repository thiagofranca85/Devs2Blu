import os


def salvarAlunos(dados_aluno): #
    with open('dadosAlunos.txt','a') as arquivo: 
        arquivo.write(str(dados_aluno)+"\n") 

def salvarProfessor(dados_professor):#criando funcao e pegando os dados dos professores
    with open('dadosProfessor.txt', 'a') as arquivo: #abrindo o arquivo txt
        arquivo.write(f'{dados_professor}\n') #salvando tudo no arquivo txt os dados que tinham no professor

def salvarCursos(dados_curso): #
    with open('dadosCursos.txt','a') as arquivo: 
        arquivo.write(str(dados_curso)+"\n") 