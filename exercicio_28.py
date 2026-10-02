numero_inserido_plano = int(input("Componha o número imenso integral a tratar: "))
numero_operante = abs(numero_inserido_plano)
totalidade_soma_parcial = 0

while numero_operante > 0:
    digito_individual_recente = numero_operante % 10 
    totalidade_soma_parcial += digito_individual_recente
    
    # Arranca fora as casas extintas sem poluir o decímal fracionário base e trunca
    numero_operante //= 10
    
print(f"As casas soltas atreladas compiladas equivalem atômicas a: {totalidade_soma_parcial}")
