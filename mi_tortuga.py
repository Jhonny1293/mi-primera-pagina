#Reto1
""" print("Simulador del movimiento de una tortuga")
pasos_adelante = int(input("Ingrese la cantidad de pasos hacia adelante: "))
print("-" * pasos_adelante + ">") """

#Reto2
""" pasos_abajo = int(input("Ingrese la cantidad de pasos hacia abajo: "))
for _ in range(pasos_abajo):
    print("|" + "v") """

#Reto3
""" pasos_derecha = int(input("¿Cuántos pasos deseas mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos deseas mover hacia abajo? "))

# Línea horizontal con el giro
print("-" * pasos_derecha + "|")

# Línea vertical hacia abajo
for _ in range(pasos_abajo - 1):
    print(" " * pasos_derecha + "|") """


#Reto4
""" def mover_derecha(pasos):
    # Dibuja la línea horizontal y el giro hacia abajo
    print("-" * pasos + "|")
    

def mover_abajo(pasos, desplazamiento):
    # Dibuja la línea vertical del escalón
    for _ in range(pasos - 1):
        print(" " * desplazamiento + "|")


# --- Programa principal ---

# Primero pedimos los pasos
pasos_derecha = int(input("¿Cuántos pasos mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos mover hacia abajo? "))

# Ahora llamamos a las funciones
mover_derecha(pasos_derecha)
mover_abajo(pasos_abajo, pasos_derecha) """

#Reto5
# Variable global para recordar la posición actual en X
posicion_horizontal = 0


def mover_derecha(pasos):
    global posicion_horizontal
    # aumentamos la posición acumulada
    posicion_horizontal += pasos
    
    # dibujamos la línea horizontal del escalón
    print("-" * pasos + "|")


def mover_abajo(pasos):
    # usamos la posición acumulada para alinear verticalmente
    for _ in range(pasos - 1):
        print(" " * posicion_horizontal + "|")

# Entradas para el usuario
cantidad_escalones = int(input("¿Cuántos escalones deseas bajar? "))

for i in range(cantidad_escalones):
    pasos_derecha = int(input(f"Pasos hacia la derecha del escalón {i+1}: "))
    pasos_abajo = int(input(f"Pasos hacia abajo del escalón {i+1}: "))
    
    mover_derecha(pasos_derecha)
    mover_abajo(pasos_abajo)
