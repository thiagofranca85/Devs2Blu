import random
#Função gravar arquivo para criptografia
def GravarArquivo(mensagem):
    #arquivo txt sendo aberto na variável 'arquivo'
    with open('mensagem.txt', 'w') as arquivo:
        for line in mensagem:
            #variável 'arquivo' com função write escrevendo a variável 'line' e quebrando a linha por cada índice da lista.
            arquivo.write(line + '\n')
    return True

#Função Ler arquivo criptografado
def LerArquivo(arquivo):

    #sintax com funcao open para arquivo txt
    lista = []
  
    with open(arquivo) as arquivo:
        #print recebendo a variavel arquivo que referencia arquivo txt, sendo lida pela funcao internalizada readlines
        for linha in arquivo.readlines():

            lista.append(linha.strip('\n'))

    return lista

#Função que gera uma chave de 3 digitos
def SetChave(chave = None):
    # caso chave seja None, gera uma chave aleatória de 3 digitos
    if chave == None:
        # gera chave aleatória de 3 digitos
        chave = random.randint(100, 999)
    # Define a chave de aleatoriedade  
    random.seed(chave)
    # retorna a chave criada
    return chave

# Função que gera o dicionário de criptografia
def GerarDicio(caracteres):
    # Cria o dicionário
    dicionario = {}
    # for que passa por cada caracter da lista de caracteres permitidos
    for caracter in caracteres:
        # gera um valor aleatório de 2 digitos
        valor = random.randint(10,99)
        # vefirica se o valor gerado já existe dentro do dicionário
        while valor in dicionario.values():
            # caso exista gera números randomicamente até achar um que não foi utilizado ainda
            valor = random.randint(10,99)
        # adiciona o caracter ao dicionário em conjunto do valor
        dicionario[caracter] = valor
    # retorna o dicionário finalizado
    return dicionario

# Função que criptografa uma mensagem
def criptografar(mensagem:list, dicio:dict):
    # cria a lista que será enviada no final
    mensagemCriptografada = []
    # passa por linha item dentro da mensagem
    for linha in mensagem:
        # cria a lista que representa cada caracter de uma linha da mensagem
        linhaLista = []
        # passa por cada caracter da linha
        for letra in linha:
            # adiciona o caracter criptografado a linha
            linhaLista.append(str(dicio[letra]))
        # junta os caracteres em uma única linha e adiciona ela a mensagem final
        mensagemCriptografada.append(' '.join(linhaLista))    
    # retorna a mensagem inteira
    return mensagemCriptografada

# função que descriptografa a mensagem  
def descriptografar(mensagem:list, dicio:dict):
    # cria a lista que será enviada a mensagem
    mensagemDescriptografada = []
    # passa por cada linha da mensagem
    for linha in mensagem:
        # cria a lista que representa cada caracter de uma linha da mensagem 
        linhaLista = []
        # passa por cada número na mensagem
        for letra in linha.split():
            # passa por cada caracter dentro do dicionário de criptografia
            for carac, valor in dicio.items():
                # caso o número na mensagem seja igual ao valor dentro do dicionário, adiciona o caracter a lista
                if int(letra) == valor:
                    linhaLista.append(carac)
        # junta os caracteres da linha
        mensagemDescriptografada.append(''.join(linhaLista))
    # retorna a mensagem completa
    return '\n'.join(mensagemDescriptografada)
