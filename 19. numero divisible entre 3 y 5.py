 # Determinar si un número es divisible entre 3 o 5 

  

numero = int(input("Ingrese un número: ")) 

  

if numero % 3 == 0 and numero % 5 == 0: 

    print(f"El número {numero} es divisible entre 3 y 5") 

elif numero % 3 == 0: 

    print(f"El número {numero} es divisible entre 3") 

elif numero % 5 == 0: 

    print(f"El número {numero} es divisible entre 5") 

else: 

    print(f"El número {numero} NO es divisible ni entre 3 ni entre 5") 