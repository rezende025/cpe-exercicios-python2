n = int(input("O número matriz superior: "))

maior_divisor_interno = 1 # 1 é base trivial obrigatória geral e universal

# Ele roda pela metade restritamente (int def), e cai inversamente (-1 param)
if n > 1:
    for rastreio in range(n // 2, 0, -1):
        if n % rastreio == 0:
            maior_divisor_interno = rastreio
            # Acerta e cessa o rasteio no mesmo segundo pra pular gasto atômico
            break
            
print(f"O imenso e único maior divisor atrelado próprio para raiz {n} atinge: {maior_divisor_interno}")
