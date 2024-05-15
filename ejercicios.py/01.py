from os import system
system("cls")

''' Diseñar un Algoritmo que lea un número entero y otro real para luego mostrar los resultadosde sumar, restar, dividir y multiplicar dichos números
'''
nreal = float(input("ingresa un numero real: "))
nentero = int(input("ingresa un numero entero: "))

print(f"resultados de suma: {nreal+nentero} resta: {nreal -
      nentero} division: {nreal/nentero} multiplicacion: {nreal*nentero}")
