num = int(input("Ingrese un número: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("El factorial de", num, "es:", fact)
