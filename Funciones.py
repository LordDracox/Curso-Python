def enumeracion(objectivo):
    respuesta = 0 
    while respuesta**2 < objectivo:
        print(respuesta)
        respuesta += 1
    if respuesta**2 == objectivo:
        print (f"la raiz cuadrada de {objectivo} es repuesta {respuesta}")
    else:
        print (f"{objectivo} no tiene raiz cuadrada")
def aproximacion(objectivo):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0 

    while abs(respuesta**2 - objectivo) >= epsilon and respuesta <= objectivo:
        respuesta += paso
    if abs(respuesta**2 - objectivo) >= epsilon:
        print(f"No se encontró la raiz cuadrada del {objectivo}")
    else:
        print (f"La raiz cuadrada del {objectivo} es {respuesta}")

def busqueda(objectivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0,objectivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objectivo) >=epsilon:
        print(f"bajo = {bajo}, alto = {alto},respuesta = {respuesta}")
        if respuesta**2 <objectivo:
            bajo = respuesta
        else:
            alto = respuesta
    
        respuesta = (alto + bajo)/2
    print(f"La raiz cuadrada de {objectivo} es {respuesta}")

a =  str(input("Seleciona Busqueda binaria, enumeracion o aproximacion : "))
objectivo = 0 
if a == "enumeracion":
    objectivo = int(input("Introduce un número: "))
    enumeracion(objectivo)
if a == "aproximacion":
    objectivo = int(input("Escoge un número: "))
    aproximacion(objectivo)
if a == "busqueda":
    objectivo = int(input("Escoge un número: "))
    busqueda(objectivo)

