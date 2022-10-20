from printsCustomizado import *
from math import sqrt

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
CLEANCOLOR = '\033[0;0m'

def customSum(numbers):
    return sum(numbers)

def customSubtract(numbers):
    if len(numbers) == 1: return numbers[0]
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    
    return result

def customDivide(num1, num2):
    if num2 == 0: return "Números não podem ser divididos por 0"
    return num1 / num2
    

def customMultiply(numbers):
    if len(numbers) == 1: return numbers[0]
    result = 1
    for number in numbers:
        result *= number
    
    return result

def wagesSum(numbers):
    return sum(numbers)

def menu():
    headerPrint('== SEJA BEM-VINDO ==')
    tablePrint(f"{RED}FUNÇÕES{CLEANCOLOR}", True, True)
    tablePrint('Somar - 1')
    tablePrint('Subtrair - 2')
    tablePrint('Dividir - 3')
    tablePrint('Multiplicar - 4')
    tablePrint('Calculo avançado - 5')
    headerPrint()

def advancedMenu():
    headerPrint('== CALCULADORA AVANÇADA ==')
    tablePrint(f"{RED}TUTORIAL{CLEANCOLOR}", True, True)
    tablePrint('Somar = +')
    tablePrint('Subtrair = -')
    tablePrint('Dividir = /')
    tablePrint('Multiplicar = *')
    tablePrint('Elevar = **')
    tablePrint('Raiz quadrada = sqrt()')
    tablePrint('Parenteses podem ser usados para indicar prioridade!')
    headerPrint()