import random
Variables = ("piedra","papel","tijeras")
Respuesta_Jugador = input("Elige Piedra, Papel o Tijeras: ").lower().strip()
Respuesta_PC= random.choice(Variables)
if Respuesta_Jugador == Respuesta_PC:
    print("¡Empate, los 2 han elegido ",Respuesta_PC,"!")
elif Respuesta_Jugador == "piedra" and Respuesta_PC == "tijeras":
    print("¡Ganaste! La piedra aplasta las tijeras.")
elif Respuesta_Jugador == "papel" and Respuesta_PC == "piedra":
    print("¡Ganaste! El papel vence a la piedra.")
elif Respuesta_Jugador == "tijeras" and Respuesta_PC == "papel":
    print("¡Ganaste! Las tijeras cortan al papel.")
else:
    print("¡Perdiste! La computadora te ha vencido.")
    print(f"La computadora ha elegido: {Respuesta_PC}")

