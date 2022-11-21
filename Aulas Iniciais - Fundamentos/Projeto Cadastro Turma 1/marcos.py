

"""
5 - No caso da alteração do cpf, o programa deverá informar se o dado digitado pelo usuário é um valor de cpf válido. 
"""


# VALIDADOR TELEFONE

dadosCadastro = [{'nome': 'Marcos Silveira', 'cpf': '78946667945'}] # serão salvos em uma lista, cada usuário terá um dicionário dentro da lista
listaTemp = list()               # lista temporária para conversão de STR > INT

while True:
    listaTemp.clear()       # sempre irá limpar a lista temporária antes de cadastrar outro usuário
    telefone = str(input('telefone: ')).strip()                   # recebe os dados (telefone) como STR
    telefone = telefone.replace('.', '')                          # REMOÇÃO DE '.' , ' ' E '-' caso o usuário use
    telefone = telefone.replace('-', '')
    telefone = telefone.replace(' ', '')

    if len(telefone) != 11 or not telefone.isdecimal():     # se telefone for diferente de 11 e se não for decimal
        print('Digite um número válido!\n')   #Se digitar a quantidade de números errada correto: 47 98888-7777

    else:
        listaTemp = list(telefone)          # Adiciona o telefone a uma lista ex: [3, 5, 6, 5]
        listaTemp.insert(2, ' ')            # Insere o espaço apos o "DDD"
        listaTemp.insert(8, '-')            # Insere o "-" no meio do número
        telefone = ''.join(listaTemp)       # Junta a lista novamente e passa ela para a variável
        print(telefone)         # print p teste

        # ADICINANDO O NÚMERO PARA O DICIONÁRIO
        dadosCadastro[0]['telefone'] = telefone         # O cadastro estará dentro de um loop
        break                                           # O "0" será o "c" do loop
                                                        # Quando cadastrar outro usuário, o "c" altera sozinho
                                                        # e não precisa se preocupar com a posição da lista

print(dadosCadastro)    # print p teste

# FIM VALIDADOR DE TELEFONE







# VALIDADOR DE CPF

# LISTAS
rLista = list()             # Respostas dos cálculos
listaCPF = list()           # Lista do CPF fracionado em str
listaInt = list()           # LIsta do CPF fracionado em int

# CPF deve ser salvo como STR porque caso inicie com '0' irá dar erro ao salvar no dicionário

while True :
    # VARIÁVEIS
    decrescente = 10
    posicao = 0
    listaCPF.clear()
    rLista.clear()
    listaInt.clear()
    cpf = str(input('CPF: ')).strip()
    cpf = cpf.replace('.', '')              # REMOÇÃO DE '.' E '-'
    cpf = cpf.replace('-', '')

    if len(cpf) != 11 or not cpf.isdecimal():   # se CPF for diferente de 11 e se não for decimal
        print('Digite o CPF corretamente!\n')   #Se digitar a quantidade de números errada

    else:
        listaCPF = list(cpf)    #CPF AINDA É UMA str FOI FATIADO NA LISTA

        # PRIMEIRO DIGITO

        # PADRÃO
        """
        for c in range(0, len(listaCPF)):
            listaInt.append(int(listaCPF[c]))       # CPF NA LISTA INT
        """
        # FIM PADRÃO

        [listaInt.append(int(digito)) for digito in listaCPF]     # LIST COMPREHENSION

        for c in range(10, 1, -1):
            """
            Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente
            de números de 10 à 2 e soma os resultados
            """
            rLista.append(listaInt[posicao]*c)   # c=10,9,8,7...  posicao=0,1,2,3,4...
            posicao += 1        # O RESULTADO ESTÁ SEDO ADICIONADO EM OUTRA LISTA COMO int
                                # EU NÃO CONSEGUI FAZER ISSO SEM USAR DUAS LISTAS

        # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
        # Caso resto da divisão = 10, considerar = 0
        # Se o resultado for igual ao primeiro digito do cpf (posição 9) , primeira parte da validação OK

        resultado = (sum(rLista)*10 ) % 11
        if resultado == 10:
            resultado = 0

        #print(resultado)   Teste para ver se o resultado é igual ao penultimo digito

        if resultado == listaInt[-2] and len(set(listaInt)) > 1:     # IRÁ PROCEGUIR CASO PASSE A PRIMEIRA VALIDAÇÃO
                                                                     # SET() REMOVE OS ITENS DUPLICADOS
            # SEGUNDO DIGITO                                         # CASO O USUÁRIO DIGITE 11111111111
            # VARIÁVEIS
            decrescente = 10
            posicao = 0
            rLista.clear()      # LIMPA rLista

            for c in range(11, 1, -1):
                """
                Vamos multiplicar os 10 primeiros números (9 números + 1 digito verificador) pela 
                sequência decrescente de números de 11 à 2 
                """
                rLista.append(listaInt[posicao]*c)   # c=11,9,8,7...  posicao=0,1,2,3,4...
                posicao += 1        # O RESULTADO ESTÁ SEDO ADICIONADO EM OUTRA LISTA COMO int E NÃO MAIS str
                                    # EU NÃO CONSEGUI FAZER ISSO DE OUTRO JEITO

            # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
            # Caso resto da divisão = 10, considerar = 0
            # Se o resultado for igual ao primeiro digito do cpf (posição 10) , primeira parte da validação OK

            resultado = (sum(rLista)*10 ) % 11
            if resultado == 10:
                resultado = 0

            #print(resultado)           teste para confirmar se o resultado é igual ao ultimo digito

            if resultado == listaInt[-1]:
                print('CPF ok')         ##*** FAZER A ALTERAÇÃO OU CADASTRO DO CPF AQUI ***##
                break
        else:
            print('CPF inválido!')
print('fim')
# FIM VALIDADOR CPF

