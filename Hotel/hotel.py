# %%
from asyncio.windows_events import NULL
import fileinput
import habitacionHotel as h
import random

def generarNumero():
    #Debemos completar esta funcion de acuerdo a los criterios establecidos en
    #el planteamiento del problema
    r = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "1234567890"
    r += random.choice(letras)
    r += random.choice(numeros)
    r += random.choice(numeros)
    r += random.choice(letras)
    return r


def crearHabitacionSpec(nombre, camas, servInc, servAd):
    numero = generarNumero()
    habitacion = h.HabitacionHotel(numero, nombre, camas, servInc, servAd)
    return habitacion

def Ocupadas():
    data = []
    with open("C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/Hotel/cuartos.txt") as file:
            for line in file:
                line = line.strip()
                line = line.split(',')
                #.split(',')
                #.split(' ')
                data.append(line)
    return data

def inicializarHabitacionesSpec():
    specs = [["", 2, ["caja seguridad"], []],
            ["", 2, ["caja seguridad", "especiales"], []],
            ["", 2, [], []],
            ["", 1, ["caja seguridad"], []],
            ["", 1, ["caja seguridad"], []],
            ["", 1, ["caja seguridad"], []]]
    ocupa = Ocupadas()
    for i in range(6):
        specs[i][0]=ocupa[i][1]
    habitaciones = {}
    for i in range(len(specs)):
        hab = crearHabitacionSpec(specs[i][0],specs[i][1],specs[i][2],specs[i][3])
        habitaciones[hab.getNumero()] = hab
    return habitaciones
        
def mostrarHabitaciones(habitaciones):
    for n in habitaciones.keys():
        print(n, habitaciones[n].cliente,habitaciones[n].getSerIncl(),habitaciones[n].serviciosAdicionales)

def mostrarHabitacionesDisponibles(habitaciones):
    for n in habitaciones.keys():
        print(n, habitaciones[n].cliente,habitaciones[n].getSerIncl(),habitaciones[n].serviciosAdicionales)

def reservarHabitacion(habitaciones, numero, cliente):
    if(numero in habitaciones.keys()):
        if(habitaciones[numero].ocuparHabitacion(cliente)):
            print("La habitacion " + numero + " fue reservada exitosamente.")
        else:
            print("La habitacion " + numero + " está ocupada por " + habitaciones[numero].cliente)
    else:
        print("El número de habitación proporcionado no es válido.")
    
def liberarHabitacion(habitaciones, numero):
    if(numero in habitaciones.keys()):
        i = list(habitaciones.keys()).index(numero)
        print(str(i+1)+','+str(habitaciones[numero].cliente))
        if(habitaciones[numero].dejarHabitacion()):
            
            with fileinput.FileInput("C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/Hotel/cuartos.txt", inplace=True, backup='.txt') as file:
                for line in file:
                    print(line.replace(str(i+1)+','+str(habitaciones[numero].cliente)+'\n',str(i+1)+',\n'), end='')
            print("La habitacion " + numero + " fue liberada exitosamente.")
        else:
            print("La habitacion " + numero + " ya está desocupada.")
    else:
        print("El número de habitación proporcionado no es válido.")

def mostrarDisponibles(habitaciones):
    disponibles = {}
    for i in list(habitaciones.keys()):
        if(habitaciones[i].getEstatus() == False):
            disponibles[i] = habitaciones[i]
    mostrarHabitaciones(disponibles)
   
def habitacion_dispo(habitaciones, ncamas, cap_diferentes):
    reservado = False
    if cap_diferentes == 1:
        for c in habitaciones.keys():
            if(habitaciones[c].getCamas()==ncamas) and ('especiales' in habitaciones[c].getSerIncl()):
                if(habitaciones[c].getEstatus()==False):
                    print('Habitación '+str(c) +' disponible')
                    nombre = input('Ingrese su nombre por favor: ')
                    habitaciones[c].ocuparHabitacion(nombre)
                    reservado = True
                    print('Habitación '+str(c) +' reservada exitosamente :D')
                else: print('No hay habitaciones con servicios para capacidades diferentes dispible :c')
    else:
        for c in habitaciones.keys():
            if(habitaciones[c].getCamas()==ncamas):
                if(habitaciones[c].getEstatus()==False):
                    nombre = input('Ingrese su nombre por favor: ')
                    habitaciones[c].ocuparHabitacion(nombre)
                    reservado = True
                    print('Habitación '+str(c) +' reservada exitosamente :D')
                    break
def reservar_habitacion(habitaciones):
    ncamas = 3
    while(ncamas > 2):
        ncamas = int(input('Número de camas necesarias: '))
        if ncamas > 2: print('No se pueden ofrecer habitaciones con más de dos camas...  :c')
    cap_diferentes = 3
    while cap_diferentes != 1 and cap_diferentes != 2:
        cap_diferentes = int(input('Requiere servicio para capacidades especiales? ingrese 1 para sí, 2 para no: '))
    habitacion = habitacion_dispo(habitaciones, ncamas, cap_diferentes)

def soliServAdicional(habitaciones,numero):
    servicio = input('Ingrese el servicio que desea: ')
    if(numero in habitaciones.keys()):
        i = list(habitaciones.keys()).index(numero)
        if(habitaciones[numero].solicitarServicioAdicional(servicio)):
            print('Se agregó el servicio '+servicio+' exitosamente.')
        else:
            print('No se pudo agregar el servicio '+servicio+'.')
    else:
        print("El número de habitación proporcionado no es válido.")
# %%

# %%
#mostrarHabitaciones(habitaciones)