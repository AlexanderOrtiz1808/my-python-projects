print("¡Bienvenido a la Mini Trivia!")
print("Cultura general")
print("-" * 30)

# 1. Guardamos todas las preguntas y respuestas en una "Lista"
trivia = [
    ("Pregunta 1: ¿Cuál es el lugar más frío de la tierra?", "antártida"),
    ("Pregunta 2: ¿Cuál es el río más largo del mundo?", "amazonas"),
    ("Pregunta 3: ¿Dónde originaron los juegos olímpicos?", "grecia"),
    ("Pregunta 4: ¿Qué cantidad de huesos tiene el cuerpo humano?", "206"),
    ("Pregunta 5: ¿Cuál es el país más grande del mundo?", "rusia")
]

puntos = 0

# 2. Usamos un bucle 'for' para recorrer la lista una por una
for pregunta, respuesta_correcta in trivia:
    intentos = 3
    
    while intentos > 0:
        # .lower() convierte todo a minúsculas y .strip() borra espacios extra
        respuesta = input(f"{pregunta} ").lower().strip()
        
        # Opcional: Aceptar "antartida" sin acento para evitar frustraciones
        if respuesta == respuesta_correcta or respuesta == "antartida":
            print("¡Correcto! Te has ganado 10 puntos.\n")
            puntos += 10
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Respuesta incorrecta. Te quedan {intentos} intentos.")
            else:
                print("Tienes cero puntos en esta pregunta, ¡Buena suerte en la próxima!\n")

print("-" * 30)
print(f"Felicidades, has logrado {puntos}/50 puntos en total.")
print("Gracias por tu participación.")