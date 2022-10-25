from time import sleep
def contador(inicio, fim, passo):
    print('-'*35)
    passo = abs(passo) if passo != 0 else 1 
    # Definindo o passo com o valor absoluto (deixa sinal positivo),
    # e caso seja zero, recebe 1
    print(f'Contagem de {inicio} ate {fim}, de {passo} em {passo}')
    sleep(1.5)

    if inicio < fim:
        for cont in range(inicio, fim + 1, passo):
            print(cont, end='')
            sleep(0.3)
    elif inicio > fim:
        for cont in range(inicio, fim, - passo):
            print(cont, end='')
            sleep(0.3)
    print('\nFuncionando')

# Inserindo os dados e colocando os atributos.
contador(10, 30, 2)

print('')
print('-'*35, "Personalize seu For ", '-'*35)
# Aqui os parametros são passados pelos inputs.
contador(int(input("Inicio: ")), int(input("Fim: ")),int(input("Passo: ")))