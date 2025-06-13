# Desarrolla un script que recomiende acciones de 
# seguridad informática a realizar basándose en el
#  nivel de amenaza actual, utilizando sentencias if/elif/else en 
# Python junto con los conceptos previamente aprendidos.

nivelesAmenaza=("Bajo","Moderado","Alto","Critico")
recomendaciones={
    "Bajo":"Atividad recomendada: Realizar auditorias de Seguridad",
    "Moderado":" Actividad recomendada: Reforzar la conciencia de los empleados sobre riesgo de syberseguridad",
    "Alto":"Actividad  recomendada: implementar medidad de seguridad adicionales y revisar los accesos",
    "Critico":"Actividad  recomendada: activar el protocolo de respuesat a incidentes"
}
amanazaActual="Alto"

print("\n ========================TENEMOS ALERTAS DE AMENAZA========================================")

if amanazaActual in nivelesAmenaza and amanazaActual in recomendaciones:
    print(f"La amenaza es: {amanazaActual}", recomendaciones[amanazaActual])
else:
    print(" no has definido el nivel de amenaza, seleciona uno de los siguientes niveles de amenaza: ", nivelesAmenaza)

print("===================================================================\n")
