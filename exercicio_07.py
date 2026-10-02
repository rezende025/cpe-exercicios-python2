hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

# Condição em que o jogo vira o dia ou dura exatas 24 horas
if hora_final <= hora_inicial:
    # Da hora inicial até às 24, somado ao que passou do zero no novo dia
    duracao = (24 - hora_inicial) + hora_final
else:
    # Terminou no mesmo dia
    duracao = hora_final - hora_inicial

print(f"O jogo durou {duracao} hora(s).")
