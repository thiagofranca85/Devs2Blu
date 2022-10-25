import os

funcionarios = []

def cadfuncionario(nome, nascimento, carteira, anoContratacao, salario):
    dados = {}
    dados['nome']=nome
    dados['nascimento']=nascimento
    dados['carteira']=carteira
    dados['anoContratacao']=anoContratacao
    dados['salario']=salario
    funcionarios.append(dados)
    print(f"\nFuncionário cadastrado com sucesso\n")
    os.system('cls')

def listarFuncionarios():
    for number, funcionario in enumerate(funcionarios):
        print(number + 1, funcionario)

        
