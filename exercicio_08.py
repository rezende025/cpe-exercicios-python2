nome = input("Nome: ")
altura = float(input("Altura em metros (ex: 1.75): "))
# Formata a string para limpar espaços em branco nas pontas e caixa alta
sexo = input("Sexo (M/F): ").strip().upper()

peso_ideal = None # Inicializa para rastreio

# Decide a fórmula a partir do padrão da letra
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Código de sexo não reconhecido.")

if peso_ideal is not None:
    print(f"{nome}, o seu peso ideal é {peso_ideal:.2f} kg.")
