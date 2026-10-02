# A lista indexa meses do espaço [0] a [11]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

num = int(input("Insira o número do mês (1 a 12): "))

# Garante a integridade e impede erros fora do índice
if 1 <= num <= 12:
    print(meses[num - 1])
else:
    print("Mês inválido.")
