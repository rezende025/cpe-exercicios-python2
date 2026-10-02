idade = int(input("Sua idade: "))
trabalho = int(input("Tempo de trabalho (anos): "))

# Avalia as condições como escritas na especificação.
# O uso dos parênteses isola a regra mista que precisa ocorrer simultaneamente.
if (idade >= 65) or (trabalho >= 30) or (idade >= 60 and trabalho >= 25):
    print("Você pode requerer aposentadoria.")
else:
    print("Você não preenche os requisitos para aposentadoria.")
