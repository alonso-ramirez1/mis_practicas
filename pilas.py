pila = []
print("Paso 1: Pila creada ->", pila)
for i in range(1, 11):
    pila.append(f"Plato {i}")
print("")
print("Paso 2: Pila con 10 elementos ->", pila)
if pila:
    cima = pila[-1]
    print("Paso 3: Elemento en la cima (Top) ->", cima)
print("")
print("\nPaso 4: Desapilando 4 elementos:")
for _ in range(4):
    plato_retirado = pila.pop()
    print(f"  - Elemento retirado: {plato_retirado}")
print("Pila actual ->", pila)
tamano = len(pila)
esta_vacia = len(pila) == 0
print(f"\nPaso 5: Tamaño actual de la pila: {tamano}")
print("")
print(f"¿La pila está vacía?: {esta_vacia}")
print("")
print("\nPaso 6 (EXTRA): Vaciando la pila completamente:")
while len(pila) > 0:
    elemento = pila.pop()
    print(f"  - Eliminando: {elemento}")
print("\nEstado final de la pila ->", pila)
print(f"¿La pila está vacía?: {len(pila) == 0}")
print("")