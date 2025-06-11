# LISTAS EN PYTHON

# coleccion de valores
# siempre respetan el orden
# se pueden agregar elementos 

lista=["tarea1", "tarea2","tarea3"]
lista_numeros=[1,2,3]
lista_combinada=["tarea",2]

print(lista)
print(lista_numeros)

# LAS TUPLAS
# las tuplas son inmutables
# cuando usar
# cunado necesitamos rapidez
# valores consttantes sin cambio
# combianar otros datos como diccionarios
tupla=("tarea",1, "perro")

# LOS DICCIONARIOS
# llevan clave y valor algo similar aun objeto
diccionario={
    "tarea":"pendiente",
    "tarea2":"en proceso",
    "tarea3":"terminada",
    "tarea4":"terminada"
}


print(diccionario["tarea"])

# indexando o accedinedo ESTOS TIPOS DE DATOS HAY 3 FORMAS
# INDEXING
print(lista[-1])
print(lista[0][1])

print(tupla[0])

print(diccionario["tarea"])

# SLICING 
print(lista[1:3])
print(tupla[1:3])

# STRIDE  SON DOS PUNTOS ADICIONALES 
print(tupla[0::2])
print(lista[0::2])

# MODIFICANDO LAS LISTAS
lista[0]="tarea especial"

print(lista)

diccionario["tarea"]="terminada de una"

print(diccionario)

cadena="texto"
cadena["0"]="p"
print(cadena)


