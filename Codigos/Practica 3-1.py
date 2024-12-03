#P-1 Mascotas
#20241028
#Elaborado por Samantha Naomi Vital Flores
#*****************************************
mascota = input("Ingresa el tipo de mascota que tienes:")

if "perro" in mascota:      #Pregunta si la palabra "perro" esta dentro
    print("Es un perro")    #De la variable mascota
elif "gato" in mascota:     #Es un else + if fusionado
    print("Tienes un gato")
else:
    print("Tipo de mascota desconocido")
    
print("¡Gracias por usar nuestros programas!")
