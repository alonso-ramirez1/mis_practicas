def mostrar_encabezado_escuela():
    print("=================================================")
    print(" UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DE JUAREZ")
    print("    REGISTRO Y EVALUACION DE CALIFICACIONES")
    print("=================================================")
    print("")

def obtener_nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    mostrar_encabezado_escuela()
    
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    
    print(f"Alumno: {nombre_alumno}")
    print(f"Nota de Exámenes: {nota_examenes}")
    print(f"Nota de Tareas: {nota_tareas}")
    print(f"Calificación Final: {nota_final}")
    print(f"Estado Académico: {estado}")
    
    if nota_final < nota_minima:
        print("Requiere presentar examen extraordinario: SÍ")
    else:
        print("Requiere presentar examen extraordinario: NO")

    print("")
    print("=================================================")

generar_boleta("Brian Alonso Ramirez Cazarez", 8.5, 9)
print("-----------------------------------------------------")
generar_boleta("Alfredo Zaragoza Rofriguez", 5, 5)
print("-----------------------------------------------------")
generar_boleta("Pedro Parker", 10, 10)