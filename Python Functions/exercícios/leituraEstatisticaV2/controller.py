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

    print(f"Há {len(pessoas)} pessoa(s) cadastrada(s).")
    print(f"A média de idade é {(media()/len(pessoas)):.1f}.")
    listaMulheres()
    idadeAcimaMedia()

def media():
    soma = 0
    for cont in pessoas:
        soma += cont['idade']
    return soma

def listaMulheres():
    print("Mulheres Cadastradas")
    for mulher in pessoas:
        if mulher['sexo']== 'F':
            print(f"\t--> {mulher['nome']}")

def idadeAcimaMedia():
    print("Pessoas com idade acima da media")
    for cadastro in pessoas:
        if cadastro['idade'] >= (media()/len(pessoas)):
            for chave, info in cadastro.items():
                print(f"\t{chave} -> {info}")
            print('-'*30)
