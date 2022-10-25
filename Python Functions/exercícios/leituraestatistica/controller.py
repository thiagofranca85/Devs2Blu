# A) Quantas pessoas foram cadastradas; 
# B) A média de idade do grupo; 
# C) Uma lista com todas as mulheres; 
# D) Uma lista com todas as pessoas com idade acima da média.

pessoas = []

def cadastro(nome, sexo, idade):
    dados = {
        'nome': nome, 
        'sexo': sexo,
        'idade': idade
    }
    pessoas.append(dados)
    print(f"\nCadastrado efetuado com sucesso.\n")
    
def listarEstatistica():
    for i in pessoas:
        print(i)
        idades = sum(pessoas, 'idade')
        mIdades = idades / (len(pessoas))
   
    print(f"Há {len(pessoas)} pessoa(s) cadastrada(s).")
    print(mIdades)

        
    