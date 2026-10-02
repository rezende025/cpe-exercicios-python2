valor = float(input("Digite o valor numérico da temperatura: "))
uni_ori = input("Unidade de origem (C, K, F): ").strip().upper()
uni_dest = input("Unidade de destino (C, K, F): ").strip().upper()

celsius = None

# Etapa 1: Levar qualquer valor obrigatoriamente para Celsius
if uni_ori == "C":
    celsius = valor
elif uni_ori == "K":
    celsius = valor - 273.15
elif uni_ori == "F":
    celsius = (valor - 32) / 1.8
else:
    print("Origem desconhecida.")

# Etapa 2: A partir de Celsius recém-coletado, levar para destino
if celsius is not None:
    if uni_dest == "C":
        resultado = celsius
    elif uni_dest == "K":
        resultado = celsius + 273.15
    elif uni_dest == "F":
        resultado = celsius * 1.8 + 32
    else:
        print("Destino desconhecido.")
        resultado = None
        
    if resultado is not None:
        print(f"Temperatura convertida: {resultado:.2f} {uni_dest}")
