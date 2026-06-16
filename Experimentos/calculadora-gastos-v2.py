print("Bienvenido a tu calculadora de gastos. \n")
Presupuesto_inicial = int(input("¿Cúal es tu presupuesto del dia de hoy? "))
while Presupuesto_inicial > 0:
    Compras = input("¿Qué comprarás? ")
    Gastos = int(input("¿Cuánto gastarás en eso? "))
    if Gastos > Presupuesto_inicial:
        print("¡Fondos insuficientes! No puedes comprar eso.\n")
    else:
        Presupuesto_inicial -= Gastos
        print(f"Gasto registrado. Te quedarán {Presupuesto_inicial} pesos.\n")
    Respuesta = input("¿Quieres registrar otro gasto? ")
    if Respuesta.lower().strip() == "si" or Respuesta.lower().strip() == "sí":
        print("Okay, continuamos.\n ")
    elif Respuesta.lower().strip() == "no":
        print("Muy bien, tu saldo actual es de", Presupuesto_inicial, "pesos.\n")
        break
if Presupuesto_inicial == 0:
    print("Te haz quedados sin fondos, bro\n")
