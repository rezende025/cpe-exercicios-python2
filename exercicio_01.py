n = int(input("Digite um número não negativo: "))

# Validação do limite inferior
if n < 0:
    print("Número inválido. Insira um valor maior ou igual a zero.")
else:
    fatorial = 1 # 1 é o elemento neutro da multiplicação
    
    # Percorre de 1 até n (o +1 inclui o n no limite do range)
    for i in range(1, n + 1):
        fatorial *= i
        
    print(f"{n}! = {fatorial}")
