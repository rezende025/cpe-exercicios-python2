# Mapeia colunas extensas das rotinas mestre super dimensionais
for linha_extensiva_maior in range(9):
    # Desenha cruzamentos do quadrante colunar local alinhado internamente
    for coluna_profunda in range(9):
        # A magia de intersecção: na diagonal perfeita ambos valem sempre números pareados casuais exatos
        if linha_extensiva_maior == coluna_profunda:
            # End isola e cimenta a lacuna na direita
            print("O", end="")
        else:
            # Lacuna coberta natural pelas restrições alheias cruzadas
            print("X", end="")
            
    # Fornece o enter obrigatório na base antes do sistema recomeçar
    print()
