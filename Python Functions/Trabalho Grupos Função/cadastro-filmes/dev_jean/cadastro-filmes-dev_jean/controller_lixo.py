def mostraPessoasBonito(listaPessoas):
    print("\n")
    for line in listaPessoas:
        tabID = " "*(5-len(str(line["ID"])))
        print("ID:" + str(line["ID"]) + tabID + " Nome: " + line["nome"])
    print("\n")

def relatorioPessoas():
    pessoasAretornar = []
    
    with open('pessoas.txt', 'r') as reader:
        
        for line in reader:
            aux = ast.literal_eval(line)
            if aux['checkin'] == '1':
                pessoasAretornar.append(aux)
                #print(aux)
        return pessoasAretornar


def existePessoa(pessoa): #Recebe o [dicionario] pessoa e verifica se ela existe no arquivo e retorna apenas true or false
    with open('pessoas.txt', 'r') as reader:

        for line in reader:
            aux = ast.literal_eval(line)
            if aux['ID'] == pessoa['ID'] or aux['nome'] == pessoa['nome']:
                return True
    return False



#Encontra a pessoa no arquivo e atualiza os dados desta pessoa. 
#Se check for passado ele altera o status de checIn/Out da pessoa;

def editaPessoa(titulo, check=False):
    
    with open('pessoas.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        pessoa = eval(pessoa)
        if check:
            print(pessoa)
            pessoa['checkin'] = 1
        else:
            pessoa['checkin'] = 0
            
        for i in range (len(data)):
            aux = eval(data[i])

            #print(aux['ID'])
            #print(str(pessoa))
            
            if aux['ID'] == pessoa['ID']:
                data[i] = str(pessoa)+"\n"

    # and write everything back
    with open('pessoas.txt', 'w') as file:
        file.writelines( data )


