# Crear un script que gestione el inventario de licencias de herramientas de
# ciberseguridad, utilizando bucles for para iterar a través de las herramientas
#  almacenadas y simular una adquisición de herramientas del inventario.

inventario=[
("Nmap",50,0.5),
("Wireshark",30,0.3),
("Metasploit",20,0.4),
("Burp Suite",15,0.45)
]




valorTotal=0

mayorCantidad={
    "herramienta":"",
    "cantidad":0,
    "precio":0
}
print("\n===========================================================\n")
for herramienta, cantidad, precio in inventario:
    valorTotal += cantidad * precio
    if cantidad > mayorCantidad["cantidad"]:
       mayorCantidad["herramienta"]=herramienta
       mayorCantidad["cantidad"]=cantidad
       mayorCantidad["precio"]
       mayorCantidad["precio"]=precio
print(f" Valor total del inventario: ${valorTotal}")
print(f" Herramienta con mayor cantidad de licencias: {mayorCantidad['herramienta']} {mayorCantidad["cantidad"]} unidades")
       
compra={"Nmap":5,
        "Wreshark":3
        }


print("\nSIMULANDO COMPRA")
print(compra)
for herramienta, cantidad, precio in inventario:
    if herramienta in compra:
        valorTotal +=(precio * compra[herramienta])


print(f"el precio de la adquisision: {valorTotal} eur")


print("\n===========================================================\n")



 

