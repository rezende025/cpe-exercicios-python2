n = int(input("Digite um número natural: "))
soma = 0
k = 1 # Variável que representará a sequência de naturais 1, 2, 3...

# Continua somando enquanto o acumulador for menor que o número alvo
while soma < n:
    soma += k
    k += 1

# Após o laço, verifica se encerrou exatamente em n ou passou direto
if soma == n:
    print(f"{n} é um número triangular!")
else:
    print(f"{n} não é um número triangular.")
