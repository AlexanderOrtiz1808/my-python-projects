combustible = 100
salto_espacial = 5
while salto_espacial > 0:
    gasto = int(input("¿Cuánta gasolina se gasto en el viaje? "))
    salto_espacial -= 1
    combustible -= gasto
    if combustible <= 0:
        print("Te haz quedado sin combustible, nave barada")
        break
if salto_espacial == 0:
    print("Se acabaron los viajes espaciales de hoy")
    if combustible > 0:
        print("✅ Misión exitosa. Llegaste al destino con", combustible, "de combustible de sobra.")
    