# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/Estudiantes/Desktop/'
def leerArchivo(fileName):
    data = []
    with open(path + fileName) as file:
        for line in file:
            data.append(line.strip())
    return data
            

fileName = 'diasSemana.txt'
data = leerArchivo(fileName)

fileName = 'WeekDays.txt'
data1 = leerArchivo(fileName)


for i in range(len(data)):
    print('El dia '+data[i]+' en ingles se dice así: '+data1[i])
print(data)

#################################################################
vocales = {'a':0, 'e':0, 'i':0, 'o':0,'u':0}
pathMoon = 'C:/Users/Estudiantes/Desktop/'
datosLuna = open(pathMoon+'moon.txt', encoding="utf8")
for i in datosLuna:
    for letra in i:
        letra = letra.lower()
        if letra in vocales.keys():
            vocales[letra] += 1 
print(vocales)

##################################################################
contenido = []
with open(path + 'tienda.txt', 'r') as dataShop:
    for line in dataShop:
        line = line.strip()
        line = line.split('\t')
        #.split(',')
        #.split(' ')
        contenido.append(line)
print(contenido)

###################################################################
empleados = {}
with open(path + 'datosEmpleados.txt', 'r') as dataShop:
    for line in dataShop:
        line = line.strip()
        line = line.split(',')
        #.split(',')
        #.split(' ')
        empleados[line[0]] = [line[1], int(line[2]),line[3]]
def calcularEdadesEmpleados(empleados):
    for e in empleados.keys():
        datosE = empleados[e]
        print(e + ' tiempos '+str(2022-datosE[1]) + ' años.') 

calcularEdadesEmpleados(empleados)
