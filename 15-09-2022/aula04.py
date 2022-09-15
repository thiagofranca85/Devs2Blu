cond = 'sim'
while cond == 'sim':
    cond = str(input("Digite algo: "))
    print(f"O nome digitado foi {cond}")
    cond = str(input('Deseja continuar? \nsim\nnao\n:> '))

print("Voce saiu do programa.")