#Irvin Vásquez Figueroa
#A01541101
#Objetivo: pedir apellidos e imprimir datos de estos.
apellido_paterno = (input("¿Cuál es tu apellido paterno?"))
apellido_materno = (input("¿Y el materno?"))
#Se piden los apellidos al usuario.

print("Tu apellido paterno tiene ",len(apellido_paterno) , "letras")
#Se imprime la longitud del apellido paterno. Es decir, cuántas letras tiene.

x = 0
for letras in apellido_materno:
    #Se hace un ciclo for que va recorriendo cada letra del apellido materno
    if letras.lower() in "a e i o u":
        #Se hace un if, en donde primero se convierten las letras del apellido en minúscula
        #Después, si la letra en la que se va recorriendo es alguna vocal, se le suma 1 al contador.
        x = x+1
print ("Tu apellido materno tiene " , x, " vocales")
#Se imprime el número de vocales que tiene

print(apellido_paterno,"$$$",apellido_materno)
#Se imprimen ambos apellidos con el símbolo de dinero en medio.
