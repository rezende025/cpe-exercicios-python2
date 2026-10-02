pop_a = 50_000_000
pop_b = 70_000_000
anos = 0

while pop_a <= pop_b:
    # Aumentos e juros macro cumulativos compostos
    pop_a = pop_a * 1.03  # + 3 por cento
    pop_b = pop_b * 1.02  # + 2 por cento
    anos += 1

print(f"Demorará especificamente {anos} anos para país A virar o país B e superá-lo.")
print(f"País A: {pop_a:,.0f} vs País B: {pop_b:,.0f}")
