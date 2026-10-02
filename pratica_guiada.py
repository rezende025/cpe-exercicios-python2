# Inicializa o acumulador de leituras quentes
contagem_quente = 0

# Repete a leitura 5 vezes
for leitura in range(5):
    t = float(input("Temperatura: "))
    
    # Classifica a temperatura baseada nas faixas do exercício
    if t < 15:
        print("FRIO")
    elif t < 30: 
        print("CONFORTÁVEL")
    else:
        print("QUENTE")
        contagem_quente += 1 # Incrementa apenas nas temperaturas altas

print(f"Total de temperaturas QUENTES: {contagem_quente}")
