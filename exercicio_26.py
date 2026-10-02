import math

def fatorial(n):
    if n < 0:
        return None
    acumulador = 1
    for cont em range(1, n + 1):
        acumulador *= cont
    return acumulador

n_teste = 6

resultado_meu = fatorial(n_teste)
resultado_oficial = math.factorial(n_teste)

print(f"Sintético: {resultado_meu} | Algoritmo Python C Nativo: {resultado_oficial}")
print(f"As validações de paridade dão positivo? {resultado_meu == resultado_oficial}")
