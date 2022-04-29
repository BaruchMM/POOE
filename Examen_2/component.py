import models as md
import random as rn
import csv

import numpy as np

# txt
def readData(path):
    data = []
    with open(path, 'r') as dataShop:
        for line in dataShop:
            line = line.strip()
            line = line.split()
            data.append(line)
    return  data

def readCSV(path):
    file = open(path)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    n = 0
    for row in csvreader:
        rows.append(row)
        n += 1
    data = rows
    file.close()
    return data

##################  client ######################
def getClient(NoCliente, nombre, correo, tipoCliente):
    cliente = md.Cliente(NoCliente, nombre, correo, tipoCliente)
    return cliente

def AllClients():
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allClients.csv'
    data = readCSV(path)
    clientes = {}
    print(data)
    for i in range(len(data)):
        NoCliente = data[i][0]
        print(data[i][0])
        cliente = getClient(NoCliente,data[i][1],data[i][2],data[i][3])
        clientes[NoCliente] = cliente
    return clientes

def viewClients(clientes):
    print('ID     \t Nombre:\t \t Mail: \t TipoCliente:')
    for n in clientes.keys():
        print(str(n)+'|'+str(clientes[n].nombre)+'|'+str(clientes[n].correo)+'|'+str(clientes[n].tipoCliente))

def newClient(clientes):
    NoCliente = md.Cliente.nocliente()
    nombre = input('Introduzca el nombre del cliente: ')
    mail = input('Introduzca el correo electrónico del cliente: ')
    tipo = 0
    print('Tipos de cliente:')
    print('\t1.- Oro')
    print('\t2.- Plata')
    print('\t3.- Bronce')
    while (tipo in ['1','2','3']) == False:
        tipo = input('Introduzca el número de la opción deseada por el cliente: ')
    if tipo == '1':
        tipoCliente = 'Oro'
    elif tipo == '2':
        tipoCliente = 'Plata'
    else:
        tipoCliente = 'Bronce'
    cliente = getClient(NoCliente,nombre,mail,tipoCliente)
    clientes[NoCliente] = cliente
    return clientes

def finDiaClientes(clientes):
    from datetime import date
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allClients.csv'
    data = []
    header = ['NoCliente', 'nombre', 'mail', 'tipoCliente']
    for n in clientes.keys():
        data.append([clientes[n].NoCliente,clientes[n].nombre,clientes[n].correo,clientes[n].tipoCliente])
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
##################  employees ######################
