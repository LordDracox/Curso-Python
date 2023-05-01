objectivo = int(input("Escode un entero: "))
respuesta = 0 
while respuesta**2 < objectivo:
    print(respuesta)
    respuesta += 1
if respuesta**2 == objectivo:
    print(f"la raiz cuadrada de {objectivo} es repuesta {respuesta}")
else:
    print(f"{objectivo} no tiene raiz cuadrada")
