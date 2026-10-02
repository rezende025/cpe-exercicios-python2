# Laço externo focado na varredura das famílias numéricas até o final
for tabuada in range(1, 10):
    print(f"\n--- Tabuada do {tabuada} ---")
    
    # Laço operante focado nos passos matemáticos de cálculo individual
    for multiplicador in range(1, 11):
        resultado = tabuada * multiplicador
        print(f"{tabuada} x {multiplicador} = {resultado}")
