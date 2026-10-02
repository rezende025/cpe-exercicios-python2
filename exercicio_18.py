nota = float(input("Nota da disciplina (0 a 10): "))

if nota < 0 or nota > 10:
    print("Erro matemático: Faixa inválida informada.")
else:
    if nota >= 9:
        mencao = "SS" 
    elif nota >= 7:
        mencao = "MS" 
    elif nota >= 5:
        mencao = "MM"
    elif nota >= 3:
        mencao = "MI"
    else:
        mencao = "II"
        
    print(f"A sua avaliação menção é: {mencao}")
