#Elaborado por Samantha Naomi Vital Flores
#20241106
#The filter pattern (filtros)
#Programa que permita crear una lista de todos los numeros menores a 50
numeros=[10,50,25,13,10,28,100,500,29,29]
menores_50=[] #crea una lista vacia
for numero in numeros:
    if numero < 50:
        menores_50.append(numero)
print("La lista original es:" , numeros)
print("La nueva lista es:" , menores_50)
