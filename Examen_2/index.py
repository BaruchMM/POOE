import random as rn
import string
import numpy as np
import component as co
import models as md



clientes = {}
empleados = {}
data = [
    ['Juan Perez','05','08','1982','electronica','10000'],
    ['Luis Lopez','08','11','1988','papeleria','5890'],
    ['María García','02','009','1990','Ropa','12000']
]
empleados = co.newEmployees(empleados,data)
ventas = {}
productos = {}
productos = co.newProducto(productos)
productos = co.newProducto(productos)
productos = co.newProducto(productos)
productos = co.newProducto(productos)
productos = co.newProducto(productos)

def menuAdmin():
    print('Utilice algún número para seleccionar una opción.')
    print('Para salir ingrese "EXIT".')
    print('\t 1) Mostrar Empleados')
    print('\t 2) Calcular Sueldos')
    print('\t 3) Producto nuevo')
    fin_admin = False
    while(fin_input == False):
        inp_admin = input('Seleccione la opción deseada: ')
        if inp_admin in ['1','2','3']:
            fin_admin = True
            if inp == '1':
                co.viewEmployees(empleados)
            elif inp == '2':
                NoEmpleado = input('Ingrese el numero de empleado: ')
                empleados = md.empleado.calcularSueldo(NoEmpleado, empleados)
            else:
                productos = co.newProducto(productos)
        elif inp.lower() == 'exit':
            fin_input = True
            fin = True
            print("Cerrando.")
        else:
            print("Opción no válida.")


clientes = co.AllClients()
fin = False
while (fin == False):
    print('')
    print('**********MENÚ*******')
    print('Utilice algún número para seleccionar una opción.')
    print('Para salir ingrese "EXIT".')
    print('\t 1) Mostrar Clientes')
    print('\t 2) Area Administrativa')
    print('\t 3) Registrar Venta')
    fin_input = False
    while(fin_input == False):
        inp = input('Seleccione la opción deseada: ')
        print("")
        if inp in ['1','2','3']:
            fin_input = True
            if inp == '1':
                co.viewClients(clientes)
            elif inp == '2':
                menuAdmin()
            else:
                co.newVentas(ventas,clientes,productos,empleados)
        elif inp.lower() == 'exit':
            fin_input = True
            fin = True
            print("Cerrando.")
        else:
            print("Opción no válida.")


