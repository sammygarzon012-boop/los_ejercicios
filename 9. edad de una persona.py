# Pedir fecha de nacimiento 

anio = int(input("Ingrese su año de nacimiento: ")) 

mes = int(input("Ingrese su mes de nacimiento (1-12): ")) 

dia = int(input("Ingrese su día de nacimiento: ")) 

  

# Fecha actual 

hoy = date.today()  # type: ignore

  

# Calcular edad 

edad = hoy.year - anio 

  

# Ajustar si aún no ha cumplido años este año 

if (hoy.month, hoy.day) < (mes, dia): 

    edad -= 1 

  

print(f"La edad es: {edad} años") 