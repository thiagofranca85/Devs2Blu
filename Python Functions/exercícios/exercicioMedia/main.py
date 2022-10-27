# Faça um programa que solicite o nome de um aluno solicite também a inserção das últimas três notas este 
# cálculo deve realizar a média desse aluno, e através desta condição deve ser impresso o nome do aluno , 
# as três notas digitadas e a média final, e deve ser impresso se o aluno foi aprovado ou nao!
from controller import media

def menu():
    nome = input("Nome: ")
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    n3 = int(input("Nota 3: "))
    media(nome,n1,n2,n3)

menu()