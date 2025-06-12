numeros_1=10
numeros_2=5

string_1="Hola"
string_2="Python"

lista_1=["valor1", "valor2", "valor3"]
lista_2=["valor4", "valor5", "valor6"]

dec_1={"clave1": "valor1",
        "clave2": "valor2",}
dec_2={"clave3": "valor3",
        "clave4": "valor4",}

# operadores de pertenencia

print("o" in string_1)
print("valor1" in lista_1)
# sobre dicionario se hace sobre los vaores clave
print("clave2" in dec_1)

# operador de negacion
print("valor6" not in lista_1)

# operadores logicos
# and not or
print(numeros_1 > numeros_2 or "valor1" in lista_1)
print(numeros_1 < numeros_2 and "valor1" in lista_1)
print(not numeros_1 < numeros_2 and "valor1" in lista_1)

# operadores de identidad
# is is not

print(string_1 is "hola")
print( type(string_1) is str)
print( string_1 is list)

