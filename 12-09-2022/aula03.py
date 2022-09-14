# Estrutura de decisao

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

print(f"Sua media {media}")
if media > 7:
    print("Voce esta acima da media")
elif media == 7:
    print("Voce atingiu a media.")
else:
    print("Voce nao atingiu a media")