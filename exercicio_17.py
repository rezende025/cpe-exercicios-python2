def pode_alistar(idade, sexo, idade_min, idade_max):
    # Condiciona as garantias num único retorno direto
    sexo_valido = sexo.strip().upper() == "M"
    idade_valida = idade_min <= idade <= idade_max
    
    # Retorna True apenas se ambos os polos acima forem confirmados
    return sexo_valido and idade_valida

# Bloco para uso e teste
i = int(input("Idade: "))
s = input("Sexo (M/F): ")
mini = int(input("Idade mínima de alistamento: "))
maxi = int(input("Idade máxima de alistamento: "))

if pode_alistar(i, s, mini, maxi):
    print("O alistamento é obrigatório e está na faixa.")
else:
    print("Fora das regras e da faixa de convocação.")
