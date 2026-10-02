num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))

if num1 > num2:
    print(f"O maior é o primeiro: {num1}")
elif num2 > num1:
    print(f"O maior é o segundo: {num2}")
else:
    print("Os dois valores fornecidos são idênticos.")
