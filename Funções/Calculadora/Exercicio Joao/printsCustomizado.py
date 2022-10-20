def headerPrint(text = '', colored = False, caracter = '-', size = 55):
    if colored: adjust = 11
    else: adjust = 0
    print(f"{text}".center(size+adjust, caracter))

def tablePrint(text, istitle = False, colored = False, size = 55):
    if colored: adjust = 10
    else: adjust = -1
    if istitle:
        print(f"{text}".center(size+adjust, ' '), end= '')
        print("|")
    else:
        print(f"{text}".ljust(size+adjust), end= '')
        print("|")
