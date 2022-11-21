"""2- Após isso, o programa tem que questionar se o usuário quer fazer uma reclamação ou alterar um dado.
- Se ele escolher reclamação, ele deve digitar o que aconteceu, após isso o usuário poderá escolher entre 
finalizar o suporte ou conversar com um atendente."""

#AS BIBLIOTECAS QUE PRECISO

from datetime import date
from random import randint

#ISSO AQUI EU CRIEI PARA CONSEGUIR FAZER TESTES - NO CÓDIGO VAI PRECISAR TROCAR O NOME DAS VARIÁVEIS

nome = str(input("Digite o seu nome: ")).title()
cpf = int(input("Digite o seu CPF: "))
telefone = input("Digite o seu telefone: ")
poli = "~"*50

#EU PRECISO DISSO PRO MEU CÓDIGO FUNCIONAR
protocolo = [randint(1,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
anoProtocolo = date.today().year
protocolostr = ""
for c in range (0,len(protocolo)):
    protocolostr += str(protocolo[c])       # Transforma em str para ficar sem os [] da lista

#AQUI É O CÓDIGO PROPRIAMENTE DITO:

print(f"{poli}")

escolha_1 = int(input("O que você quer fazer? \n1- Reclamação\n2- Alteração de Dados\nDigite: "))

print(f"{poli}")

while escolha_1 == 1:
    reclamacao = str(input("Qual a sua reclamação? "))
    print(f"{poli}")

    print(f"Obrigado(a) {nome} pelas informações fornecidas! O seu protocolo é o número {protocolostr}-{anoProtocolo}." \
        "\nIremos avaliar e entraremos em contato no telefone informado.")
    
    
    print()

    print(f"{poli}")

    escolha_1 = str(input("Deseja finalizar o atendimento ou conversar com um atendente? Escolha: \n1- Finalizar atendimento." \
        "\n2- Conversar com um atendente\n"))
    break

    print(f"{poli}")

else:
    str(input("Qual dados você gostaria de alterar? "))

# EM TEORIA ACABA AQUI

print(f"{poli}")

print("Obrigada por ter nos escolhido!")        #ISSO FOI SÓ PRA TER ALGO NO FINAL DO MEU CÓDIGO E PODE SAIR.

print(f"{poli}")
