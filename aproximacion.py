objetivo = int(input("Escoge un numero: "))
epsilon = 0.0001 #cuanto más 0 pongamos más tardará en dar la respuesta
paso = epsilon**2
respuesta = 0.0 

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontró la raiz cuadrada del {objetivo}")
else:
    print (f"La raiz cuadrada del {objetivo} es {respuesta}")