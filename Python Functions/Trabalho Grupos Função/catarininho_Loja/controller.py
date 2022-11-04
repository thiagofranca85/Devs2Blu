from datetime import datetime


def cadastroProduto(produto):
    
    with open('produtos.txt', 'a') as arquivo:#com arquivo aberto
        arquivo.write(str(produto)+"\n")#escreve no arquivo o dicionario recebido


def procuraItem(nome):#função que recebe a variavel nome para procurar no arquivo 
    index=0#ponteiro
    flag=0#verificador de existencia 
    arquivo = open("produtos.txt", "r") #abre arquivo em modo de leitura
    for line in arquivo:#percorre o arquivo
        index +=1#soma o ponteiro
        if nome == eval(line)['nome']:#verifica se o nome na linha é igual ao nome procurado
            chave = index #armazena a linha que contem o nome procurdo
            flag =1#indica pro flag que existe o usuario
    if flag == 0:#verifica se existe o usuario
        arquivo.close()#se nao existe fecha o arquivo e retorna 0
        return 0
    else:
        arquivo.close()#se existe fecha o arquivo e retorna a linha que esta o usuario
        return chave  

def apagarProduto(findProduto):
        #Lista onde vão ser colocados os produtos dentro do arquivo
        #   V
        lista = []

        #Pega cada linha dentro do arquivo e joga dentro da lista
        #   V
        with open('produtos.txt', 'r') as arquivo:
            for numero, linha in enumerate(arquivo): #lê linha por linha o arquivo
                relatorio = eval(linha) #converte a linha do arquivo para dicionário
                lista.append(relatorio) #joga esse dicionário para dentro da lista

        #Deleta o produto dentro da lista
        #   V
        for x in range(0, len(lista)): #lê a lista de produtos indice por indice...
            if findProduto == lista[x]['nome']: #se o nome escrito do input for o mesmo do produto da lista, executa o comando

                del lista[x] #deleta o produto dentro da lista
                break #quebra o loop (evita o erro "index out of range")
        
        #Reescreve o arquivo com os produtos da lista
        #   V
        with open('produtos.txt', 'w') as arquivo: #Na hora de executar o comando, ele limpa o arquivo de texto para substituir os dados
            for x in range(0, len(lista)): #Lê a lista indice por indice
                arquivo.write(str(lista[x])+'\n') #Repõe os produtos da lista para dentro do arquivo de texto

def venda(nome,quant):#função que registra a venda
    chave=procuraItem(nome)#armazena a linha que ta o usuario procurado
    temp={}#cria um dicionario temporario vazio
    if chave != False:#verifica se a chave é true
        try:
            with open('produtos.txt', 'r') as fr:#abre o arquivo em mode de leitura
                # reading line by line
                lines = fr.readlines()
                
          
                # pointer for position
                ptr = 1
                
                # opening in writing mode
                with open('produtos.txt', 'w') as fw:
                    for line in lines:
                        
                        # we want to remove chave line
                        if ptr != chave:#verifica se a linha atual é a linha desejada
                            fw.write(line)#se nao for digita a linha normalmente
                        else:#se for a linha desejada
                            dif = eval(line)['quantidade'] -quant  #variavel que recebe quantidade atual

                            temp=eval(line)#faz a lista temporaria receber a linha desejada
                            
                            
                            temp['quantidade'] = dif #faz a lista temporaria receber o valor de quantidade atual
                            lucro=quant*eval(line)['preco'] #calcula o lucro
                            
                            with open('vendas.txt', 'a') as fv: #abre o arquivo venda como altere
                                fv.write("item:{} lucro:{} quantidade vendida:{}\n".format(eval(line)['nome'],lucro,quant))#escreve no arquivo
                            
                        ptr = ptr+1
                
        except:
            print("Oops! someting error")
        with open('produtos.txt', 'a') as fd:#abre o arquivo produtos como altere
            fd.write(str(temp)+'\n')#digita a variavel temporario no arquivo produtos
    else:
        print("NAO ENCONTRADO")

def relatorio():#função que retorna o relatorio de vendas
    with open('vendas.txt','r') as arquivo:  # abre arquivo como leitura
        print(arquivo.read())#printa o arquivo


def aumentarEstoque(estoque,quant):#função que aumenta estoque
    chave=procuraItem(estoque)#armazena linha do produto desejado
    temp={}
    if chave != False:
        
        
        try:
            with open('produtos.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
          
                # pointer for position
                ptr = 1
                
                # opening in writing mode
                with open('produtos.txt', 'w') as fw:
                    for line in lines:
                        
                      
                        if ptr != chave:
                            fw.write(line)
                        else:
                            dif = eval(line)['quantidade'] + quant #aumenta na colunaquantidade o valor digitado

                            temp=eval(line) 
                            
                            
                            temp['quantidade'] = dif
                            
                            
                            
                            
                        ptr = ptr+1
                
        except:
            print("Oops! someting error")
        with open('produtos.txt', 'a') as fd:
            fd.write(str(temp)+'\n')
    else:
        print("NAO ENCONTRADO")