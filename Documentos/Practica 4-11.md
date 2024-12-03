Elaborado por Samantha Naomi Vital Flores

20241108

"""Programa que se repite hasta que

ingrese la palabra ´salir´"""

Inicialización de variables
```
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o ´salir´ para terminar: ")
    palabra = palabra.lower() #Convierte la palabra en minúsculas
    print("Usted ingresó:", palabra)
print("Fin del programa")
````
