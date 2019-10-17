salida = False
agenda = []

while not salida:
    accion = input("¿Que quieres hacer ? [Añadir un numero [A] / Consultar un numero [C] / Salir [S]: ")

    # Accion añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono: ")
        print("---------------: ")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda.append([nombre, numero])

    #Accion consultar
    elif accion == "C":
        print("Consultar numero:")
        print("------------:")
        nombre = input("De quien quieres saber el numero:")
        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])
    # Accion salir
    elif accion == "S":
        salida = True
