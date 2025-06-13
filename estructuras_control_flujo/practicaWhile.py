# Desarrollar un script que simule la gestión de recursos
# financieros en un equipo de respuesta a incidentes de ciberseguridad, utilizando bucles While en
# Python junto con los conceptos previamente aprendidos.

fondos= 10000

acciones=[20000,-5500,-900,-950]

indice=0
print("\n==============================================================\n")

print(f"Fondos iniciales: {fondos}")
while indice < len(acciones):
    accionActual=acciones[indice]
    if accionActual< 0 and abs(accionActual)> fondos:
        print(f"Accion omitida por fondos insuficientes: {accionActual}")
    else: fondos +=accionActual
    print(f"Accion procesada: {accionActual}. fondos actuales: {fondos} ")
    indice +=1



print(f"\nFondos finales despues de las acciones: {fondos}\n")


print("\n==============================================================\n")