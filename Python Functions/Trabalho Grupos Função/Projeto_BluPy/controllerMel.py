#Funçaõ de save dos dados de cadastro do aluno.
def salvarAlunos(dados_aluno): #(dados_aluno) é o dicionário em que consta as informações cadastradas.
    with open('alunosCadastrados.txt','a') as arquivo: #função 'open' abre o arquivo txt para ser editado.
        arquivo.write(str(dados_aluno)+"\n") #função 'write' escreve no arq. txt as informações cadastradas pelo usuário.

#Funçaõ de listagem dos dados cadastrados.
def listarAlunos():
    with open('alunosCadastrados.txt') as arquivo: #função 'open' abre o arquivo txt para ser editado.
        print(arquivo.read()) #função 'read' lê o arq. txt com informações cadastradas pelo usuário e exibe.