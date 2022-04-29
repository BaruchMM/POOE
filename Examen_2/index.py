import random as rn
import string
import numpy as np
import component as co



clientes = {}
empleados = {}
ventas = {}
datos = {}

clientes = co.AllClients()
co.viewClients(clientes)

co.newClient(clientes)
co.viewClients(clientes)
co.finDiaClientes(clientes)
fin = True
while (fin == False):
    print('')
    print('MENÚ INGRESO DE DATOS')
    print('Utilice algún número para seleccionar una opción.')
    print('Para salir ingrese "EXIT".')
    print('\t 1. Agregar datos en archivo')
    print('\t 2. Agregar datos manualmente')
    print('\t 3. Mostrar datos actuales')
    print('\t 4. Procesar datos actuales')
    fin_input = False
    while(fin_input == False):
        inp = input('Seleccione la opción deseada: ')
        print("")
        if inp in ['1','2','3','4']:
            fin_input = True
            if inp == '1':
                datos = ag_datos_archivo(datos)
            elif inp == '2':
                datos = ag_datos_manual(datos)
            elif inp == '3':
                if(datos == []):
                    print("Actualmente no hay datos agregados.")
                else:
                    co.seeStars(datos)
            else:
                menu_proc(datos)
        elif inp.lower() == 'exit':
            fin_input = True
            fin = True
            print("Cerrando.")
        else:
            print("Opción no válida.")


