nome = input("Alerte o seu nome original livre: ")
novo_nome = ""

# Substituição de Z no laço relacional perante avaliação condicional in
for letra in nome:
    if letra.lower() in "aeiouáéíóúâêîôûãõ":
        # Evitando complexidade excessiva entre maiúsculas, joga direto pra z livre
        novo_nome += "z"
    else:
        novo_nome += letra
        
print(f"Nome substituído nas regras paramétricas zzz: {novo_nome}")

nome_reverso = novo_nome[::-1] 

print(f"O nome bizarramente em reverso final fica: {nome_reverso}")
