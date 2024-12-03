#Patrones para ciclos
#(Loops Patterns)
#The count pattern
letras= ["a", "b", "c", "d", "e"]
contador=0 #inicializa variable
for letra in letras:
    contador=contador+1
print("La lista \"letras\"tiene", contador, "letras")


#The sum pattern
numeros=[100, 200, 300, 400]
sumatoria=0 #Inicialización
for numero in numeros:
    sumatoria=sumatoria+numero
print("La sumatoria es", sumatoria)


#The accumulation pattern
palabras=["Hoy", " ","Hace", " ", "Frío"]
mensaje=""
for palabra in palabras:
    mensaje=mensaje+palabra
print(mensaje)

#The Map pattern
#Sirve para "mapear" cada uno de los elementos de una nueva variable.
#Por ejemplo, para crear una lista idéntica nueva desde otra ya existente
lista_anterior= ["Mnazana", "Piña", "Uva"]
lista_nueva=[]
print("La lista vacia", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es", lista_nueva)