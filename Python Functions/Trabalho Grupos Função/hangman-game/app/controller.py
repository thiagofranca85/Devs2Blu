from random import randint
from os import system


def sorteioPalavras():
    """ Função criada para sorteio de palavras (dificil/facil)
    Returns:
        List: Retorna a palavra referente ao nível selecionado
        dentro de uma lista, onde cada "letra" está em um indice
    """
    
    print('Escolha o nível de dificuldade:')
    nivel = str(input('[facil/dificil]: ')).lower().strip()     # Seleção de nível
    
    # VALIDAÇÃO
    while nivel not in 'facildificil' :
        print('Opção incorreta!')
        print('Escolha o nível de dificuldade:')
        nivel = str(input('[facil/dificil]: ')).lower().strip()     # Seleção de nível


    if nivel == 'facil':     # Nível facil
        
        with open('./db/facil.txt', 'r') as facil:     # Abre o TXT (leitura)
            palavras = facil.readlines()         # Cada linha será uma str
            
        sorteio = randint(0, len(palavras))     # Sorteio de um número (de 0 a len de palavras)
        
        return list(palavras[sorteio].strip())  # Retorna uma palavra do txt no indice de sorteio

    else:           # Nível dificil
        
        with open('./db/dificil.txt', 'r') as dificil:     # Abre o TXT (leitura)
            palavras = dificil.readlines()         # Cada linha será uma str
            
        sorteio = randint(0, len(palavras))     # Sorteio de um número (de 0 a len de palavras)
        
        return list(palavras[sorteio].strip())  # Retorna uma palavra do txt no indice de sorteio
    

def jogo(palavra):
    """
    Função contendo o jogo
    Args:
        palavra (List): Lista contendo a palavra utilizada no jogo
                        Cada letra está em um indice
    Returns:
        Boolean: True venceu / False perdeu
    """
    
    tempPalavra = list('_'*len(palavra))    # Lista mutável contendo "_" ao invés das letras da palavra
    indice = 0                              # Variável utilizada para informar o indice da lista forca
    vida = 5                                # Variável contendo a quandidade de chances do player
    
    # Listas com os ASCIIs do jogo
    forca = ['''
        _________
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \\
        |
       _|_ ''',
        '''
        _________
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / 
        |
       _|_ ''',
        '''
        _________
        |/      |
        |      (_)
        |      \|/
        |       |
        |      
        |
       _|_ ''',
        '''
        _________
        |/      |
        |      (_)
        |      \|/
        |       
        |      
        |
       _|_ ''',
            '''
        _________
        |/      |
        |      (_)
        |     
        |       
        |      
        |
       _|_ ''',
            '''
        _________
        |/   _____                         ____                 
        |   / ____|                       / __ \                
        |  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
        |  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
        |  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
        |   \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
       _|_ ''']
    win = '''
     __      __        //\                                  
     \ \    / /       |/ \|                                 
      \ \  / /__   ___ ___  __   _____ _ __   ___ ___ _   _ 
       \ \/ / _ \ / __/ _ \ \ \ / / _ \ '_ \ / __/ _ \ | | |
        \  / (_) | (_|  __/  \ V /  __/ | | | (_|  __/ |_| |
         \/_\___/ \___\___|_  \_/ \___|_| |_|\___\___|\__,_|
          |  __ \              | |     /_/          | |          
          | |__) |_ _ _ __ __ _| |__   ___ _ __  ___| |          
          |  ___/ _` | '__/ _` | '_ \ / _ \ '_ \/ __| |          
          | |  | (_| | | | (_| | |_) |  __/ | | \__ \_|          
          |_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___(_)     
    '''
    
    while vida != 0:    # Irá fazer o loop enquanto a vida for diferente de 0
        
        system('cls')   # "Limpa" a  tela
        
        #print(palavra)     # Print da palavra para teste
        
        print('='* 30)      # Topo
        print('ESCOLHA UMA LETRA'.center(30), ' ')
        print('='* 30)
    
        print(forca[indice], end =' ')      # Print da forca
        
        for letra in tempPalavra:           # Print da lista mutável
            print(letra.upper(), end=' ')
        
        
        letra = str(input(' > '))[0].strip().lower()    # Inserção da letra do jogador
        
        
        if letra in palavra:                        # Se a letra digitada "está" na palavra sorteada
            for i in range(0, len(palavra)):        # Irá percorrer o indice das letras contidas na palavra sorteada
                if palavra[i] == letra:             # Se palavra[i] for igual a letra digitada 
                    del tempPalavra[i]              # Remove "_" da lista temporária
                    tempPalavra.insert(i, letra)    # Coloca a letra digitada na possição correta
                  
                    
        else:           # Se a letra não estiver contida na palavra
            vida -=1    # Irá retirar uma vida e alter o indice para impressão da forca
            indice +=1
        
        
        if palavra == tempPalavra:      # Se a lista temporário for igual a lista contendo a palavra sorteada
            break                       # Jogador ganhou e irá sair do loop
    
    
    system('cls')   # "Limpa" a tela
    
    if vida == 0:               # Se a vida for igual a 0
        print(forca[-1])        # Irá inprimir a forca com o Game Over
        return False            # Retor False
    
    
    else :                      # Ganhou
        print(win)              # Irá inprimir a str win 
        return True             # Retorna True
            

