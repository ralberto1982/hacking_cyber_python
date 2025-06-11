# CREA UNA LISTA DE PLATOS
platos=["Paella","Risotto","Sushi","Tacos","Pizza"]
# print(platos)

# CREAR UNA TUPLA CON LOS PLATOS Y SUS PRECIOS
platosPrecios=("Paella: 15 Euros","Risotto: 12 Euros","Sushi: 20 Euros","Tacos; 10 Euros","Pizza: 8 Euros")
# print(platosPrecios)
# print(platosPrecios[1:4])


# MENU UTILIZANDO DICCIONARIOS
menu={
    "Paella":"$15",
    "Risotto":"$12",
    "sushi":"$20",
    "tacos":"$10",
    "pizza":"$8"
}
print("====================================================\n")
print("BIENVENIDOS A NUESTRO RESTAURANTE \"EL GUSTICO DE JUAN\"\n")
print("ESTE ES NUESTRO MENU ESPECIAL")
print("-" + platosPrecios[0])
print("-" + platosPrecios[1])
print("-" + platosPrecios[2])
print("-" + platosPrecios[3])
print("-" + platosPrecios[4])

print("\n El tercer plato de nuestro menu es Suschi y su precio es " + menu["sushi"] + "\n" )

print(" Los platos pares son: ", platos[0::2], "\n")