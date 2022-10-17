texto = input("Digite uma frase: ")

print("Tem espaços?",texto.isspace())
print("É alfabetico?",texto.isalpha())
print("É Alfanumérico?", texto.isalnum())
print("É Alfanumérico e tem espaços?", texto.replace(' ', '').isalnum())
print("É numero?",texto.isnumeric())
print("Espaço entre textos?", ' ' in texto)