# PROGRAMA 1 (Com FOR)
contador = 1
for _ in range(5):
    contador = 1
    print(contador)
# A saída é 1, 1, 1, 1, 1. Termina porque o limite do 'for' 
# é controlado de forma invisível pelo range(5), e não pela variável 'contador'.

print("---")

# PROGRAMA 2 (Com WHILE - CORRIGIDO)
contador = 1
while contador <= 5:
    # Se a linha "contador = 1" ficasse aqui, a condição 'contador <= 5' 
    # seria sempre 'True', causando loop infinito.
    print(contador)
    contador += 1
