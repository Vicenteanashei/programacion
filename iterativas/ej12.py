from os import system
system("cls")
while True:
    print("""Ingresa la opción que desees.
            1. área cuadrado
            2. área de rectángulo
            3. área de trriángulo
            4. área de círculo
            5. Para salir """)
    op = input("Ingrese una opcion: ")

    match op:
        case "1":
            cuadrado = int(
                input("Ingrese la longitud del lado del cuadrado: "))
            print(f"El área solicitada es de {cuadrado * cuadrado}")
            break
        case "2":
            rec = int(input("Ingrese la base del rectangulo: "))
            reca = int(input("Ingrese la altura del rectangulo: "))
            print(f"El área solicitada es de {rec*reca} ")
            break
        case "3":
            tri = int(input("Ingrese la base del triángulo: "))
            tria = int(input("Ingrese la altura del triángulo: "))
            print(f"El área solicitada es de {(tri*tria)/2}")
            break
        case "4":
            rcir = float(input("Ingrese el radio del circulo: "))
            print(f"El área solicitada es de {(rcir*rcir)*3.14}")
            break
        case "5":
            print("Saliendo del programa")
            break
        case other:
            print("ta malo webon")
            system("cls")
