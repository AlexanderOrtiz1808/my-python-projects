print("Bienvenido a tu calculadora de gastos. \n")
Presupuesto_inicial = int(input("¿Cúal es tu presupuesto del dia de hoy? "))
while Presupuesto_inicial > 0:
    Compras = input("¿Qué compraste? ")
    Gastos = int(input("¿Cuánto gastaste en eso? "))
    Presupuesto_inicial -= Gastos
    Respuesta = input("¿Quieres registrar otro gasto? ")
    if Respuesta.lower().strip() == "si" or Respuesta.lower().strip() == "sí":
        print("Okay, continuamos.")
    elif Respuesta.lower().strip() == "no":
        print("Muy bien, tu saldo actual es de", Presupuesto_inicial, "pesos")
        break
if Presupuesto_inicial == 0:
    print("Te haz quedados sin fondos, bro")
