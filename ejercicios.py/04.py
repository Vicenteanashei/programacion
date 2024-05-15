from os import system
system("cls")

""" Escriba un programa que permita convertir una medida dada en pies, a su equivalente enyardas, pulgadas, centímetros, metros
(1 pie=12 Pulgadas ;1 yarda=3 pies ; 1 pulgada =2,54 cmy 1 metro=100 cm).
 Muestre todas las equivalencias
"""
pies = int(input(
    f"escribe la medida que deseas convertir de pies a , yardas, pulgadas, centimetros y/o metros: "))
print(f"sus medidas son las siguientes, yardas: {
      pies*3} - pulgadas: {pies*12*2.54} - metros: {pies*100} ")
