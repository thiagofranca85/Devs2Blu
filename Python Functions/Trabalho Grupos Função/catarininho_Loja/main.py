from controller import cadastroProduto,venda,apagarProduto,relatorio,aumentarEstoque #importa as funções

def menu():#função menu



    menu=1 #valor inicial de menu
    while (menu!=0): #menuzinho
            print('='*30, 'CATARININHO MEGA STORE', '='*30)#cabeçalho

            print('\n O que podemos fazer para você hoje?\n')
            #menu recebe a opção desejada
            menu = int(input('1. -> Cadastro de Produto\n2. -> Relatorio de Vendas\n3. -> Venda\n4. -> Apagar\n5. -> Aumentar quantidade do produto\n0. -> Sair\n>: '))

            match menu: #condicional 
                case 1:#caso cadastro

                    produto = {} #declara lista vazia
                    quantidadeInicial={} #declara lista vazia
                    #leitura de dicionario 
                    produto['nome']=str(input("Digite o nome do produto: "))   
                    produto['tipo']=str(input("Digite o tipo do produto: "))
                    produto['preco']=float(input("Insira o preço do seu produto: "))
                    produto['quantidade']=int(input("Digite a quantidade de itens: "))
                    produto['quantidadeInicial']=produto['quantidade']
                    cadastroProduto(produto) #chama a função cadastro e passa o produto como parametro
                case 2:
                    relatorio()#chama a função relatorio 
                case 3:
                    nome=str(input("digite o nome do item vendido"))#digita o nome a ser procurado
                    quant=int(input("digite a quantidade vendida: "))#digita a quantidade vendida
                    venda(nome,quant)#chama a função venda e passa o produto e a quantidade como parametro
                case 4:
                    produto = input('Informe o produto: ')#recebe o produto
                    apagarProduto(produto)#chama a função apagar e passa o produto como parametro
                case 5:
                    estoque = str(input('Informe o nome do produto que queira aumentar o estoque\n>'))#digita o nome a ser procurado
                    quant=int(input("digite a quantidade aumentada: "))#digita a quantidade aumentada
                    aumentarEstoque(estoque,quant)#chama a função aumentarEstoque e passa o produto e a quantidade como parametro
                
        


menu()