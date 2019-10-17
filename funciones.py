
def input_con_confirmacion(pregunta):
    confimacion = False
    dato_usuario = ""
    while not confimacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, ¿Estas seguro? [Si/No] ".format(dato_usuario))
        if seguro =="Si":
            confimacion = True
    return dato_usuario


nombre = input_con_confirmacion("¿Como te llamas? ")
print("Has confirmado que te llamas {}".format(nombre))

numero = input_con_confirmacion("¿Dime un numero?")
print("Has dicho que el numero es {}".format(numero))

