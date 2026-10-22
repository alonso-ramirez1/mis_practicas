from collections import deque
import time 
cola_reproduccion=deque()
#Agrega elementos de reproduccion
cola_reproduccion.append("1.- Mochila azul")
cola_reproduccion.append("2.- Aerolinea carrillo")
cola_reproduccion.append("3.- La calabaza")
#Mostrar las canciones en esspera
print("Canciones en espera: ")
for cancion in cola_reproduccion:
    print(" _", cancion)
    print("INICIANDO REPRODUCCION")
#Desencolar
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora: {cancion_actual}")
    time.sleep(1) #Simula la duracion del tema
    print(f"Finalizo {cancion_actual}")
    #Muestra cuantas canciones quedan en la cola
    print(f"(Quedan {len(cola_reproduccion)} canciones en la cola)")
    print("LA COLA DE REPRODUCCION HA FINALZADO")