

"""
O intuito é fazer um chatbot de suporte técnico.          

1- Primeiramente terá um menu questionando ao usuário se ele quer se identificar ou não (reclamar de forma anônima)
- Se ele escolher se identificar, o usuário deve informar seu nome, CPF e telefone.

2- Após isso, o programa tem que questionar se o usuário quer fazer uma reclamação ou alterar um dado.
- Se ele escolher reclamação, ele deve digitar o que aconteceu, após isso o usuário poderá escolher entre
finalizar o suporte ou conversar com um atendente.

3- Se ele escolher falar com atendente deverá entrar na fila de espera

4- Se ele escolher alterar dados, o usuário deverá escolher qual dado quer alterar
- No caso dele alterar algum dado, as informações do usuário que estarão salva num dicionário deverão ser
atualizadas pelo programa.

5 - No caso da alteração do cpf, o programa deverá informar se o dado digitado pelo usuário é um valor de cpf válido.

1 - No caso de ser anônimo, o usuário vai direto pra parte de reclamar (já que não tem dado pra ser verificado ou coisa do tipo)"""


# MENSAGEM DE INÍCIO DO BOT E CONFIRMACAO DE IDENTIFICACAO
id = str(input("BEM-VINDO(A) AO CHATBOT!\nPor favor, digite SIM para se identificar ou NÃO para continuar: "))


# SOLICITACAO DE DADOS DO USUARIO.
if id == "sim":
    print("\nPara darmos seguimento tenha em mãos os seguintes dados: Nome completo, número de CPF e telefone")
    nome = str(input("Agora, por favor informe seu nome: "))
    cpf = input(f"Obrigado, {nome}! Agora precisamos de seu CPF. Digite apenas os números, sem pontuação: ")

    #### INCLUIR VERIFICAÇÃO DE VALIDADE DO CPF ####
    tel = int(input("Excelente, seu CPF é válido! Por último, favor digitar seu telefone para contato com DDD: "))

else:
    print("Ok, vamos continuar conversando sem identificação.")
    ### INCLUIR CADASTRO DA RECLAMACAO AQUI.