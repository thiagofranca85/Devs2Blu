# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um 
# dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas; 
# B) A média de idade do grupo; 
# C) Uma lista com todas as mulheres; 
# D) Uma lista com todas as pessoas com idade acima da média.

def menu(): 
    dados = {}
    pessoas = []
    acumulaIdade = 0   
    while True:
        dados['nome']=input("Nome: ").strip().capitalize()
        dados['sexo']=input("Sexo [M/F]: ").strip().upper()
    
        while dados['sexo'] not in ('M', 'F'):
            print("Digite a alternativa correta.")
            dados['sexo']=input("Digite [M/F]: ").strip().upper()
        
        dados['idade']=int(input("Idade: "))
        acumulaIdade += dados['idade']

        pessoas.append(dados.copy())

        print('-'*30)
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()

        while continuar not in ('S', 'N'):
            print("Informe a opção correta.")
            continuar = input("Deseja continuar? [S/N]: ").strip().upper()

        if continuar == 'N':
            break

    print(f'{"Estatistica:":^30}\n' + '-'*30)
    print(f"Há {len(pessoas)} pessoa(s) cadastrada(s).")     

    idadeMedia = acumulaIdade / len(pessoas)
    print(f"A idade media é {idadeMedia:.1f} anos.")

    print("Mulheres Cadastradas")
    for cadastro in pessoas:
        if cadastro['sexo']== 'F':
            print(f"\t--> {cadastro['nome']}")

    print("\nPessoas com idade acima da media")
    for cadastro in pessoas:
        if cadastro['idade'] >= idadeMedia:
            for chave, info in cadastro.items():
                print(f"\t{chave} -> {info}")
            print('-'*30)

menu()


    



