# for<variable> in <iterable>:
#     <sentencias>

lista=["tarea1","tarea2","tarea3"]
recomendaciones={
    "Bajo":"Atividad recomendada: Realizar auditorias de Seguridad",
    "Moderado":" Actividad recomendada: Reforzar la conciencia de los empleados sobre riesgo de syberseguridad",
    "Alto":"Actividad  recomendada: implementar medidad de seguridad adicionales y revisar los accesos",
    "Critico":"Actividad  recomendada: activar el protocolo de respuesat a incidentes"
}

for tarea in lista:
    print("estoy trabajando en la tarea:",tarea)
for reconmendacion in recomendaciones:
    print("Estado",reconmendacion)
    print( recomendaciones[reconmendacion])


# saber si algo es iterable
#   iter()
    # recomendaciones_iter = iter(recomendaciones)

    # print(next(recomendaciones_iter))


    # print(next(recomendaciones_iter))