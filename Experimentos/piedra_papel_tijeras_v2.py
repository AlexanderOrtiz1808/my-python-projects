import random

Variables = ("piedra","papel","tijeras")

puntos_jugador = 0
puntos_pc = 0

print("Bienvenido al juego de piedra, papel y tijeras \n")
print("Recuerda si quieres terminar el juego solo escribe: Salir \n ")
while True:
    Respuesta_Jugador = input("Elige Piedra, Papel o Tijeras: ").lower().strip()
    Respuesta_PC= random.choice(Variables)
    if Respuesta_Jugador == Respuesta_PC:
        print("¡Empate, los 2 han elegido ",Respuesta_PC, "+ 1 pnt!")
        puntos_jugador += 1
        puntos_pc += 1
    elif Respuesta_Jugador == "piedra" and Respuesta_PC == "tijeras":
        puntos_jugador += 1
        print("¡Ganaste! La piedra aplasta las tijeras. + 1 pnt")
    elif Respuesta_Jugador == "papel" and Respuesta_PC == "piedra":
        puntos_jugador += 1
        print("¡Ganaste! El papel vence a la piedra. + 1 pnt")
    elif Respuesta_Jugador == "tijeras" and Respuesta_PC == "papel":
        puntos_jugador += 1
        print("¡Ganaste! Las tijeras cortan al papel. + 1 pnt")
    else:
        print("¡Perdiste! La computadora te ha vencido.")
        puntos_pc += 1
        print(f"La computadora ha elegido: {Respuesta_PC}")
    if Respuesta_Jugador == "salir":
        print("¡Gracias por jugar!")
        print(f"Marcador Final -> Tú: {puntos_jugador} | PC: {puntos_pc}")
        break
