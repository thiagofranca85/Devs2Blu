from time import sleep

media = 0

while media < 7:
    nome = str(input("Digite seu nome: "))
    sobreNome = str(input("Digite seu sobrenome: "))
    idade = int(input("Digite a sua idade: "))
    lista_notas = []

    for lista in range(0, 2):
        nota = int(input("Digite sua nota: "))
        lista_notas.append(nota)

    media = sum(lista_notas) / len(lista_notas)
    situacao = 'Reprovado'

    if media >= 7:
        for i in range(0, 6):
            sleep(1)
            print("*")
        situacao = "aprovado"
 
    dicionario_alunos = {"Nome": nome,"Sobrenome": sobreNome,"Idade": idade,"Situacao": situacao, "Media": media}
    print(f"{dicionario_alunos['Nome']} {dicionario_alunos['Sobrenome']} {dicionario_alunos['Idade']} - {dicionario_alunos['Situacao']} {dicionario_alunos['Media']}")

