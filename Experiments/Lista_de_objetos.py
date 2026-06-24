inventario = []
objetos_prohibidos = ["cuchillo","pistola","bomba","cigarro","alcohol"]
objetos = 0
while objetos < 5:
    objeto = input("¿Qué objeto haz encontrado? ")
    inventario.append(objeto)
    objetos +=1
print(f"Misión de recolección terminada. Tu inventario es: {inventario}")

contrabando = input("Alto ahi, ¿Qué objeto estas buscando oficial? ")
print(f"Estoy buscando estos objetos prohibidos {objetos_prohibidos}")
if contrabando in inventario:
     inventario.remove(contrabando)
     print("¡Contrabando detectado! Confiscando ahora")
else:
    print("Todo limpio. Puedes continuar tu viaje.")