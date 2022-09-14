
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

print(f"Sua media {media}")

# Quando tiver ate 2 condicoes ..
print("Parabens voce atingiu a media. " if media >=7 else "Voce nao atingiu a media. ")