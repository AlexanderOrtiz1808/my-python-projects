import random
Salarios= []
for i in range(100):
    Salario_generado = random.randint(10000, 50000)
    Salarios.append(Salario_generado)
print("Bienvenido al mini analizador de datos \n")


while True:
    print("¿Qué te gustaría hacer ahora?")
    print("1. Ver el salario máximo")
    print("2. Ver el salario mínimo")
    print("3. Calcular el promedio")
    print("4. Salir \n")
    opcion_elegida = input("¿Qué te gustaría hacer? ").strip().lower()
    if opcion_elegida == "1":
        print(f"El salario máximo es: {max(Salarios)}")
    elif opcion_elegida == "2":
        print(f"El salario mínimo es: {min(Salarios)}")
    elif opcion_elegida == "3":
        print(f"El promedio de salarios es: {sum(Salarios)/len(Salarios)}")
    else:
        print("Haz salido del mini analizador de datos")
        break