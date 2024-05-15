from os import system
system("cls")
op = input("""
        Este programa calcula area de diferentes formas
        1.- Para calcular el area de un cuadrado
        2.- Para calcular el area de un rectangulo
        3.- Para calcular el area de un triangulo
        4.- Para calcular el area de un circulo
        5.- Para salir
        """)
if op == "1":
    lado = int(input("Ingrese el lado del cuadrado: "))
    print(f"El area de su cuadrado es: {lado*lado}")
elif op == "2":
    largo = int(input("Ingrese el largo de su rectangulo: "))
    ancho = int(input("Ingrese el ancho de su rectangulo: "))
    print(f"El area de su rectangulo es: {largo * ancho}")
elif op == "3":
    base = int(input("Ingrese la base de su triangulo: "))
    altura = int(input("Ingrese la altura de su triangulo: "))
    print(f"El area de su triangulo es: {base * altura / 2}")
elif op == "4":
    radio = float(input("Ingrese el radio del circulo: "))
    radio = radio / 2
    print(f"El area de su circulo es: {3.14 * radio}")
else:
    ("Salio del programa")
