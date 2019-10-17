
mi_lista = []
inpunt_usuario = input("¿Que necesitas comprar? (escribe fin parasalir): ")

while inpunt_usuario != "fin":
    mi_lista.append(inpunt_usuario)
    inpunt_usuario = input("¿Que necesitas comprar? (escribe fin para salir)")

largo_lista = len(mi_lista)
indice_actual = 0

for item in mi_lista:
    print("Tengo que comprar {}".format(item))


print("esta es la lista de la comra")
