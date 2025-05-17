#IMPORTAR LAS CLASES
from clientes import cliente
from equipos import equipo

#CREAR LOS OBJETOS CLIENTE Y EQUIPO
cliente1 = cliente()
equipo1 = equipo()
Opcion = ""

while (Opcion!=5):
    print("1. Agregar Cliente")
    print("2.Crear Equipo")
    print("3. Asignar Equipos a Cliente")
    print("4. Ver Listado de Equipos")
    print("5. Salir")
    print("-*50")
    print("Ingrese la opción que desea: ")
    Opcion = int(input())

    if Opcion == 1:
        # PEDIR LOS DATOS DEL CLIENTE
        apellidos = input("Ingrese apellidos del cliente:")
        nombre = input("Ingrese nombre del Cliente:")
        telefono = input("Ingrese telefono del Cliente")

        # AGREGAR DATOS DEL CLIENTE
        cliente1.AgregarCliente(apellidos,nombre,telefono)
    elif Opcion == 2:
        # INGRESAR DATOS DEL EQUIPO
        codigo = input("Ingrese el código del equipo:")
        nomEquipo = input("Ingrese nombre del equipo: ")
        precio = float(input("Ingrese precio del equipo:"))

        # CREAR EL EQUIPO CON SUS CARACTERISTICAS
        equipo1.AgregarEquipo(codigo,nomEquipo,precio)

    elif Opcion == 3:
        cliente1.AgregrarEquipo(equipo1)

    elif Opcion == 4:
        cliente1.VerEquipos()