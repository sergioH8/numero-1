"""
Obtener la tabla de multiplicar de un numero
"""

numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range (1, 11):
    print("{} x {} = {}5".format(numero_tabla, multiplo, numero_tabla * multiplo))
