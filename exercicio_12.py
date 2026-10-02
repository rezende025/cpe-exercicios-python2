lbs = float(input("Digite o peso em Libras (lb): "))

if lbs < 0:
    print("Atenção: Pesos negativos não são aceitos.")
else:
    # Aplica o cálculo e arredonda a exibição de saída
    kg = lbs * 0.453592
    print(f"O peso correspondente é {kg:.2f} kg.")
