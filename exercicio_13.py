n = float(input("Insira o seu número da sorte: "))

# Compara as faixas pedidas diretamente de forma sequencial limpa
if 8 <= n <= 12 or n > 33:
    print("Você ganhou!")
else:
    print("Não foi dessa vez.")
