# Determinar el menor de 3 números 

num1 = float(input("Ingrese el primer número: ")) 

num2 = float(input("Ingrese el segundo número: ")) 

num3 = float(input("Ingrese el tercer número: ")) 

  

if num1 <= num2 and num1 <= num3: 

    menor = num1 

elif num2 <= num1 and num2 <= num3: 

    menor = num2 

else: 

    menor = num3 