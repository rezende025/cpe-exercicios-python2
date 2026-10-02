def mdc(a, b):
    # Rastreia as repetições do laço
    ciclos = 0
    # Enquanto houver resto, continuamos dividindo
    while b != 0:
        a, b = b, a % b
        ciclos += 1
    return a, ciclos

# 3.1: Testando valores sugeridos
res1, cic1 = mdc(76, 34)
print(f"mdc(76, 34) = {res1} em {cic1} ciclos.")

res2, cic2 = mdc(224, 7)
print(f"mdc(224, 7) = {res2} em {cic2} ciclos.")

# 3.2: Primos entre si
a, b = 15, 8
valor_mdc, _ = mdc(a, b)
if valor_mdc == 1:
    print(f"{a} e {b} são primos entre si.")

# 3.3: Calcular o MMC usando a propriedade matemática fornecida
a, b = 76, 34
valor_mdc, _ = mdc(a, b)
# '//' garante o resultado inteiro exigido
mmc = abs(a * b) // valor_mdc 
print(f"O MMC de {a} e {b} é {mmc}.")
