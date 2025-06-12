# Desarrollar un script que calcule la puntuación final de um
# participante en una competición de ciberseguridad, utilizando operadores aritméticos,
# de comparación y de asignación.

# PUNTUCACIONES ALUMNO
p_pentesting=5
p_analisis_vulnerabilidades=3
p_desarrollo_exploits=6

# PORCENTAGES
pentestting=0.5
vulnerabilidad=0.2
exploit=0.3

# RESULTADOS
puntuacionFinal=(p_pentesting * pentestting) +(  p_analisis_vulnerabilidades * vulnerabilidad) + (p_desarrollo_exploits * exploit)

participanteAprobado= puntuacionFinal >= 5.0
distincionHonor=puntuacionFinal==10
print("\n"+ "===========================================================")

print("RESULTADO DE LA PRUEBA DE CYBERSEGURIDAD CON PYTHON")

print(f"LA PUNTUACION FINAL FUE: {puntuacionFinal} ")
print(f"¿ EL PARTICIPANTE FUE APROBADO.?  {participanteAprobado}")
print(f"¿ EL PARTICIPANTE TIENE DISTINCION DE HONOR.?{distincionHonor} ")


print("================================================================")