# El objetivo de este ejercicio es implementar el cifrado César
# utilizando el lenguaje de programación Python.
# El cifrado César es un tipo de cifrado por sustitución en el que
# cada letra en el texto plano es 'desplazada' un cierto número de
# lugares hacia la derecha o hacia la izquierda en el alfabeto. Por 
# ejemplo, con un desplazamiento de 3, la 'A' se convierte en 'D', la 'B'
# se convierte en 'E', y así sucesivamente. Este método de cifrado lleva el
# nombre de Julio César, quien, según se informa, lo usó para comunicarse con sus generales.

alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def cifradoCesar(texto, desplazamiento):
    """ Cifra un texto utilizando el metodo de cifrado cesar.


    arg:
       texto(str):El texto a cifrar
       desplazamiento (int): El numero deposisiones que cada letra 
       del texto sera desplazada a lo largo del alfabeto

    return:
        str: El texto cifrado si todos loa caracteres son validos(mayus y dentrod el alfabeto)
        str: unmensaje de error si algun caracter no es valido
    Ejemplo:
        >>> cifradoCesar("HOLA MUNDO", 3)
        'KROD PXQGR'

    """
    textoCifrado=""
    for letra in texto:
        if letra in alfabeto:
            indiceNuevo=(alfabeto.index(letra) + desplazamiento) % len(alfabeto)
            textoCifrado += alfabeto[indiceNuevo]
        elif letra in " ,.":
            textoCifrado += letra
        else:
            return "todos los caracteres deben estar en mayusculas y dentro del alfabeto" 
    return textoCifrado


def descifradoCesar(textoCifrado, desplazamiento):
    """
       Descifra un texto que ha sido cifrado con el método del cifrado César.
    Args:
        texto_cifrado (str): El texto cifrado a descifrar.
        desplazamiento (int): El número de posiciones que cada letra del texto cifrado
            será desplazada hacia atrás a lo largo del alfabeto. 
     Returns:
        str: El texto descifrado si todos los caracteres son válidos.
        str: Un mensaje de error si algún caracter no es válido.
 
    Ejemplo:
        >>> descifrado_cesar("KROD PXQGR.", 3)
        'HOLA MUNDO.        
    
    """

    textoDescifrado = ""
    for letra in textoCifrado:
        if letra in alfabeto:
           indiceOriginal=(alfabeto.index(letra) - desplazamiento) % len(alfabeto)
           textoDescifrado += alfabeto[indiceOriginal]
        elif letra in " ,.:":
           textoDescifrado += letra
        else:
            return "todos los caracteres deben estar en mayusculas y dentro del alfabeto "
    return textoDescifrado

help(cifradoCesar)
    
print("\n======================================================\n")

textPrueba= "HOLA MUNDO"
desplazamientoPrueba=3
textoCifrado=cifradoCesar(textPrueba, desplazamientoPrueba)
print("proceso de cifrado")
print("- texto a cifrar", textPrueba)
print("- texto cifrado", textoCifrado)


textoDescifrado=descifradoCesar(textoCifrado, desplazamientoPrueba)
print("proceso de descifrado:")
print("- texto  cifrado", textoCifrado)
print("- texto descifrado",textoDescifrado )

textoMinuscula="hola mundo"
resultadoMinuscula=cifradoCesar(textoMinuscula, desplazamientoPrueba)
print("prueba con texto en minusculas:")
print("-", resultadoMinuscula)

print("\n======================================================\n")
    