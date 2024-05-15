from os import system
system("cls")

"""Diseñar un programa que pueda invertir un número de 2 dígitos. Por ejemplo, si el número es 56 en la pantalla debe mostrar 65.
"""
num1 = input("ingrese un numero de dos digitos")
print(f"el numero invertido es {num1[-1]}{num1[0]}")
