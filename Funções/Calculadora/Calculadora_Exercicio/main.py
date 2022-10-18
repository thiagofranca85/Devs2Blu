from controller import soma,subtracao,multiplicacao,divisao

operacoes = ['+','-','*','/']
poli = "="*30

print(poli)
print(f" Calculadora ".center(30,"="))
print(poli)
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(f"{poli}\n")

while True:
    opcao = input("Digite + para somar.\nDigite - para subtrair.\nDigite * para multiplicar.\nDigite / para dividir.\n>> ")
    if not opcao in operacoes:
        print(f"{poli}\nDigite uma opcao valida.\n{poli}")

    if opcao == '+':
        print(f"{poli}\nResultado: {soma(n1,n2)}\n{poli}")
        break
    if opcao == '-':
        print(f"{poli}\nResultado: {subtracao(n1,n2)}\n{poli}")
        break
    if opcao == '*':
        print(f"{poli}\nResultado: {multiplicacao(n1,n2)}\n{poli}")
        break
    if opcao == '/':
        print(f"{poli}\nResultado: {divisao(n1,n2)}\n{poli}")
        break

