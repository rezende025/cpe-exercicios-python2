h = int(input("Altura da pirâmide: "))

for i in range(1, h + 1):
    # A base mais baixa tem 0 espaços. A de cima tem h - i.
    espacos = " " * (h - i)
    # Segundo o PDF, os asteriscos seguem a fórmula 2 * i
    asteriscos = "*" * (2 * i)
    
    print(espacos + asteriscos)
