#Elaborado por Samantha Naomi Vital Flores
#20241031
#p-9  Igualdad de listas
#Compare puntos con todas las demas listas
puntos=[10, 30, 20]
puntos_2=[10, 30, 20]
ordenados=[10, 20, 30]
puntos_texto=["10", "30", "20"]

print(puntos==puntos_2) #True
print(puntos==ordenados) #False
print(puntos==puntos_texto) #False

print(puntos!=puntos_2) #False
print(puntos!=ordenados) #True
print(puntos!=puntos_texto) #True