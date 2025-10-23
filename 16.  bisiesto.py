# Determinar si un año es bisiesto 

  

anio = int(input("Ingrese un año: ")) 

  

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0): 

    print(f"El año {anio} es BISIESTO") 

else: 

    print(f"El año {anio} NO es bisiesto") 