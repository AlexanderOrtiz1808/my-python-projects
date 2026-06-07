print("¡Bienvenido a la Mini Trivia!")
print("Cultura general")

IntentosP1 = 3
IntentosP2 = 3
IntentosP3= 3
IntentosP4 = 3
IntentosP5 = 3

Puntos=0
Llave=0
#Pregunta 1
while IntentosP1>0:
    respuesta = input("Pregunta 1: ¿Cuál es el lugar más frío de la tierra?")
    if respuesta == "Antártida":
        print("¡Correcto! Te has ganado 10 puntos.")
        Puntos += 10
        Llave += 1
        break
    else:
        IntentosP1 -= 1
        print(f"Respuesta incorrecta. Te quedan {IntentosP1} intentos.")
if IntentosP1==0:
    print("Tienes cero puntos en esta pregunta, ¡Buena surte en las siguientes preguntas!")
    Llave += 1
#Pregunta 2
if Llave == 1:
    while IntentosP2 > 0:
            respuesta2 = input("Pregunta 2: ¿Cuál es el río más largo del mundo?")
            if respuesta2 == "Amazonas":
                print("¡Correcto! Te has ganado 10 puntos.")
                Puntos += 10
                Llave += 1
                break
            else:
                IntentosP2 -= 1
                print(f"Respuesta incorrecta. Te quedan {IntentosP2} intentos.")
    if IntentosP2==0:
        print("Tienes cero puntos en esta pregunta, ¡Buena surte en las siguientes preguntas!")
        Llave += 1

#Pregunta 3
if Llave == 2:
    while IntentosP3 > 0:
        respuesta3 = input("Pregunta 3: ¿Dónde originaron los juegos olímpicos?")
        if respuesta3 == "Grecia":
            print("¡Correcto! Te has ganado 10 puntos.")
            Puntos += 10
            Llave += 1
            break
        else:
            IntentosP3 -= 1
            print(f"Respuesta incorrecta. Te quedan {IntentosP3} intentos.")
    if IntentosP3==0:
        print("Tienes cero puntos en esta pregunta, ¡Buena surte en las siguientes preguntas!")
        Llave += 1
        
#Pregunta 4
if Llave == 3:
    while IntentosP4 > 0:
        respuesta4 = input("Pregunta 4: ¿Qué cantidad de huesos en el cuerpo humano?")
        if respuesta4 == "206":
            print("¡Correcto! Te has ganado 10 puntos.")
            Puntos += 10
            Llave += 1
            break
        else:
            IntentosP4 -= 1
            print(f"Respuesta incorrecta. Te quedan {IntentosP4} intentos.")
    if IntentosP4==0:
        print("Tienes cero puntos en esta pregunta, ¡Buena surte en las siguiente pregunta!")
        Llave += 1        

#Pregunta 5
if Llave == 4:
    while IntentosP5 > 0:
        respuesta5 = input("Pregunta 5: ¿Cuál es el país más grande del mundo?")
        if respuesta5 == "Rusia":
            print("¡Correcto! Te has ganado 10 puntos.")
            Puntos += 10
            print(f"Felicidades haz logrado {Puntos}/50 puntos en total")
            print("Gracias por tu participación")
            break
        else:
            IntentosP5 -= 1
            print(f"Respuesta incorrecta. Te quedan {IntentosP5} intentos.")
    if IntentosP5==0:
        print("Tienes cero puntos en esta pregunta, ¡Buena surte en la proxima!")  
        print(f"Felicidades haz logrado {Puntos}/50 puntos en total")             
        print("Gracias por tu participación")        