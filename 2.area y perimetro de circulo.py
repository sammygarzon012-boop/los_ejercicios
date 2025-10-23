
import math  # Importamos la librería math para usar el valor de π (pi)

# Pedimos el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calculamos el área y el perímetro
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

# Mostramos los resultados
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)