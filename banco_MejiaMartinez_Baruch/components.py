from sqlalchemy import false
import models as md
import csv
import random

### usuarios ######################################################

def crearUsuario(nombre, nacimiento, lugarNacimiento, RFC, edad, direccion, telefono, mail):
    cliente = md.persona(nombre, nacimiento, lugarNacimiento, RFC, edad, direccion, telefono, mail)
    return cliente

def inicializarUsuarios():
    path = 'C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/banco_MejiaMartinez_Baruch/'
    file = open(path+"allUsers.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    n = 0
    for row in csvreader:
        rows.append(row)
        n += 1
    data = rows
    file.close()
    clientes = {}
    print(data[0][0])
    for i in range(n):
        print(i)
        nombre = []
        nombre.append(data[i][0])
        nombre.append(data[i][1])
        nombre.append(data[i][2])
        nacimiento = []
        nacimiento.append(data[i][3])
        nacimiento.append(data[i][4])
        nacimiento.append(data[i][5])
        edad = data[i][6]
        lugarNacimiento = data[i][7]
        direccion = data[i][8]
        telefono = data[i][9]
        mail = data[i][10]
        RFC = data[i][11]
        cliente = crearUsuario(nombre, nacimiento, lugarNacimiento, RFC, edad, direccion, telefono, mail)
        clientes[RFC] = cliente 
    return clientes


def registrarCliente(clientes):
    nombre = []
    nombre.append(input('Nombre(s): '))
    nombre.append(input('Apellido PATERNO: '))
    nombre.append(input('Apellido MATERNO: '))
    nacimiento = []
    print('A continuación se le solicitará la fecha de nacimiento en el siguiente formato "DD-MM-AA"')
    nacimiento.append(input('Ingrese el día de nacimiento "DD": '))
    nacimiento.append(input('Ingrese el mes de nacimiento "MM": '))
    nacimiento.append(input('Ingrese el año de nacimiento "AAAA": '))
    edad = 2022 - int(nacimiento[2])
    lugarNacimiento = input('Escriba el lugar de nacimiento: ')
    direccion = input('Escriba la dirección actual: ')
    telefono = input('Escriba el número telefóninco: ')
    mail = input('Escriba el correo electrónico: ')
    RFC = md.persona.generarRFC(nombre, nacimiento)
    cliente = crearUsuario(nombre, nacimiento, lugarNacimiento, RFC, edad, direccion, telefono, mail)
    clientes[RFC] = cliente
    
    path = 'C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/banco_MejiaMartinez_Baruch/'
    data = [nombre[0],nombre[1],nombre[2],nacimiento[0],nacimiento[1],nacimiento[2], lugarNacimiento, RFC, edad, direccion, telefono, mail]
    with open(path+"allUsers.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return clientes

def mostarClientes(clientes):
    print('nombre\t nacimiento\t lugarNacimiento\t RFC\t edad\t direccion\t telefono\t mail:')
    for n in clientes.keys():
        print(str(clientes[n].nombre)+'|'+str(clientes[n].nacimiento)+'|'+str(clientes[n].lugarNacimiento)+'|'+str(n)+'|'+str(clientes[n].edad)+'|'+str(clientes[n].direccion)+'|'+str(clientes[n].telefono)+'|'+str(clientes[n].mail))

def readAllUsers():
    path = 'C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/banco_MejiaMartinez_Baruch/'
    file = open(path+"allUsers.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    return rows

def buscarUsuario(RFC,clientes):
    return clientes[RFC]

def modificarUsuario(RFC,clientes):
    nombre = []
    nombre.append(input('Nombre(s): '))
    nombre.append(input('Apellido PATERNO: '))
    nombre.append(input('Apellido MATERNO: '))
    nacimiento = []
    print('A continuación se le solicitará la fecha de nacimiento en el siguiente formato "DD-MM-AA"')
    nacimiento.append(input('Ingrese el día de nacimiento "DD": '))
    nacimiento.append(input('Ingrese el mes de nacimiento "MM": '))
    nacimiento.append(input('Ingrese el año de nacimiento "AAAA": '))
    edad = 2022 - int(nacimiento[2])
    lugarNacimiento = input('Escriba el lugar de nacimiento: ')
    direccion = input('Escriba la dirección actual: ')
    telefono = input('Escriba el número telefóninco: ')
    mail = input('Escriba el correo electrónico: ')
    cliente = crearUsuario(nombre, nacimiento, lugarNacimiento, RFC, edad, direccion, telefono, mail)
    clientes[RFC] = cliente



### cuenta de banco ######################################################
def crearCuenta(numero, cliente, saldo):
    cliente = md.persona(numero, cliente, saldo)
    return cliente

def inicializarCuentas(clientes):
    path = 'C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/banco_MejiaMartinez_Baruch/'
    file = open(path+"cuentas.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    n = 0
    for row in csvreader:
        rows.append(row)
        n += 1
    data = rows
    file.close()
    cuentas = {}
    print(data[0][0])
    for i in range(n):
        print(i)
        numero = data[i][0]
        cliente = clientes[data[i][1]]
        saldo = data[i][2]
        cuenta = crearCuenta(numero, cliente, saldo)
        cuentas[numero] = cuenta 
    return cuentas


def registrarCuenta(clientes, RFC,cuentas):
    numero = str(random.randint(0, 9)) + str(random.randint(0, 9)) +str(random.randint(0, 9)) +str(random.randint(0, 9)) +str(random.randint(0, 9))+ str(random.randint(0, 9)) +str(random.randint(0, 9))
    cliente = clientes[RFC]
    saldo = 0
    cuentaNueva = crearCuenta(numero, cliente, saldo)
    cuentas[numero] = cuentaNueva
    
    path = 'C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/banco_MejiaMartinez_Baruch/'
    data = [numero, cliente.RFC, saldo]
    with open(path+"cuentas.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return clientes

def mostarCuentas(cuentas):
    print('numero\t cliente\t saldo:')
    for n in cuentas.keys():
        print(str(cuentas[n].numero)+'|'+str(cuentas[n].cliente.nombre)+'|'+str(cuentas[n].saldo))

def operacionesCuenta(numero,cuentas,clientes):
    cuenta = cuentas[numero]
    print('Elija la operacion a realizar introduciendo un numero')
    print('\t 1.Consultar saldo')
    print('\t 2.Modificar saldo')
    print('\t 3.Modificar datos del usuario')
    res = 5
    while (res in range(3)) == False:
        res = int(input('Opcion a elegir: '))
        if res == 0:
            print('Su saldo es de '+str(cuenta.saldo))
        elif res == 1:
            nuevoSaldo = float(input('ingrese el nuevo saldo: '))
            cuenta.saldo = nuevoSaldo
            cuentas[numero] = cuenta
        else:
            print('s')
    return cuentas,clientes