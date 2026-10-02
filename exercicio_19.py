limite = int(input("Indique o valor teto para Fibonacci: "))

# Inicia as duas unidades primordiais de progressão
a, b = 0, 1

# O laço para se o valor atual a ser exibido já passa da regra teto
while a <= limite:
    # Parametriza a saída linear numa mesma fileira no painel
    print(a, end=" ")
    
    # Esta instrução chave computa a alteração sem a variável apagar as ref
    a, b = b, a + b
