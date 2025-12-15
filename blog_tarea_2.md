# Tarea 2 - Ejercicios Unidad 1

##  Reto 1: simula el comportamiento de la tortuga usando solo print() e input().
Intenta recrear el movimiento de la tortuga únicamente con texto, usando funciones, print() y input() para pedir valores al usuario.

### Solución Reto 1.
print("Simulador del movimiento de una tortuga")
pasos_adelante = int(input("Ingrese la cantidad de pasos: "))
print("-" * pasos_adelante)

La solución consiste en mostrar primero al usuario un mensaje informando que se va a trabajar sobre la simulación del movimiento de una tortuga. Luego, se almacena en una variable un dato de tipo int que hace referencia a la cantidad de pasos que se desean simular hacia adelante y luego, se imprime el resultado del valor de la variable pasos_adelante multiplicado por el string "-"

##  Reto 2: Tortuga bajando.
Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente print() e input().


### Solución Reto 2.
pasos_abajo = int(input("Ingrese la cantidad de pasos hacia abajo: "))
for _ in range(pasos_abajo):
    print("|")

La solución consiste en almacenar en la varibale pasos_abajo el valor de un dato tipo entero que ingresa el usuario. Luego, se crea una iteración que usa como rango el valor obtenido previamente en pasos_abajo para imprimir el string "|" esa cantidad de veces.

##  Reto 3: Girar y dibujar usando solo print() e input().
Ahora la tortuga no solo avanza: también gira.

### Solución Reto 3.
pasos_derecha = int(input("¿Cuántos pasos deseas mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos deseas mover hacia abajo? "))

print("-" * pasos_derecha + "|")

for _ in range(pasos_abajo - 1):
    print(" " * pasos_derecha + "|")

La solución consiste en preguntar incialmente la cantidad de pasos que se desean dar tanto hacia la derecha como hacia abajo y se almacenan en variables separadas. 
Luego, se dibujan los strings "-" para mostrar pasos hacia adelante y "|" para mostrar pasos hacia abajo, de acuerdo al valor que se contiene en cada variable.

##  Reto 4: Encapsula los comportamientos anteriores usando funciones.
Reescribe los retos anteriores creando funciones que representen los movimientos de la tortuga solo con texto.

### Solución Reto 4.
def mover_derecha(pasos):
    # Dibuja la línea horizontal y el giro hacia abajo
    print("-" * pasos + "|")
    

def mover_abajo(pasos, desplazamiento):
    # Dibuja la línea vertical del escalón
    for _ in range(pasos - 1):
        print(" " * desplazamiento + "|")


pasos_derecha = int(input("¿Cuántos pasos mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos mover hacia abajo? "))

mover_derecha(pasos_derecha)
mover_abajo(pasos_abajo, pasos_derecha)

En la solución planteada se crean dos funciones. La primera permite generar un desplazamiento hacia la derecha y la segunda hacia abajo. Luego, se definen la cantidad de pasos a la derecha y abajo preguntando al usuario en la interfaz y finalmente, se ejecutan las funciones con la cantidad de pasos ingresados como parámetros de las funciones.

##  Reto 5: La tortuga baja las escalas.
Ajusta tus funciones para que la tortuga pueda bajar escalones.
Cada escalón debe conservar la posición horizontal acumulada y dibujar correctamente tanto el tramo horizontal como el vertical.

### Solución Reto 5.
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

Para lograr la solución de este reto, inicialmente se tenía que pensar la forma de guardar la posición de la tortuga a medida que hace recorridos hacia la derecha. Esta vez, en las funciones mover_derecha y mover_abajo se dibuja desde la posición actual y se actualiza la posición.
Finalmente, se llaman a las funciones la cantidad de veces que se quiera de acuerdo al número de escalones que se deseen observar en la interfaz.
