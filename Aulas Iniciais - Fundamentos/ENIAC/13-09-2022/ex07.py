border = "="*5
num = int(input("Qual tabuada você quer saber: "))

print(f"{border} Tabuada de {num} {border}")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print(border*5)