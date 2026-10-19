hitortial_navegacion = []

hitortial_navegacion.append("google.com")
hitortial_navegacion.append("youtube.com")
hitortial_navegacion.append("wikipedia.org")

print("historial_cargado", hitortial_navegacion)
#operacion cima(top/peek)
pagina_actual = hitortial_navegacion[-1]
print("Pagina actual en pantalla" , pagina_actual)

#Operacion de desapilar(pop)
pagina_cerrada = hitortial_navegacion.pop()
print("Saliendo  de" , pagina_cerrada)

print("Historial despues de precionar 'atras': " , hitortial_navegacion)

#Tamaño de la pila
total_paginas=len(hitortial_navegacion)
print("Paginas previas guaradas: " , total_paginas)

#Operacio vacia (empty)
sin_paginas=len(hitortial_navegacion) == 0
print("¿El hsitorial esta vacioss ?", sin_paginas)

