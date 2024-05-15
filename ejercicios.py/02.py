from os import system
system("cls")

"""Queremos conocer los datos estadísticos de una asignatura, por lo tanto, necesitamos unprograma en Python que lea el número de reprobados y aprobados de una asignatura,
 y nosdevuelva:
 a. El porcentaje de alumnos que han aprobado la asignatura.
 b. El porcentaje de alumnos que han reprobado la asignatura.
"""
naprobados = int(input("ingresa el numero total de aprobados: "))
nreprp = int(input("ingresa el numero total de reprobados: "))
total = naprobados + nreprp
print(f"el porcentaje de aprobados es: {
      naprobados*100/total} y el porcentaje de reprobados es: {nreprp*100/total}")
