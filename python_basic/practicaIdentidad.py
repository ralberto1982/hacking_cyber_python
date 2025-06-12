# Implementa un programa en Python que verifique 
# si una contraseña es segura bajo los criterios que se muestran 
# a continuación. Para ello, utiliza operadores de pertenencia
#  y lógicos.

# Debe tener al menos 8 caracteres.

# No debe contener el carácter @ ni #.

# Debe contener al menos un número.

# No debe contener espacios.

lista=["Longitud es mayor a 8 caracters:","No contiene sinbolos @#","Tiene numeros:","No tiene espacios"]

password="edwinloaiza10"
longitud=(len(password)>8)
caracter=(not "@" in password and not "#" in password)
numero=("10" in password)
espacios=(not " " in password)

print("\n ========================================================")
print("VERIFICADOR DE CONTRASEÑAS TENER EN CUENTA LOS PARAMETROS")
print(f"SU CONTRASEÑA ES:{password}")
print("-"+lista[0],longitud)
print("-"+lista[1],caracter)
print("-"+lista[2],numero)
print("-"+lista[3],espacios)
contaseñaok=(caracter == True and longitud == True and numero == True and espacios == True  )
print(f"¿ LA CONTRASEÑA CUMPLE CON LOS REQUISITOS ESTABLECIDOS:? {contaseñaok}")
print("\n =============================================================================")