def cadastroPessoa(player):
    """ Função criada para cadastrar o jogador no txt
    Args:
        player (Dict): Dicionário contendo as informações do jogador
    """
    
    with open('./db/infoUsuario.txt', 'a') as arquivo:  # Abre o txt
        arquivo.write(str(player)+"\n")     # Adiciona o dicionário ao txt


def atualizar(nome, resultado):
    """Função criada para atualizar as infomrações do jogador
    Args:
        nome (str): Nome / nickname do jogador 
        resultado (Boolean): Resultado do jogo (True venceu / False perdeu)
    """
    
    posicao = index = 0        # Variável criada para validação do código
    flag = False
    infoUsuario = open('./db/infoUsuario.txt', 'r')   # abre o TXT (leitura)
    player = {'nome':nome}      # Cria o dicionário e atribui o nome do Jogador
    
    
    # VALIDAÇÃO DO PLAYER NO TXT 
    for linha in infoUsuario:                  # Pra cada player de infoUsuario
        if nome == eval(linha)['nome']:     # Se nome for igual ao dicionário linha na posção nome
            player = eval(linha)            # Encontra o player e coloca em um dicionário para alteração futura
            posicao = index     # Variável para validação futura
            flag = True         # Variável para validação futura
            
        else :              # Se não, irá atribuir +1 a variável index
            index += 1
            
    infoUsuario.close()        # Fecha o arquivo
    
    
    # "PEGAR" AS INFORMAÇÕES DO PLAYER
    if flag :       # Se o player já possuir um histórico, Flag será True
        
        with open('./db/infoUsuario.txt', 'r') as ler:  # Abre o TXT (leitura)
            linhas = ler.readlines()            # Cada linha será uma str
            index = 0                           # Altera o valor de index
            
            with open('./db/infoUsuario.txt', 'w') as escrever:     # Abre o TXT (escrever no arquivo)
                for item in linhas:                         # Loop para percorrer linha por linha
                    if posicao != index:                    # Se posição do loop for diferente da posição do player
                        escrever.write(item)                # Escreva linha[c] no txt
                    index += 1                              # Altera o valor de index
                
                
        # ATUALIZAÇÃO DAS PORCENTAGENS
        player['qPartidas'] += 1        # Adiciona + 1 jogo no histórico

        if resultado:                   # Se resultado for True (ganhou)
            player['vitorias'] += 1     # round(6.4654654984, 1) irá limitar o float a 1 decimal
            player['pVitorias'] = round(player['vitorias'] / player['qPartidas'] * 100, 1)  # Cálculo para a porcentagem de vitorias
            player['pDerrotas'] = round(100 - player['pVitorias'], 1)                       # Cálculo para a porcentagem de derrotas
        
        else:                           # Ganhou
            player['derrotas'] += 1     # round(6.4654654984, 1) irá limiar o float a 1 decimal
            player['pDerrotas'] = round(player['derrotas'] / player['qPartidas'] * 100, 1)  # Cálculo para a porcentagem de derrotas
            player['pVitorias'] = round(100 - player['pDerrotas'], 1)                       # Cálculo para a porcentagem de vitorias
        
        
        cadastroPessoa(player)   # Função que adiciona o player no txt


    else :      # O player não possui um histórico
        
        # INSERÇÃO DAS PORCENTAGENS 
        if resultado:   # Se resultado for True (ganhou)
            player['qPartidas'] = 1
            player['vitorias'] = 1
            player['derrotas'] = 0
            player['pVitorias'] = 100   # 100% de vitorias
            player['pDerrotas'] = 0
        
        
        else:           # Perdeu
            player['qPartidas'] = 1
            player['vitorias'] = 0
            player['derrotas'] = 1
            player['pVitorias'] = 0
            player['pDerrotas'] = 100   # 100% de derrotas
        
        cadastroPessoa(player)   # Função que adiciona o player no txt
        

def estatisticas():
    """ Função criada para mostrar as estatisticas e infomrações dos
        Jogadores no jogo
        ### Falta criar uma ordem por % de vitórias ###
    """
    
    system('cls')       # "Limpa" a tela
    print('HISTÓRICO DE JOGADORES'.center(30))      # Topo
    
    infoUsuario = open('./db/infoUsuario.txt', 'r')            # Abre o TXT (leitura)
    
    
    for player in infoUsuario:     # Loop para acessar cada linha que estava no txt
        temp = eval(player)     # Variável temporária para auxiliar na impressão
                                # eval() transforma em um objeto
        
        # Print contendo as informações 
        print(f'''Player: {temp['nome'].title()}
Quantidade de partidas: {temp['qPartidas']}
Vitórias: {temp['vitorias']}
Derrotas: {temp['derrotas']}
Percentual de Vitórias: {temp['pVitorias']}%
Percentual de Derrotas: {temp['pDerrotas']}%\n''')
            
