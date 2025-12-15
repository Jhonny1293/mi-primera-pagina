#Reto1
print("Simulador del movimiento de una tortuga")
pasos_adelante = int(input("Ingrese la cantidad de pasos hacia adelante: "))
print("-" * pasos_adelante + ">")

#Reto2
pasos_abajo = int(input("Ingrese la cantidad de pasos hacia abajo: "))
for _ in range(pasos_abajo):
    print("|" + "v")

#Reto3
pasos_derecha = int(input("¿Cuántos pasos deseas mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos deseas mover hacia abajo? "))

# Línea horizontal con el giro
print("-" * pasos_derecha + "|")

# Línea vertical hacia abajo
for _ in range(pasos_abajo - 1):
    print(" " * pasos_derecha + "|")


#Reto4
def mover_derecha(pasos):
    # Dibuja la línea horizontal y el giro hacia abajo
    print("-" * pasos + "|")
    

def mover_abajo(pasos, desplazamiento):
    # Dibuja la línea vertical del escalón
    for _ in range(pasos - 1):
        print(" " * desplazamiento + "|")


# Primero pedimos los pasos
pasos_derecha = int(input("¿Cuántos pasos mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos mover hacia abajo? "))

# Ahora llamamos a las funciones
mover_derecha(pasos_derecha)
mover_abajo(pasos_abajo, pasos_derecha)

#Reto5
x = 0

def mover_derecha(pasos):
    global x
    print(" " * x + "-" * pasos + "|")
    x += pasos

def mover_abajo(pasos):
    global x
    for _ in range(pasos - 1):
        print(" " * x + "|")

mover_derecha(4)
mover_abajo(4)

mover_derecha(5)
mover_abajo(5)

mover_derecha(6)
mover_abajo(6)
