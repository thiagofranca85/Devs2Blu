
def media(nome, n1, n2, n3):
    med = (n1+n2+n3)/3
    print("Nome: ", nome)
    print("Nota 1", n1)
    print("Nota 2", n2)
    print("Nota 3", n3)
    print(f"Média - {med:.1f}")
    if med >= 7:
        print("Você foi aprovado.")
    else:
        print("Você foi reprovado.")
