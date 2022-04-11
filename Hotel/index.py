# %%
import hotel as ho

habitaciones = {}
habitaciones = ho.inicializarHabitacionesSpec()
# %%
## Menu ##
fin = False
while fin != True:
    print('Bienvenido, utilice uno de los números para seleccionar la opción deseada:')
    print('\t 1-Mostrar habitaciones')
    print('\t 2-Reservar habitación')
    print('\t 3-Dejar habitación')
    print('\t 4-Solicitar servicio adicional')
    print('\n\n Para marcar el fin del día, escriba "EXIT"')
    i = 1
    while(i != 0):
        inp = str(input('Seleccione la opción deseada: '))
        if inp in ['1','2','3','4']:
            i = 0
            if inp == '1': ho.mostrarHabitaciones(habitaciones)
            elif inp == '2': ho.reservar_habitacion(habitaciones)
            elif inp == '3': 
                numero = int(input('Ingrese el número de habitación'))
                ho.liberarHabitacion(habitaciones, numero)
        elif inp.lower() == 'exit':
            i = 0
            fin = True

# %%
