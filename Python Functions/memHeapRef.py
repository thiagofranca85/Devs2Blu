class main():
    def __init__(self) -> None:
        self.a = 10
        self.b = 10

def trocar(c: main):
    c.a = 100

c = main()

print(c.a)

trocar(c)

print(c.a)