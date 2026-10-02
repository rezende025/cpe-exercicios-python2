d = int(input("Dia: "))
m = int(input("Mês: "))
a = int(input("Ano: "))

# Identifica se é ano bissexto para atuar em fevereiro
bissexto = (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0))

# Mapeia duração, o índice [0] é inútil, permitindo mapeamento direto (índice 1 = mês 1)
dias_mes = [0, 31, 29 if bissexto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Dia seguinte
d_pos, m_pos, a_pos = d + 1, m, a
if d_pos > dias_mes[m]:  # Virou mês
    d_pos = 1
    m_pos += 1
    if m_pos > 12:       # Virou ano
        m_pos = 1
        a_pos += 1

# Dia anterior
d_ant, m_ant, a_ant = d - 1, m, a
if d_ant == 0:           # Voltou pro mês de trás
    m_ant -= 1
    if m_ant == 0:       # Voltou pro ano de trás
        m_ant = 12
        a_ant -= 1
    d_ant = dias_mes[m_ant]

print(f"Data anterior: {d_ant:02d}/{m_ant:02d}/{a_ant}")
print(f"Data original: {d:02d}/{m:02d}/{a}")
print(f"Data seguinte: {d_pos:02d}/{m_pos:02d}/{a_pos}")
