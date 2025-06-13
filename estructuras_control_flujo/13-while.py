recomendaciones={
    "Bajo":"Atividad recomendada: Realizar auditorias de Seguridad",
    "Moderado":" Actividad recomendada: Reforzar la conciencia de los empleados sobre riesgo de syberseguridad",
    "Alto":"Actividad  recomendada: implementar medidad de seguridad adicionales y revisar los accesos",
    "Critico":"Actividad  recomendada: activar el protocolo de respuesat a incidentes"
}

# while <expresion>:
#     <sentencias> 

num = 4

while num > 0:
    num -= 1
    print(num)

# romper 
while num > 0:
    # num -= 1
    print(num)
    break
print("esta linea nunca se va ejecutar")

# romper 
while num > 0:
    # num -= 1
    print(num)
    continue
    print("esta linea nunca se va ejecutar")


print("esto esta fuera del bucle")

# iteraun rango

for i in range(20):
    print(i)