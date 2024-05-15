from os import system
system("cls")
# Desarrollar un algoritmo que simule el proceso de reserva de pasajes de buses para una empresa
# de transporte en Chile. El programa debe comenzar solicitando al usuario su nombre y si es cliente
# frecuente de la empresa (True/False).
# Luego, debe preguntar al usuario su destino preferido entre las siguientes opciones:
#       1. Santiago 8.000
#       2. Valparaíso 10.000
#       3. Concepción 12.000
# Una vez seleccionado el destino, el programa debe preguntar al usuario la fecha de viaje y de
# retorno. Después, debe preguntar si el usuario desea agregar servicios adicionales a su reserva,
# como seguro de viaje o asientos premium. Si la respuesta es afirmativa, el programa debe mostrar
# las siguientes opciones:
#       1. Seguro de viaje - $5.500
#       2. Asiento premium - $2.500
# El usuario debe seleccionar los servicios extras deseados y la cantidad en caso de aplicar.
# Finalmente, el programa debe mostrar un resumen de la reserva con el nombre del pasajero,
# destino, fechas, servicios adicionales seleccionados y el costo total.


print("Bienvenido a maxucaobus")
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre != "":
        break
    else:
        print("debe ingresar un nombre valido")
costo_total = 0
santiago = 8000
valparaiso = 10000
concepcion = 12000
valor_seguro = 5500
valor_asiento = 2500
op = int(input("""¿Cual es su destino favorito?
1.Santiago: $8000
2.Valparaiso: $10000
3.Concepcion: $12000
"""))
while op > 0 and op <= 3:
    match op:
        case 1:
            print("Usted ingresó Santiago.")
            destino = "santiago"
            costo_total += santiago
            break
        case 2:
            print("Usted ingresó Valparaiso.")
            destino = "Valparaiso"
            costo_total += concepcion
            break
        case 3:
            print("Usted ingressó Concepción.")
            destino = "Concepción"
            costo_total += concepcion
            break
