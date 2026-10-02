dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if divisor == 0:
    print("Erro: não é possível dividir por zero.")
else:
    # Ajustamos para valores absolutos para lidar com as subtrações
    resto = abs(dividendo)
    div_abs = abs(divisor)
    quociente = 0
    
    # Executa a regra matemática proposta no material
    while resto >= div_abs:
        resto -= div_abs
        quociente += 1
        
    # Tratamento simples do sinal matemático final
    if (dividendo < 0 and divisor > 0) or (dividendo > 0 and divisor < 0):
        quociente = -quociente
        
    print(f"O quociente é {quociente}")
