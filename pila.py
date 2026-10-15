historial_navegacion=[]
historial_navegacion.append=("google.com")
historial_navegacion.append=("youtube.com")
historial_navegacion.append=("wikipedia.com")
print("Historial cargado",historial_navegacion)

#OPERACIONES CIMA(TOP/PEEK)
pagina_actual=historial_navegacion[-1]
print("pagina acual de la pantalla", pagina_actual)

#OPERACION DESAPILAR(POP)
pagina_cerrada=historial_navegacion.pop()
print("SALIENDO DE ", pagina_cerrada)
print("Historial mdespues depresinar 'Atras' : ",historial_navegacion)

#TAMAÑO DE LA PILA
total_paginas=len(historial_navegacion)
print("Paginas previas guardads: ", total_paginas)

#OPERACION VACIA (EMPTY)
sin_paginas=len(historial_navegacion)==0
print("¿El historial esta vacio? ", sin_paginas)        