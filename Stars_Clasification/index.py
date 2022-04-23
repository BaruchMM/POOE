import star
import components as co

stars = {}
stars = co.Stars()
co.buildDataFrame(stars)
## Menu ##
fin = False
while fin != False:
    print('MENÚ PRINCIPAL')
    print('Utilice algún número para seleccionar una opción.')
    print('Para salir del menú ingrese "EXIT".')
    print('\t 1. Mostrar habitaciones')
    print('\t 2. Reservar habitación')
    print('\t 3. Dejar habitación')
    print('\t 4. Solicitar servicio adicional')
    i = 1
    while(i != 0):
        inp = input('Seleccione la opción deseada: ')
        if inp in ['1','2','3','4']:
            i = 0
            if inp == '1':
                print('OPCION 1 SELECCIONADA')
                co.seeStars(stars)
                
            elif inp == '2':
                print('OPCION 2 SELECCIONADA')
                
            elif inp == '3':
                print('OPCION 3 SELECCIONADA')
                
            else:
                print('OPCION 4 SELECCIONADA')
                
        elif inp.lower() == 'exit':
            i = 0
            fin = True
            print("Cerrando.")
        else:
            print("Opción no válida.")

