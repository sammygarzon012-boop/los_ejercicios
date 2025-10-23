positivos = 0
negativos = 0

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    elif num > 0:
        positivos += 1
    else:
        negativos += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
