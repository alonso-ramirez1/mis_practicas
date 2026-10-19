platos = []
platos.append("Plato_1")
platos.append("Plato_2")
platos.append("Plato_3")
platos.append("Plato_4")
platos.append("Plato_5")
platos.append("Plato_6")
platos.append("Plato_7")
platos.append("Plato_8")
platos.append("Plato_9")
platos.append("Plato_10")
print("Lista de paltos" , platos)
#operacion cima(top/peek)
platos_nuevos = platos[-1]
print("Platos actuales de la lista" , platos_nuevos)
#Operacion de desapilar(pop)
print("Operacion de desapilar")
for i in range(4):
    platos_elimidados = platos.pop()
    print("Los paltos elimidados son :", platos_elimidados)

#Tamaño de la pila
platos_restantes = len(platos)
print("Los platos restantes :" , platos_restantes)

#Operacio vacia (empty)
sin_platos = len(platos) == 0
print("¿La pila esta vacia?:" , sin_platos)

#ciclo while paso extra
while len(platos) > 0:
    platos_elimidados = platos.pop()
    print("Plato elimidado :" , platos_elimidados)
sin_platos = len(platos) == 0
print("¿Ya no hay platos?:" , sin_platos)