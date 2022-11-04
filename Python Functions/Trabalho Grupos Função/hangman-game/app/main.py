from controller import atualizar, estatisticas, sorteioPalavras, jogo
from os import system


def menu():
    """
    Função principal contendo o menu do jogo
    """
    
    while True:                     # Loop do jogo
        system('cls')               # "Limpa" a tela
        
        print('JOGO DA FORÇA'.center(25, ' '))      # Topo
        
        # MENU
        print('Escolha uma das opções:')
        opcao = int(input('1 - Jogar \n2 - Estatísticas \n3 - Sair\n=> '))
        
        if opcao == 1:  # JOGAR
            nome = str(input('Insira seu nome: ')).strip().title()      # Inserção do nome do player
            print()     # Print para quebra de linha
            
            palavra = sorteioPalavras()     # Função que escolhe a palavra referente ao nível selecionado
            resultado = jogo(palavra)       # Resultado do jogo (True/False) será atribuido a variável resultado
            
            atualizar(nome, resultado)      # Função que atualiza o histórico do jogador
            
            enter = input('Precione ENTER para voltar ao Menu ')      # Enter para trocar de "tela"


        elif opcao == 2:    # ESTATISTICAS
            estatisticas()          # Função que mostra as estatisticas do jogo e jogadores
            enter = input('Precione ENTER para voltar ao Menu ')      # Enter para trocar de "tela"
        
        
        elif opcao == 3:    # SAIR
            break
        
        
        else:       # OPÇÃO INCORRETA
            print('Opção incorreta!')


menu()
