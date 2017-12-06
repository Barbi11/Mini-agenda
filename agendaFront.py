#!/usr/bin/env python3

import os

def menu():
    print("Mini agenda")
    print("==== ======")
    print("1- Ingresar contacto")
    print("2- Eliminar contacto")
    print("3- Buscar contacto")
    print("4- Mostrar contactos")
    print("5- Salir")
    
directorio = []
nombres = {}
apellidos = {}
telefonos = {}
opcionMenu = 0
menu()

while opcionMenu != 5:
	opcionMenu = int(input("Elija una opcion: "))
	if opcionMenu == 1:
		print("Ingrese Nombre, Apellido y Número de teléfono")
		name = input("Nombre: ")
		surname = input("Apellido: ")
		phone = input("Teléfono: ")
		telefonos["telefono"] = phone
		nombres["nombre"] = name
		apellidos["apellido"] = surname
		directorio.append([nombres]) 
		directorio.append([apellidos]) 
		directorio.append([telefonos])
		menu()

	elif opcionMenu == 2:
		surname = Input("Apellido: ")
		if surname in directorio:
			choice = input("¿Desea eliminar este contacto? (y/n)")
			if choice == "y":
				print("Contacto borrado")
			else:
				menu()
			menu()
	
	elif opcionMenu == 3:
		print("Buscar contacto")
		surname = input("Apellido: ")
		if surname in telefonos:
			print(apellidos["telefonos"])
			
	elif opcionMenu == 4:
		print(directorio)
		menu()
