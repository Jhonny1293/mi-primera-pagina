# Tarea 2 - Ejercicios Unidad 1

##  Reto1: simula el comportamiento de la tortuga usando solo print() e input().
Intenta recrear el movimiento de la tortuga únicamente con texto, usando funciones, print() y input() para pedir valores al usuario.

### Solución Reto1.
print("Simulador del movimiento de una tortuga")
pasos_adelante = int(input("Ingrese la cantidad de pasos: "))
print("-" * pasos_adelante)

La solución consiste en mostrar primero al usuario un mensaje informando que se va a trabajar sobre la simulación del movimiento de una tortuga. Luego, se almacena en una variable un dato de tipo int que hace referencia a la cantidad de pasos que se desean simular hacia adelante y luego, se imprime el resultado del valor de la variable pasos_adelante multiplicado por el string "-"

##  Reto 2: Tortuga bajando.
Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente print() e input().


### Solución Reto2.
pasos_abajo = int(input("Ingrese la cantidad de pasos hacia abajo: "))
for _ in range(pasos_abajo):
    print("|")

La solución consiste en almacenar en la varibale pasos_abajo el valor de un dato tipo entero que ingresa el usuario. Luego, se crea una iteración que usa como rango el valor obtenido previamente en pasos_abajo para imprimir el string "|" esa cantidad de veces.

##  Reto 3: Girar y dibujar usando solo print() e input().
Ahora la tortuga no solo avanza: también gira.

### Solución Reto3.
pasos_derecha = int(input("¿Cuántos pasos deseas mover hacia la derecha? "))
pasos_abajo = int(input("¿Cuántos pasos deseas mover hacia abajo? "))

print("-" * pasos_derecha + "|")

for _ in range(pasos_abajo - 1):
    print(" " * pasos_derecha + "|")

La solución consiste en preguntar incialmente la cantidad de pasos que se desean dar tanto hacia la derecha como hacia abajo y se almacenan en variables separadas. 
Luego, se dibujan los strings "-" para mostrar pasos hacia adelante y "|" para mostrar pasos hacia abajo, de acuerdo al valor que se contiene en cada variable.
