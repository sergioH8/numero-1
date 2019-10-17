apetece_helado = input("Te apetece un helado? (Si/No): ")
tienes_dinero = input("Tienes dinero? (Si/No): ")
esta_el_señor_de_los_helados = input("Esta el señor de los helados? (Si/No): ")
esta_tu_tia = input("Estas con tu tia ? (Si/No): ")

if apetece_helado == "Si" and (tienes_dinero == "Si" or esta_tu_tia == "Si") and esta_el_señor_de_los_helados == "Si":
    print("Pues comete un helado")

else:
    print("Pues nada")
