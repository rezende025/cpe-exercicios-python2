codigo_idioma = input("Digite es, ptbr ou en: ").strip().lower()

# O match analisa a variável do topo contra cenários fixos explícitos
match codigo_idioma:
    case "es":
        print("¡Soy un traductor!")
    case "ptbr":
        print("Sou um tradutor!")
    case "en":
        print("I am a translator!")
    case _:
        # Case underline substitui o 'else' ou valor coringa não previsto
        print("Código de idioma desconhecido.")
