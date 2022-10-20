def salvar(nome):
    with open('modulo2/pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('modulo2/pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes

salvar('Thiago')
print('Lista de Nomes',listar())