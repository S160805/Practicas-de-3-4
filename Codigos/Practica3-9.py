#Elaborado por Samantha Naomi Vital Flores
#20241108
"""Programa que demuestre el uso de los comandos
\"break\"y \"continue\" """

#EJEMPLO 1 - break
#pero si el numero es 5
#salir del ciclo while
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 #Equivale a i = i + 1
print("Fin del programa")

#ejemplo 2 - continue
#Imprimir los numeros del 1 al 10,
#pero si el numero es 5, omitirlo
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("Fin del programa")
