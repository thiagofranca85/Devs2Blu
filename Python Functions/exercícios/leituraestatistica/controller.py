
pessoas = []

def cadastro(nome, sexo, idade):
    dados = {}
    dados['nome']=nome
    dados['sexo']=sexo
    dados['idade']=idade
    pessoas.append(dados)
    print(f"\nCadastrado efetuado com sucesso.\n")

def listarEstatistica():
    for number, pessoa in enumerate(pessoas):
        print(number + 1, pessoa)