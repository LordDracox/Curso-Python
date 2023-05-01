## en este curso usamos el while#

#contador = 0 

#while contador < 10 :
    #print(contador)
    #contador = contador + 1 #puedes usar +=1

#contador_externo = 0
#contador_interno = 0

#while contador_externo < 5:
    #while contador_interno < 6 :
        #print (contador_externo, contador_interno)
        #contador_interno = contador_interno + 1
        #if contador_interno == 3:
            #break
    #contador_externo = contador_externo + 1
    #conntador_interno = 0#

horas = 0 
minutos = 0
seg = 0

while horas < 24:
    while minutos < 60:
        while seg < 60:
            print (horas, minutos , seg)
            seg = seg + 1 
        minutos = minutos + 1
        seg = 0
    horas = horas + 1 
    minutos = 0
    